"""
AI Model Manager Module - Background Remover v12.2
จัดการ AI Models ทั้งหมด (Loading, Switching, Processing)
รองรับ Local Models Folder + Multi-language
"""

import os
import sys
import io
import threading
from pathlib import Path
from rembg import remove, new_session
from PIL import Image

from config import (
    AI_MODELS, MODEL_MINIMUM_DEFAULTS, DEFAULT_SETTINGS,
    ALPHA_MATTING_CONFIG, COLORS, get_text
)


def setup_local_models_path():
    """
    ตั้งค่า path สำหรับ local models folder
    
    รองรับ 3 ตำแหน่ง:
    1. ./models/ (ใน folder เดียวกับ script)
    2. ~/.u2net/ (default cache folder)
    3. bundled models (สำหรับ PyInstaller)
    
    Returns:
        str: path ที่ใช้งาน
    """
    # 1. ลอง ./models/ ก่อน (local folder)
    script_dir = Path(__file__).parent
    local_models = script_dir / "models"
    
    if local_models.exists() and local_models.is_dir():
        # ตรวจสอบว่ามีไฟล์ .onnx อยู่จริง
        onnx_files = list(local_models.glob("*.onnx"))
        if onnx_files:
            os.environ['U2NET_HOME'] = str(local_models)
            print(f"✅ Using local models from: {local_models}")
            return str(local_models)
    
    # 2. ลอง bundled models (PyInstaller)
    if getattr(sys, 'frozen', False):
        bundle_dir = Path(sys._MEIPASS)
        model_dir = bundle_dir / '.u2net'
        if model_dir.exists():
            os.environ['U2NET_HOME'] = str(model_dir)
            print(f"✅ Using bundled models from: {model_dir}")
            return str(model_dir)
    
    # 3. ใช้ default cache (~/.u2net/)
    default_cache = Path.home() / '.u2net'
    print(f"ℹ️ Using default cache: {default_cache}")
    return str(default_cache)


