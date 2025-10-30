"""
Image Handler Module - Background Remover v12.2
จัดการการแสดงผลและประมวลผลภาพ
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageEnhance
from config import *
from utils import *
from widgets import *


class ImageDisplayManager:
    """จัดการการแสดงผลภาพทั้งหมด"""
    
    def __init__(self, app):
        """
        สร้าง Image Display Manager
        
        Args:
            app: BackgroundRemoverApp instance
        """
        self.app = app
    
    def create_tabs(self, parent):
        """สร้าง 3 Tabs สำหรับแสดงภาพ"""
        lang = self.app.current_lang
        
        main = tk.Frame(parent, bg=COLORS['bg'])
        main.grid(row=1, column=0, sticky='nsew', padx=15, pady=5)
        
        # Style for Notebook
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Custom.TNotebook", background=COLORS['bg'], borderwidth=0)
        style.configure("Custom.TNotebook.Tab", background=COLORS['card'],
                       foreground=COLORS['text'], padding=[20, 10], 
                       font=("Segoe UI", 11, "bold"))
        style.map("Custom.TNotebook.Tab",
                 background=[("selected", COLORS['accent'])],
                 foreground=[("selected", "#ffffff")])
        
        self.notebook = ttk.Notebook(main, style="Custom.TNotebook")
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        self.create_input_tab()
        self.create_output_tab()
        self.create_compare_tab()
        
        return self.notebook
    
    def create_input_tab(self):
        """Tab 1: รูปภาพต้นฉบับ"""
        lang = self.app.current_lang
        
        tab = tk.Frame(self.notebook, bg=COLORS['bg'])
        self.notebook.add(tab, text=get_text('tab_original', lang))
        
        card = tk.Frame(tab, bg=COLORS['card'])
        card.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        header = tk.Frame(card, bg=COLORS['card'])
        header.pack(fill=tk.X)
        
        self.input_tab_header = tk.Label(header, text=get_text('original_image', lang),
                                         font=("Segoe UI", 13, "bold"),
                                         bg=COLORS['card'], fg=COLORS['text'], pady=12)
        self.input_tab_header.pack(side=tk.LEFT, padx=12)
        
        # Zoom controls
        self.input_zoom_controls = ZoomControls(
            header, COLORS['card'], COLORS['text'],
            self.app.input_zoom_in, self.app.input_zoom_out, self.app.input_zoom_reset
        )
        self.input_zoom_controls.pack(side=tk.RIGHT, padx=12, pady=12)
        
        # Image canvas
        self.input_canvas_widget = ImageCanvas(
            card, COLORS['card'],
            get_text('no_image_selected', lang)
        )
        self.input_canvas_widget.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))
        self.input_canvas_widget.on_resize = self.app.on_input_canvas_resize
    
    def create_output_tab(self):
        """Tab 2: ผลลัพธ์"""
        lang = self.app.current_lang
        
        tab = tk.Frame(self.notebook, bg=COLORS['bg'])
        self.notebook.add(tab, text=get_text('tab_result', lang))
        
        card = tk.Frame(tab, bg=COLORS['card'])
        card.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        header = tk.Frame(card, bg=COLORS['card'])
        header.pack(fill=tk.X)
        
        self.output_tab_header = tk.Label(header, text=get_text('result_image', lang),
                                          font=("Segoe UI", 13, "bold"),
                                          bg=COLORS['card'], fg=COLORS['text'], pady=12)
        self.output_tab_header.pack(side=tk.LEFT, padx=12)
        
        # Zoom controls
        self.output_zoom_controls = ZoomControls(
            header, COLORS['card'], COLORS['text'],
            self.app.zoom_in, self.app.zoom_out, self.app.zoom_reset
        )
        self.output_zoom_controls.pack(side=tk.RIGHT, padx=12, pady=12)
        
        # Image canvas
        self.output_canvas_widget = ImageCanvas(
            card, COLORS['card'],
            get_text('waiting_result', lang)
        )
        self.output_canvas_widget.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))
        self.output_canvas_widget.on_resize = self.app.on_output_canvas_resize
    
    def create_compare_tab(self):
        """Tab 3: เปรียบเทียบ"""
        lang = self.app.current_lang
        
        tab = tk.Frame(self.notebook, bg=COLORS['bg'])
        self.notebook.add(tab, text=get_text('tab_compare', lang))
        
        compare_frame = tk.Frame(tab, bg=COLORS['bg'])
        compare_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        left = tk.Frame(compare_frame, bg=COLORS['card'])
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 3))
        
        self.compare_before_label = tk.Label(left, text=get_text('before', lang),
                                            font=("Segoe UI", 10, "bold"),
                                            bg=COLORS['card'], fg=COLORS['text'], pady=5)
        self.compare_before_label.pack(fill=tk.X)
        
        self.compare_input_label = tk.Label(left, text="", bg="#1e1e1e",
                                           fg=COLORS['text_dim'], font=("Segoe UI", 9))
        self.compare_input_label.pack(fill=tk.BOTH, expand=True, padx=3, pady=(0, 3))
        
        right = tk.Frame(compare_frame, bg=COLORS['card'])
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(3, 0))
        
        self.compare_after_label = tk.Label(right, text=get_text('after', lang),
                                           font=("Segoe UI", 10, "bold"),
                                           bg=COLORS['card'], fg=COLORS['text'], pady=5)
        self.compare_after_label.pack(fill=tk.X)
        
        self.compare_output_label = tk.Label(right, text="", bg="#1e1e1e",
                                            fg=COLORS['text_dim'], font=("Segoe UI", 9))
        self.compare_output_label.pack(fill=tk.BOTH, expand=True, padx=3, pady=(0, 3))
    
    def refresh_tab_texts(self, lang):
        """รีเฟรช Tab texts เป็นภาษาใหม่"""
        self.notebook.tab(0, text=get_text('tab_original', lang))
        self.notebook.tab(1, text=get_text('tab_result', lang))
        self.notebook.tab(2, text=get_text('tab_compare', lang))
        
        self.input_tab_header.config(text=get_text('original_image', lang))
        self.output_tab_header.config(text=get_text('result_image', lang))
        self.compare_before_label.config(text=get_text('before', lang))
        self.compare_after_label.config(text=get_text('after', lang))
        
        # อัปเดต placeholders
        if not self.app.input_image:
            self.input_canvas_widget.set_placeholder(get_text('no_image_selected', lang))
        if not self.app.output_image:
            self.output_canvas_widget.set_placeholder(get_text('waiting_result', lang))
    
    def center_canvas_item(self, canvas, item_id, image, zoom):
        """จัดกึ่งกลางภาพใน Canvas"""
        if not image:
            return
        
        cw = canvas.winfo_width()
        ch = canvas.winfo_height()
        
        if cw <= 1:
            cw = CANVAS_DEFAULT_SIZE['width']
        if ch <= 1:
            ch = CANVAS_DEFAULT_SIZE['height']
        
        nw = int(image.width * zoom)
        nh = int(image.height * zoom)
        
        canvas.configure(scrollregion=(0, 0, nw, nh))
        
        if nw < cw and nh < ch:
            x_pos = (cw - nw) // 2
            y_pos = (ch - nh) // 2
            canvas.coords(item_id, x_pos, y_pos)
        else:
            canvas.coords(item_id, 0, 0)
    
    def display_input_image(self, reset_zoom=False):
        """แสดงรูปภาพต้นฉบับ"""
        if not self.app.input_image:
            return
        
        canvas = self.input_canvas_widget.canvas
        cw = canvas.winfo_width()
        ch = canvas.winfo_height()
        
        if cw <= 1:
            cw = CANVAS_DEFAULT_SIZE['width']
        if ch <= 1:
            ch = CANVAS_DEFAULT_SIZE['height']
        
        if reset_zoom:
            self.app.input_zoom_level = calculate_fit_to_screen_scale(
                self.app.input_image.width, self.app.input_image.height, cw, ch
            )
            self.input_zoom_controls.update_label(self.app.input_zoom_level)
        
        img = self.app.input_image.copy()
        new_width = int(img.width * self.app.input_zoom_level)
        new_height = int(img.height * self.app.input_zoom_level)
        
        if new_width > 0 and new_height > 0:
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        photo = ImageTk.PhotoImage(img)
        self.input_canvas_widget.set_image(photo)
        self.input_canvas_widget.configure_scrollregion(new_width, new_height)
        self.center_canvas_item(canvas, self.input_canvas_widget.canvas_id,
                               self.app.input_image, self.app.input_zoom_level)
    
    def display_output_image(self, reset_zoom=False):
        """แสดงรูปภาพผลลัพธ์พร้อม Transparency Grid"""
        if not self.app.output_image:
            return
        
        canvas = self.output_canvas_widget.canvas
        cw = canvas.winfo_width()
        ch = canvas.winfo_height()
        
        if cw <= 1:
            cw = CANVAS_DEFAULT_SIZE['width']
        if ch <= 1:
            ch = CANVAS_DEFAULT_SIZE['height']
        
        if reset_zoom:
            self.app.zoom_level = calculate_fit_to_screen_scale(
                self.app.output_image.width, self.app.output_image.height, cw, ch
            )
            self.output_zoom_controls.update_label(self.app.zoom_level)
        
        img = self.app.output_image.copy()
        new_width = int(img.width * self.app.zoom_level)
        new_height = int(img.height * self.app.zoom_level)
        
        if new_width > 0 and new_height > 0:
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        if self.app.transparency_grid.get() and img.mode == 'RGBA':
            grid = create_transparency_grid(new_width, new_height)
            grid.paste(img, (0, 0), img)
            img = grid
        
        photo = ImageTk.PhotoImage(img)
        self.output_canvas_widget.set_image(photo)
        self.output_canvas_widget.configure_scrollregion(new_width, new_height)
        self.center_canvas_item(canvas, self.output_canvas_widget.canvas_id,
                               self.app.output_image, self.app.zoom_level)
    
    def update_compare(self):
        """อัปเดตหน้า Compare"""
        self.app.root.after(50, self._update_compare_images)
    
    def _update_compare_images(self):
        """อัปเดตภาพจริงหลัง widget พร้อม"""
        if self.app.input_image:
            cw = self.compare_input_label.winfo_width()
            ch = self.compare_input_label.winfo_height()
            
            if cw <= 1:
                cw = 700
            if ch <= 1:
                ch = 800
            
            img = self.app.input_image.copy()
            scale = calculate_fit_to_screen_scale(img.width, img.height, cw, ch, 0.98)
            
            new_width = int(img.width * scale)
            new_height = int(img.height * scale)
            
            if new_width > 0 and new_height > 0:
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(img)
            self.compare_input_label.config(image=photo, text='')
            self.compare_input_label.image = photo
        
        if self.app.output_image:
            cw = self.compare_output_label.winfo_width()
            ch = self.compare_output_label.winfo_height()
            
            if cw <= 1:
                cw = 700
            if ch <= 1:
                ch = 800
            
            img = self.app.output_image.copy()
            scale = calculate_fit_to_screen_scale(img.width, img.height, cw, ch, 0.98)
            
            new_width = int(img.width * scale)
            new_height = int(img.height * scale)
            
            if new_width > 0 and new_height > 0:
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            if self.app.transparency_grid.get() and img.mode == 'RGBA':
                grid = create_transparency_grid(new_width, new_height)
                grid.paste(img, (0, 0), img)
                img = grid
            
            photo = ImageTk.PhotoImage(img)
            self.compare_output_label.config(image=photo, text='')
            self.compare_output_label.image = photo


class ImageProcessor:
    """จัดการการประมวลผลภาพ"""
    
    def __init__(self, app):
        """
        สร้าง Image Processor
        
        Args:
            app: BackgroundRemoverApp instance
        """
        self.app = app
    
    def reapply_filters(self):
        """ประมวลผลใหม่เมื่อเปลี่ยน Minimum Filter"""
        try:
            if not hasattr(self.app, 'original_output_image') or self.app.original_output_image is None:
                return
            
            processed_image = self.app.original_output_image.copy()
            
            min_value = self.app.minimum_filter.get()
            if min_value > 0:
                processed_image = apply_minimum_filter(processed_image, iterations=min_value)
            
            if self.app.auto_crop.get():
                processed_image = crop_transparent(processed_image)
            
            self.app.output_image = processed_image
            
            self.app.root.after(0, lambda: self.app.display_manager.display_output_image(reset_zoom=True))
            self.app.root.after(0, lambda: self.app.display_manager.update_compare())
            
            msg = get_text('minimum_applied', self.app.current_lang).format(min_value)
            self.app.root.after(0, lambda: self.app.update_status(msg, COLORS['success']))
            
        except Exception as e:
            print(f"Reapply filters error: {e}")
            self.app.root.after(0, lambda: self.app.update_status(
                "❌ Error in Minimum Filter",
                "#ef4444"
            ))
    
    def apply_global_adjust(self):
        """อัปเดตภาพเมื่อปรับ Brightness / Contrast / Saturation"""
        if not hasattr(self.app, "cropped_output_image") or self.app.cropped_output_image is None:
            return

        base_img = self.app.cropped_output_image.copy()

        bright = self.app.brightness_var.get()
        contrast = self.app.contrast_var.get()
        satur = self.app.saturation_var.get()

        img = ImageEnhance.Brightness(base_img).enhance(bright)
        img = ImageEnhance.Contrast(img).enhance(contrast)
        img = ImageEnhance.Color(img).enhance(satur)

        self.app.output_image = img
        self.app.display_manager.display_output_image()
        self.app.display_manager.update_compare()

        msg = get_text('adjust_applied', self.app.current_lang).format(bright, contrast, satur)
        self.app.update_status(msg, COLORS['success'])

    def reset_adjust(self):
        """รีเซ็ตค่าการปรับแสงโดยไม่กระทบการ Crop"""
        self.app.brightness_var.set(1.0)
        self.app.contrast_var.set(1.0)
        self.app.saturation_var.set(1.0)

        if hasattr(self.app, "cropped_output_image") and self.app.cropped_output_image is not None:
            self.app.output_image = self.app.cropped_output_image.copy()
            self.app.display_manager.display_output_image()
            self.app.display_manager.update_compare()

        msg = get_text('adjust_reset', self.app.current_lang)
        self.app.update_status(msg, COLORS['success'])
    
    def rotate_image(self):
        """หมุนภาพ 90 องศา"""
        if self.app.output_image:
            self.app.output_image = self.app.output_image.rotate(-90, expand=True)
            self.app.display_manager.display_output_image(reset_zoom=True)
            self.app.display_manager.update_compare()
            msg = get_text('rotate', self.app.current_lang)
            self.app.update_status(msg, COLORS['success'])
        elif self.app.input_image:
            self.app.input_image = self.app.input_image.rotate(-90, expand=True)
            self.app.display_manager.display_input_image(reset_zoom=True)
            self.app.display_manager.update_compare()
            msg = get_text('rotate', self.app.current_lang)
            self.app.update_status(msg, COLORS['success'])
    
    def flip_horizontal(self):
        """พลิกภาพซ้าย-ขวา"""
        if self.app.output_image:
            self.app.output_image = ImageOps.mirror(self.app.output_image)
            self.app.display_manager.display_output_image(reset_zoom=True)
            self.app.display_manager.update_compare()
            msg = get_text('flip_h', self.app.current_lang)
            self.app.update_status(msg, COLORS['success'])
        elif self.app.input_image:
            self.app.input_image = ImageOps.mirror(self.app.input_image)
            self.app.display_manager.display_input_image(reset_zoom=True)
            self.app.display_manager.update_compare()
            msg = get_text('flip_h', self.app.current_lang)
            self.app.update_status(msg, COLORS['success'])
    
    def flip_vertical(self):
        """พลิกภาพบน-ล่าง"""
        if self.app.output_image:
            self.app.output_image = ImageOps.flip(self.app.output_image)
            self.app.display_manager.display_output_image(reset_zoom=True)
            self.app.display_manager.update_compare()
            msg = get_text('flip_v', self.app.current_lang)
            self.app.update_status(msg, COLORS['success'])
        elif self.app.input_image:
            self.app.input_image = ImageOps.flip(self.app.input_image)
            self.app.display_manager.display_input_image(reset_zoom=True)
            self.app.display_manager.update_compare()
            msg = get_text('flip_v', self.app.current_lang)
            self.app.update_status(msg, COLORS['success'])