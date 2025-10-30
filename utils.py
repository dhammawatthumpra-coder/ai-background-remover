"""
Utility Functions Module - Background Remover v12.0
ฟังก์ชันเสริมสำหรับการประมวลผลภาพ
"""

from PIL import Image, ImageFilter
import numpy as np
from config import TRANSPARENCY_GRID, AUTO_CROP_PADDING


def create_transparency_grid(width, height, grid_size=None):
    """
    สร้างพื้นหลังตารางโปร่งใสแบบ Photoshop
    
    Args:
        width: ความกว้างของภาพ
        height: ความสูงของภาพ
        grid_size: ขนาดของแต่ละช่องตาราง (default จาก config)
    
    Returns:
        PIL Image: ภาพพื้นหลังตาราง
    """
    if grid_size is None:
        grid_size = TRANSPARENCY_GRID['size']
    
    grid_img = Image.new('RGB', (width, height), '#ffffff')
    
    color1 = TRANSPARENCY_GRID['color1']
    color2 = TRANSPARENCY_GRID['color2']
    
    for y in range(0, height, grid_size):
        for x in range(0, width, grid_size):
            if (x // grid_size + y // grid_size) % 2 == 0:
                color = color1
            else:
                color = color2
            
            for py in range(y, min(y + grid_size, height)):
                for px in range(x, min(x + grid_size, width)):
                    grid_img.putpixel((px, py), color)
    
    return grid_img


def crop_transparent(image, padding=None):
    """
    ตัดขอบโปร่งใส (Auto Crop)
    
    Args:
        image: PIL Image ที่ต้องการตัดขอบ
        padding: ระยะขอบที่เหลือ (default จาก config)
    
    Returns:
        PIL Image: ภาพที่ตัดขอบแล้ว
    """
    try:
        if padding is None:
            padding = AUTO_CROP_PADDING
        
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        bbox = image.getbbox()
        
        if bbox:
            bbox_padded = (
                max(0, bbox[0] - padding),
                max(0, bbox[1] - padding),
                min(image.width, bbox[2] + padding),
                min(image.height, bbox[3] + padding)
            )
            return image.crop(bbox_padded)
        else:
            return image
    except Exception as e:
        print(f"Crop error: {e}")
        return image


def apply_minimum_filter(image, iterations=1):
    """
    ใช้ Gaussian Blur + Threshold แทน Binary Erosion
    เพื่อกัดขอบภาพให้กระชับขึ้น
    
    Args:
        image: PIL Image ที่ต้องการประมวลผล
        iterations: จำนวนรอบการกัดขอบ (1-20)
    
    Returns:
        PIL Image: ภาพที่ประมวลผลแล้ว
    """
    try:
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        r, g, b, a = image.split()
        
        if iterations > 0:
            alpha_img = a
            
            # ใช้ Gaussian Blur ตามจำนวน iterations
            blur_radius = iterations * 0.5
            alpha_img = alpha_img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
            
            # ปรับ threshold ตามจำนวน iterations
            threshold = 255 - (iterations * 15)
            threshold = max(threshold, 128)
            
            # แปลงเป็น array และใช้ threshold
            alpha_array = np.array(alpha_img)
            alpha_array[alpha_array < threshold] = 0
            
            new_alpha = Image.fromarray(alpha_array)
            
            result = Image.merge('RGBA', (r, g, b, new_alpha))
            return result
        
        return image
        
    except Exception as e:
        print(f"Minimum filter error: {e}")
        return image


def resize_image_aspect_ratio(image, target_width=None, target_height=None, max_size=None):
    """
    ปรับขนาดภาพโดยรักษาอัตราส่วน
    
    Args:
        image: PIL Image
        target_width: ความกว้างเป้าหมาย
        target_height: ความสูงเป้าหมาย
        max_size: ขนาดสูงสุด (width, height)
    
    Returns:
        PIL Image: ภาพที่ปรับขนาดแล้ว
    """
    if max_size:
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        return image
    
    if target_width and target_height:
        return image.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    if target_width:
        ratio = target_width / image.width
        new_height = int(image.height * ratio)
        return image.resize((target_width, new_height), Image.Resampling.LANCZOS)
    
    if target_height:
        ratio = target_height / image.height
        new_width = int(image.width * ratio)
        return image.resize((new_width, target_height), Image.Resampling.LANCZOS)
    
    return image


def calculate_fit_to_screen_scale(image_width, image_height, canvas_width, canvas_height, padding=0.95):
    """
    คำนวณ scale สำหรับ Fit to Screen
    
    Args:
        image_width: ความกว้างของภาพ
        image_height: ความสูงของภาพ
        canvas_width: ความกว้างของ canvas
        canvas_height: ความสูงของ canvas
        padding: ระยะขอบ (0.0-1.0)
    
    Returns:
        float: scale ที่เหมาะสม
    """
    if canvas_width <= 1 or canvas_height <= 1:
        return 1.0
    
    width_scale = canvas_width / image_width
    height_scale = canvas_height / image_height
    
    return min(width_scale, height_scale) * padding


def get_model_display_name(model_key, ai_models_dict):
    """
    ดึงชื่อแสดงผลของ Model
    
    Args:
        model_key: key ของ model
        ai_models_dict: dictionary ของ models
    
    Returns:
        str: ชื่อแสดงผล (ส่วนในวงเล็บ)
    """
    model_name = ai_models_dict.get(model_key, "")
    if "(" in model_name:
        display_name = model_name.split("(")[1].rstrip(")")
        return f"({display_name})"
    return ""


def validate_image_format(file_path, supported_formats):
    """
    ตรวจสอบว่าไฟล์เป็นรูปแบบที่รองรับหรือไม่
    
    Args:
        file_path: path ของไฟล์
        supported_formats: list ของรูปแบบที่รองรับ
    
    Returns:
        bool: True ถ้ารองรับ
    """
    ext = file_path.lower().split('.')[-1]
    for fmt in supported_formats:
        if ext in fmt.replace('*', '').replace('.', ''):
            return True
    return False
