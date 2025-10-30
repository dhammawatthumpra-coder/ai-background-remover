"""
UI Components Module - Background Remover v12.2
แยก UI Components ออกมาเป็น module
"""

import tkinter as tk
from tkinter import ttk
from config import *
from widgets import *


class TopBar:
    """แถบด้านบน (Settings bar)"""
    
    def __init__(self, parent, app):
        """
        สร้าง Top Bar
        
        Args:
            parent: parent widget
            app: BackgroundRemoverApp instance (เพื่อเข้าถึง methods และ variables)
        """
        self.app = app
        self.lang = app.current_lang
        
        top = tk.Frame(parent, bg=COLORS['card'], height=70)
        top.grid(row=0, column=0, sticky='ew')
        top.grid_propagate(False)
        
        # Left side - Settings
        left = tk.Frame(top, bg=COLORS['card'])
        left.pack(side=tk.LEFT, padx=15, pady=12)
        
        self.settings_label = tk.Label(left, text=get_text('settings', self.lang),
                                       font=("Segoe UI", 11, "bold"),
                                       bg=COLORS['card'], fg=COLORS['text'])
        self.settings_label.pack(side=tk.LEFT, padx=(0, 15))
        
        self.ai_model_label = tk.Label(left, text=get_text('ai_model', self.lang),
                                       font=("Segoe UI", 9),
                                       bg=COLORS['card'], fg=COLORS['text'])
        self.ai_model_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Style for Combobox
        self._setup_combobox_style()
        
        # Model Dropdown
        self.model_dropdown = ttk.Combobox(
            left,
            textvariable=app.model_choice,
            values=list(AI_MODELS.keys()),
            state='readonly',
            width=32,
            font=("Segoe UI", 9),
            style='Custom.TCombobox'
        )
        self.model_dropdown.pack(side=tk.LEFT, padx=5)
        
        self.model_label = tk.Label(left, text="", font=("Segoe UI", 8),
                                    bg=COLORS['card'], fg=COLORS['text_dim'])
        self.model_label.pack(side=tk.LEFT, padx=(5, 10))
        self.update_model_label()
        
        self.model_dropdown.bind('<<ComboboxSelected>>', lambda e: self.update_model_label())
        
        tk.Frame(top, bg=COLORS['border'], width=1).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Checkboxes
        self.alpha_check = tk.Checkbutton(top, text=get_text('alpha_matting', self.lang),
                                         variable=app.alpha_matting,
                                         font=("Segoe UI", 9), bg=COLORS['card'], fg=COLORS['text'],
                                         selectcolor=COLORS['accent'], activebackground=COLORS['card'],
                                         cursor="hand2")
        self.alpha_check.pack(side=tk.LEFT, padx=5)
        
        self.crop_check = tk.Checkbutton(top, text=get_text('auto_crop', self.lang),
                                        variable=app.auto_crop,
                                        font=("Segoe UI", 9), bg=COLORS['card'], fg=COLORS['text'],
                                        selectcolor=COLORS['accent'], activebackground=COLORS['card'],
                                        cursor="hand2")
        self.crop_check.pack(side=tk.LEFT, padx=5)
        
        self.grid_check = tk.Checkbutton(top, text=get_text('transparency_grid', self.lang),
                                        variable=app.transparency_grid,
                                        font=("Segoe UI", 9), bg=COLORS['card'], fg=COLORS['text'],
                                        selectcolor=COLORS['accent'], activebackground=COLORS['card'],
                                        cursor="hand2")
        self.grid_check.pack(side=tk.LEFT, padx=5)
        
        tk.Frame(top, bg=COLORS['border'], width=1).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Edge Mode
        self._create_edge_controls(top)
        
        tk.Frame(top, bg=COLORS['border'], width=1).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Minimum Filter
        self._create_minimum_controls(top)
        
        # Language button (มุมขวา)
        right = tk.Frame(top, bg=COLORS['card'])
        right.pack(side=tk.RIGHT, padx=12, pady=8)
        
        lang_text = '🌐 EN' if self.lang == 'th' else '🌐 TH'
        self.lang_btn = ModernButton(right, text=lang_text, command=app.toggle_language,
                                    bg_color=COLORS['accent'], 
                                    hover_color=COLORS['accent_hover'],
                                    width=65, height=36)
        self.lang_btn.pack(side=tk.RIGHT)
    
    def _setup_combobox_style(self):
        """ตั้งค่า style สำหรับ Combobox"""
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Custom.TCombobox',
                       fieldbackground=COLORS['card'],
                       background=COLORS['accent'],
                       foreground=COLORS['text'],
                       arrowcolor=COLORS['text'],
                       borderwidth=1,
                       relief='solid')
        
        style.map('Custom.TCombobox',
                 fieldbackground=[('readonly', COLORS['card'])],
                 selectbackground=[('readonly', COLORS['accent'])],
                 selectforeground=[('readonly', '#ffffff')])
    
    def _create_edge_controls(self, parent):
        """สร้างส่วนควบคุม Edge Mode"""
        edge_frame = tk.Frame(parent, bg=COLORS['card'])
        edge_frame.pack(side=tk.LEFT, padx=5)
        
        self.edge_label = tk.Label(edge_frame, text=get_text('edge', self.lang),
                                   font=("Segoe UI", 9),
                                   bg=COLORS['card'], fg=COLORS['text'])
        self.edge_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.edge_dropdown = ttk.Combobox(
            edge_frame,
            textvariable=self.app.edge_mode,
            values=[get_edge_mode_text(k, self.lang) for k in EDGE_MODES.keys()],
            state='readonly',
            width=10,
            font=("Segoe UI", 9),
            style='Custom.TCombobox'
        )
        self.edge_dropdown.pack(side=tk.LEFT, padx=2)
        
        # สร้าง mapping จาก text กลับไปเป็น key
        self.edge_mode_keys = list(EDGE_MODES.keys())
        
        def on_edge_change(event):
            idx = self.edge_dropdown.current()
            if 0 <= idx < len(self.edge_mode_keys):
                self.app.edge_mode.set(self.edge_mode_keys[idx])
                if self.app.output_image:
                    import threading
                    threading.Thread(target=self.app.reapply_filters, daemon=True).start()
        
        self.edge_dropdown.bind('<<ComboboxSelected>>', on_edge_change)
    
    def _create_minimum_controls(self, parent):
        """สร้างส่วนควบคุม Minimum Filter"""
        min_frame = tk.Frame(parent, bg=COLORS['card'])
        min_frame.pack(side=tk.LEFT, padx=5)
        
        self.minimum_label_text = tk.Label(min_frame, text=get_text('minimum', self.lang),
                                          font=("Segoe UI", 9),
                                          bg=COLORS['card'], fg=COLORS['text'])
        self.minimum_label_text.pack(side=tk.LEFT, padx=(0, 5))
        
        self.minimum_scale = tk.Scale(min_frame, 
                                     from_=MINIMUM_FILTER_RANGE['min'], 
                                     to=MINIMUM_FILTER_RANGE['max'], 
                                     orient=tk.HORIZONTAL,
                                     variable=self.app.minimum_filter, length=120,
                                     bg=COLORS['card'], fg=COLORS['text'],
                                     highlightthickness=0, troughcolor=COLORS['bg'],
                                     activebackground=COLORS['accent'], cursor="hand2",
                                     command=self.app.on_minimum_change)
        self.minimum_scale.pack(side=tk.LEFT)
        
        self.minimum_value_label = tk.Label(min_frame, text="0 px", font=("Segoe UI", 8),
                                           bg=COLORS['card'], fg=COLORS['text_dim'], width=5)
        self.minimum_value_label.pack(side=tk.LEFT, padx=(5, 0))
    
    def update_model_label(self):
        """อัปเดต label แสดงชื่อ model"""
        from utils import get_model_display_name
        display_name = get_model_display_name(self.app.model_choice.get(), AI_MODELS)
        self.model_label.config(text=display_name)
    
    def refresh_texts(self, lang):
        """รีเฟรชข้อความทั้งหมดเป็นภาษาใหม่"""
        self.lang = lang
        self.settings_label.config(text=get_text('settings', lang))
        self.ai_model_label.config(text=get_text('ai_model', lang))
        self.alpha_check.config(text=get_text('alpha_matting', lang))
        self.crop_check.config(text=get_text('auto_crop', lang))
        self.grid_check.config(text=get_text('transparency_grid', lang))
        self.edge_label.config(text=get_text('edge', lang))
        self.minimum_label_text.config(text=get_text('minimum', lang))
        
        # อัปเดต edge dropdown
        translated_values = [get_edge_mode_text(k, lang) for k in EDGE_MODES.keys()]
        self.edge_dropdown['values'] = translated_values
        current_key = self.app.edge_mode.get()
        for i, key in enumerate(EDGE_MODES.keys()):
            if key == current_key:
                self.edge_dropdown.current(i)
                break
        
        # อัปเดต language button
        new_lang_text = '🌐 EN' if lang == 'th' else '🌐 TH'
        self.lang_btn.update_text(new_lang_text)