class AIModelManager:
    """ตัวจัดการ AI Models (รองรับหลายภาษา)"""
    
    def __init__(self, root, status_callback, on_ready_callback=None, on_error_callback=None, lang='th'):
        """
        สร้าง AI Model Manager
        
        Args:
            root: tkinter root window (สำหรับ root.after)
            status_callback: ฟังก์ชันสำหรับอัปเดตสถานะ
            on_ready_callback: ฟังก์ชันเรียกเมื่อ model พร้อม
            on_error_callback: ฟังก์ชันเรียกเมื่อเกิด error
            lang: ภาษา ('en' หรือ 'th')
        """
        self.root = root
        self.status_callback = status_callback
        self.on_ready_callback = on_ready_callback
        self.on_error_callback = on_error_callback
        self.lang = lang
        
        # Model state
        self.session = None
        self.is_loaded = False
        self.current_model = DEFAULT_SETTINGS['model']
        
        # ตั้งค่า local models path
        self.models_path = setup_local_models_path()
        
        # โหลด model แบบ async
        self._init_model_async()
    
    def _init_model_async(self):
        """โหลด model แบบ background thread"""
        threading.Thread(target=self._load_model, 
                        args=(self.current_model,), 
                        daemon=True).start()
    
    def _load_model(self, model_key):
        """
        โหลด AI Model
        
        Args:
            model_key: key ของ model ที่ต้องการโหลด
        """
        try:
            # กำหนด path สำหรับ bundled models (สำหรับ PyInstaller)
            if getattr(sys, 'frozen', False):
                bundle_dir = sys._MEIPASS
                model_dir = os.path.join(bundle_dir, '.u2net')
                if os.path.exists(model_dir):
                    os.environ['U2NET_HOME'] = model_dir
            
            # ลอง fallback เป็น u2net ถ้า model เริ่มต้นมีปัญหา
            try:
                self.session = new_session(model_key)
                self.current_model = model_key
                success_model = AI_MODELS.get(model_key, model_key)
            except Exception as e:
                error_str = str(e)
                # ถ้าเป็น ONNX error ให้ใช้ u2net แทน
                if "ONNX" in error_str or "external" in error_str:
                    print(f"Model {model_key} failed, using u2net instead")
                    self.session = new_session('u2net')
                    self.current_model = 'u2net'
                    success_model = "U2-Net (Fallback)"
                    
                    warning_template = "⚠️ {} requires additional files - Using U2-Net instead" if self.lang == 'en' else "⚠️ {} ต้องการไฟล์เพิ่มเติม - ใช้ U2-Net แทน"
                    warning_msg = warning_template.format(AI_MODELS.get(model_key, model_key))
                    
                    self.root.after(0, lambda: self.status_callback(
                        warning_msg,
                        COLORS['warning']
                    ))
                else:
                    raise
            
            self.is_loaded = True
            
            # แจ้งว่าโหลดสำเร็จ
            msg = get_text('model_loaded', self.lang).format(success_model)
            self.root.after(0, lambda: self.status_callback(msg, COLORS['success']))
            
            # เรียก callback
            if self.on_ready_callback:
                self.root.after(0, self.on_ready_callback)
                
        except Exception as e:
            error_msg = str(e)
            self.is_loaded = False
            self.session = None
            
            # แจ้ง error
            if self.on_error_callback:
                self.root.after(0, lambda msg=error_msg: self.on_error_callback(msg))
    
    def switch_model(self, new_model_key, on_complete=None):
        """
        เปลี่ยน AI Model
        
        Args:
            new_model_key: key ของ model ใหม่
            on_complete: ฟังก์ชันเรียกเมื่อเสร็จสิ้น
        """
        if not self.is_loaded:
            return
        
        def _switch():
            try:
                model_name = AI_MODELS.get(new_model_key, new_model_key)
                
                # แจ้งว่ากำลังโหลด
                msg = get_text('model_loading', self.lang).format(model_name)
                self.root.after(0, lambda: self.status_callback(msg, COLORS['warning']))
                
                # โหลด model ใหม่
                self.session = new_session(new_model_key)
                self.current_model = new_model_key
                
                # แจ้งว่าโหลดสำเร็จ
                success_msg = get_text('model_loaded', self.lang).format(model_name)
                self.root.after(0, lambda: self.status_callback(success_msg, COLORS['success']))
                
                # เรียก callback
                if on_complete:
                    self.root.after(0, on_complete)
                    
            except Exception as e:
                error_msg = str(e)
                self.root.after(0, lambda msg=error_msg: self._handle_switch_error(msg))
        
        threading.Thread(target=_switch, daemon=True).start()
    
    def _handle_switch_error(self, error_msg):
        """จัดการ error เมื่อเปลี่ยน model"""
        # แสดง error
        if "ONNX" in error_msg or "external" in error_msg:
            if self.lang == 'en':
                error_display = "⚠️ This model requires additional files - Switching to U2-Net"
            else:
                error_display = "⚠️ Model นี้ต้องการไฟล์เพิ่มเติม - กำลังเปลี่ยนเป็น U2-Net"
        else:
            if self.lang == 'en':
                error_display = "⚠️ Model Error - Switching to U2-Net"
            else:
                error_display = "⚠️ Model Error - กำลังเปลี่ยนเป็น U2-Net"
        
        self.root.after(0, lambda: self.status_callback(error_display, COLORS['warning']))
        
        # Reset กลับไป u2net (เสถียรที่สุด)
        fallback_model = 'u2net'
        try:
            self.current_model = fallback_model
            self.session = new_session(fallback_model)
            
            if self.lang == 'en':
                success_msg = f"✅ Switched to {AI_MODELS[fallback_model]}"
            else:
                success_msg = f"✅ เปลี่ยนเป็น {AI_MODELS[fallback_model]} แล้ว"
            
            self.root.after(0, lambda: self.status_callback(success_msg, COLORS['success']))
        except:
            # ถ้า u2net ก็ล้มเหลว ให้แจ้ง error
            if self.on_error_callback:
                if self.lang == 'en':
                    error = "❌ Cannot load Model\nPlease install: pip install --upgrade rembg"
                else:
                    error = "❌ ไม่สามารถโหลด Model ได้\nกรุณาติดตั้ง: pip install --upgrade rembg"
                
                self.root.after(0, lambda: self.on_error_callback(error))
    
    def get_recommended_minimum(self):
        """
        ดึงค่า Minimum Filter ที่แนะนำสำหรับ model ปัจจุบัน
        
        Returns:
            int: ค่าแนะนำ (0-20)
        """
        return MODEL_MINIMUM_DEFAULTS.get(self.current_model, 2)
    
    def remove_background(self, input_image, alpha_matting=False, 
                         on_progress=None, on_complete=None, on_error=None):
        """
        ลบพื้นหลังรูปภาพ
        
        Args:
            input_image: PIL Image ต้นฉบับ
            alpha_matting: เปิดใช้ Alpha Matting หรือไม่
            on_progress: ฟังก์ชัน callback สำหรับ progress (รับพารามิเตอร์ percentage)
            on_complete: ฟังก์ชัน callback เมื่อสำเร็จ (รับพารามิเตอร์ output_image)
            on_error: ฟังก์ชัน callback เมื่อเกิด error (รับพารามิเตอร์ error_msg)
        """
        if not self.is_loaded or not self.session:
            if on_error:
                error = get_text('no_image', self.lang)
                self.root.after(0, lambda: on_error(error))
            return
        
        def _process():
            try:
                # แจ้งว่ากำลังประมวลผล
                model_name = AI_MODELS.get(self.current_model, self.current_model)
                msg = get_text('processing', self.lang).format(model_name)
                self.root.after(0, lambda: self.status_callback(msg, COLORS['warning']))
                
                # Progress callback
                if on_progress:
                    for i in range(10):
                        self.root.after(0, lambda val=i: on_progress((val + 1) * 10))
                        import time
                        time.sleep(0.2)
                
                # แปลงเป็น bytes
                img_byte_arr = io.BytesIO()
                input_image.save(img_byte_arr, format='PNG')
                img_byte_arr.seek(0)
                
                # ลบพื้นหลัง
                if alpha_matting:
                    output_byte_arr = remove(
                        img_byte_arr.read(),
                        session=self.session,
                        alpha_matting=True,
                        alpha_matting_foreground_threshold=ALPHA_MATTING_CONFIG['foreground_threshold'],
                        alpha_matting_background_threshold=ALPHA_MATTING_CONFIG['background_threshold'],
                        alpha_matting_erode_size=ALPHA_MATTING_CONFIG['erode_size']
                    )
                else:
                    output_byte_arr = remove(
                        img_byte_arr.read(),
                        session=self.session
                    )
                
                # แปลงกลับเป็น Image
                output_image = Image.open(io.BytesIO(output_byte_arr))
                
                # Progress สำเร็จ
                if on_progress:
                    self.root.after(0, lambda: on_progress(100))
                
                # แจ้งว่าสำเร็จ
                success_msg = get_text('success', self.lang)
                self.root.after(0, lambda: self.status_callback(success_msg, COLORS['success']))
                
                # เรียก callback
                if on_complete:
                    self.root.after(0, lambda img=output_image: on_complete(img))
                    
            except Exception as e:
                error_msg = str(e)
                
                # Reset progress
                if on_progress:
                    self.root.after(0, lambda: on_progress(0))
                
                # แจ้ง error
                error = get_text('error', self.lang)
                self.root.after(0, lambda: self.status_callback(error, "#ef4444"))
                
                # เรียก callback
                if on_error:
                    if "ONNX" in error_msg or "external" in error_msg:
                        error = get_text('model_not_supported', self.lang)
                        self.root.after(0, lambda: on_error(error))
                    else:
                        error = get_text('processing_failed', self.lang).format(error_msg[:300])
                        self.root.after(0, lambda: on_error(error))
        
        threading.Thread(target=_process, daemon=True).start()
    
    def is_ready(self):
        """
        ตรวจสอบว่า model พร้อมใช้งานหรือไม่
        
        Returns:
            bool: True ถ้าพร้อม
        """
        return self.is_loaded and self.session is not None
    
    def get_current_model_name(self):
        """
        ดึงชื่อ model ปัจจุบัน
        
        Returns:
            str: ชื่อ model
        """
        return AI_MODELS.get(self.current_model, self.current_model)
    
    def get_current_model_key(self):
        """
        ดึง key ของ model ปัจจุบัน
        
        Returns:
            str: key ของ model
        """
        return self.current_model