class BottomBar:
    """แถบด้านล่าง (Control bar)"""
    
    def __init__(self, parent, app):
        """
        สร้าง Bottom Bar
        
        Args:
            parent: parent widget
            app: BackgroundRemoverApp instance
        """
        self.app = app
        self.lang = app.current_lang
        
        bottom = tk.Frame(app.root, bg=COLORS['card'], height=60)
        bottom.grid(row=2, column=0, sticky='ews')
        bottom.grid_propagate(False)
        
        # Progress bar (ซ้าย)
        self._create_progress_bar(bottom)
        
        # Status bar (กลาง - ขยายเต็ม)
        self.status_bar = StatusBar(bottom, COLORS['card'], COLORS['text'])
        self.status_bar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        # Control buttons (ขวาสุด)
        self._create_control_buttons(bottom)
    
    def _create_progress_bar(self, parent):
        """สร้าง Progress bar"""
        prog_container = tk.Frame(parent, bg=COLORS['card'])
        prog_container.pack(side=tk.LEFT, padx=15, pady=0)
        
        self.progress = ttk.Progressbar(prog_container, mode='determinate', 
                                       length=PROGRESS_BAR['length'],
                                       style="Custom.Horizontal.TProgressbar")
        self.progress.pack(pady=18)
        
        style = ttk.Style()
        style.configure("Custom.Horizontal.TProgressbar", 
                       troughcolor=COLORS['bg'],
                       background=COLORS['accent'], 
                       borderwidth=0, thickness=3)
    
    def _create_control_buttons(self, parent):
        """สร้างปุ่มควบคุม"""
        right = tk.Frame(parent, bg=COLORS['card'])
        right.pack(side=tk.RIGHT, padx=12, pady=8)

        # ปรับแสง/สี
        self._create_adjust_controls(right)
 
        # Transform tools
        self._create_transform_buttons(right)
                   
        # เส้นแบ่ง
        tk.Frame(right, bg=COLORS['border'], width=1, height=30).pack(side=tk.LEFT, padx=8)
        
        # ปุ่มหลัก
        self.select_btn = ModernButton(right, text=get_text('select_image', self.lang),
                                       command=self.app.select_image,
                                       bg_color=COLORS['accent'], 
                                       hover_color=COLORS['accent_hover'],
                                       width=85, height=36)
        self.select_btn.pack(side=tk.LEFT, padx=2)
        
        self.remove_btn = ModernButton(right, text=get_text('remove_bg', self.lang), 
                                       command=self.app.remove_background,
                                       bg_color=COLORS['warning'], 
                                       hover_color=COLORS['warning_hover'],
                                       width=105, height=36)
        self.remove_btn.pack(side=tk.LEFT, padx=2)
        self.remove_btn.set_enabled(False)
        
        self.save_btn = ModernButton(right, text=get_text('save', self.lang),
                                     command=self.app.save_image,
                                     bg_color=COLORS['success'], 
                                     hover_color=COLORS['success_hover'],
                                     width=85, height=36)
        self.save_btn.pack(side=tk.LEFT, padx=2)
        self.save_btn.set_enabled(False)
    
    def _create_adjust_controls(self, parent):
        """สร้างส่วนปรับแสง/สี"""
        adj_frame = tk.Frame(parent, bg=COLORS['card'])
        adj_frame.pack(side=tk.LEFT, padx=(10, 10), pady=5)

        tk.Label(adj_frame, text=get_text('adjust_label', self.lang), font=("Segoe UI", 11, "bold"),
                bg=COLORS['card'], fg=COLORS['text']).pack(side=tk.LEFT, padx=(0, 5))

        def make_compact_slider(parent, label, var):
            frame = tk.Frame(parent, bg=COLORS['card'])
            frame.pack(side=tk.LEFT, padx=(5, 0))
            
            tk.Label(frame, text=label, font=("Segoe UI", 9, "bold"),
                    bg=COLORS['card'], fg=COLORS['text_dim']).pack(side=tk.LEFT)
            
            tk.Scale(
                frame,
                from_=0.2, to=2.0, resolution=0.1, orient=tk.HORIZONTAL,
                variable=var, length=120, showvalue=False,
                sliderlength=10, troughcolor=COLORS['bg'],
                bg=COLORS['card'], fg=COLORS['text'],
                highlightthickness=0,
                activebackground=COLORS['accent'],
                command=lambda v: self.app.apply_global_adjust()
            ).pack(side=tk.LEFT)

        make_compact_slider(adj_frame, get_text('brightness', self.lang), self.app.brightness_var)
        make_compact_slider(adj_frame, get_text('contrast', self.lang), self.app.contrast_var)
        make_compact_slider(adj_frame, get_text('saturation', self.lang), self.app.saturation_var)

        tk.Button(
            adj_frame, text="↺", command=self.app.reset_adjust,
            font=("Segoe UI", 10, "bold"),
            bg=COLORS['card'], fg=COLORS['text'],
            cursor="hand2", relief=tk.FLAT, width=2
        ).pack(side=tk.LEFT, padx=(6, 0))
    
    def _create_transform_buttons(self, parent):
        """สร้างปุ่ม Transform"""
        tf = tk.Frame(parent, bg=COLORS['card'])
        tf.pack(side=tk.LEFT, padx=(0, 15))
        
        for txt, cmd in [("↻", self.app.rotate_image), ("↔", self.app.flip_horizontal), 
                         ("↕", self.app.flip_vertical)]:
            tk.Button(tf, text=txt, command=cmd, font=("Segoe UI", 16),
                     bg=COLORS['card'], fg=COLORS['text'], cursor="hand2",
                     relief=tk.FLAT, width=2, height=1).pack(side=tk.LEFT, padx=2)
    
    def refresh_texts(self, lang):
        """รีเฟรชข้อความทั้งหมดเป็นภาษาใหม่"""
        self.lang = lang
        self.select_btn.update_text(get_text('select_image', lang))
        self.remove_btn.update_text(get_text('remove_bg', lang))
        self.save_btn.update_text(get_text('save', lang))