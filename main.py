"""
โปรแกรมลบพื้นหลังรูปภาพ v12.2 - Multi-language (Simplified)
รวมทุก module ไว้ในไฟล์เดียว เพื่อความเรียบง่าย

ใช้ไฟล์นี้แทน main.py ถ้าเวอร์ชัน modular มีปัญหา
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk, ImageOps, ImageEnhance
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
from pathlib import Path

# Import จาก modules ที่มีอยู่
from config import *
from utils import *
from models import AIModelManager
from widgets import CircularProgress


# ==================== Custom Widgets ====================
class ModernButton(tk.Frame):
    """ปุ่มสไตล์ Modern"""
    def __init__(self, parent, text, command, bg_color, hover_color, width=100, height=40):
        super().__init__(parent, bg=parent['bg'])
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.command = command
        self.is_enabled = True
        
        self.button = tk.Button(self, text=text, command=self._on_click,
            bg=bg_color, fg='#ffffff', font=('Segoe UI', 10, 'bold'),
            relief=tk.FLAT, cursor='hand2', padx=10, pady=5)
        self.button.pack()
        self.button.bind('<Enter>', self._on_enter)
        self.button.bind('<Leave>', self._on_leave)
    
    def _on_click(self):
        if self.is_enabled and self.command:
            self.command()
    
    def _on_enter(self, e):
        if self.is_enabled:
            self.button.config(bg=self.hover_color)
    
    def _on_leave(self, e):
        if self.is_enabled:
            self.button.config(bg=self.bg_color)
        else:
            self.button.config(bg='#4b5563')
    
    def set_enabled(self, enabled):
        self.is_enabled = enabled
        if enabled:
            self.button.config(bg=self.bg_color, cursor='hand2')
        else:
            self.button.config(bg='#4b5563', cursor='arrow')
    
    def update_text(self, new_text):
        self.button.config(text=new_text)


# ==================== Main Application ====================
class BackgroundRemoverApp:
    """แอปพลิเคชันลบพื้นหลัง - รองรับ Multi-language"""
    
    def __init__(self, root):
        self.root = root
        self.current_lang = DEFAULT_LANGUAGE
        
        self.root.title(get_text('window_title', self.current_lang))
        self.root.state(WINDOW_CONFIG['state'])
        self.root.configure(bg=COLORS['bg'])
        
        # ตัวแปร
        self.input_image = None
        self.output_image = None
        self.original_output_image = None
        self.cropped_output_image = None
        self.input_path = None
        
        self.model_choice = tk.StringVar(value=DEFAULT_SETTINGS['model'])
        self.alpha_matting = tk.BooleanVar(value=DEFAULT_SETTINGS['alpha_matting'])
        self.auto_crop = tk.BooleanVar(value=DEFAULT_SETTINGS['auto_crop'])
        self.transparency_grid = tk.BooleanVar(value=DEFAULT_SETTINGS['transparency_grid'])
        self.minimum_filter = tk.IntVar(value=MODEL_MINIMUM_DEFAULTS.get(DEFAULT_SETTINGS['model'], 0))
        self.edge_mode = tk.StringVar(value=DEFAULT_SETTINGS['edge_mode'])
        
        self.zoom_level = ZOOM_SETTINGS['default']
        self.input_zoom_level = ZOOM_SETTINGS['default']
        
        self.brightness_var = tk.DoubleVar(value=1.0)
        self.contrast_var = tk.DoubleVar(value=1.0)
        self.saturation_var = tk.DoubleVar(value=1.0)
        
        # AI Model Manager
        self.model_manager = AIModelManager(
            root=self.root,
            status_callback=self.update_status,
            on_ready_callback=lambda: None,
            on_error_callback=lambda msg: messagebox.showerror(get_text('error', self.current_lang), msg),
            lang=self.current_lang
        )
        
        # สร้าง UI
        self.setup_ui()
    
    def setup_ui(self):
        """สร้าง UI"""
        self.root.grid_rowconfigure(0, weight=0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=0)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.create_top_bar()
        self.create_tabs()
        self.create_bottom_bar()
        
        self.model_choice.trace_add('write', lambda *a: self.on_model_changed())
        self.auto_crop.trace_add('write', lambda *a: self.update_info())
        self.transparency_grid.trace_add('write', lambda *a: self.refresh_output_display())
    
    def create_top_bar(self):
        """สร้างแถบด้านบน"""
        lang = self.current_lang
        
        top = tk.Frame(self.root, bg=COLORS['card'], height=70)
        top.grid(row=0, column=0, sticky='ew')
        top.grid_propagate(False)
        
        left = tk.Frame(top, bg=COLORS['card'])
        left.pack(side=tk.LEFT, padx=15, pady=12)
        
        self.settings_label = tk.Label(left, text=get_text('settings', lang),
                                       font=("Segoe UI", 11, "bold"),
                                       bg=COLORS['card'], fg=COLORS['text'])
        self.settings_label.pack(side=tk.LEFT, padx=(0, 15))
        
        self.ai_model_label = tk.Label(left, text=get_text('ai_model', lang),
                                       font=("Segoe UI", 9),
                                       bg=COLORS['card'], fg=COLORS['text'])
        self.ai_model_label.pack(side=tk.LEFT, padx=(0, 5))
        
        # Style for Combobox
        style = ttk.Style()
        style.theme_use('default')
        
        # Configure Combobox style
        style.configure('Custom.TCombobox',
                       fieldbackground=COLORS['card'],
                       background=COLORS['card'],
                       foreground=COLORS['text'],
                       arrowcolor=COLORS['text'],
                       bordercolor=COLORS['border'],
                       lightcolor=COLORS['card'],
                       darkcolor=COLORS['card'],
                       borderwidth=1,
                       relief='solid')
        
        # Configure dropdown list style
        style.map('Custom.TCombobox',
                 fieldbackground=[('readonly', COLORS['card'])],
                 selectbackground=[('readonly', COLORS['accent'])],
                 selectforeground=[('readonly', '#ffffff')],
                 foreground=[('readonly', COLORS['text'])],
                 background=[('readonly', COLORS['card'])])
        
        # Configure the dropdown list window
        self.root.option_add('*TCombobox*Listbox.background', COLORS['card'])
        self.root.option_add('*TCombobox*Listbox.foreground', COLORS['text'])
        self.root.option_add('*TCombobox*Listbox.selectBackground', COLORS['accent'])
        self.root.option_add('*TCombobox*Listbox.selectForeground', '#ffffff')
        
        # Model Dropdown
        self.model_dropdown = ttk.Combobox(left, textvariable=self.model_choice,
            values=list(AI_MODELS.keys()), state='readonly', width=32,
            font=("Segoe UI", 9), style='Custom.TCombobox')
        self.model_dropdown.pack(side=tk.LEFT, padx=5)
        
        self.model_label = tk.Label(left, text="", font=("Segoe UI", 8),
                                    bg=COLORS['card'], fg=COLORS['text_dim'])
        self.model_label.pack(side=tk.LEFT, padx=(5, 10))
        self.update_model_label()
        self.model_dropdown.bind('<<ComboboxSelected>>', lambda e: self.update_model_label())
        
        tk.Frame(top, bg=COLORS['border'], width=1).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Checkboxes
        self.alpha_check = tk.Checkbutton(top, text=get_text('alpha_matting', lang),
                                         variable=self.alpha_matting,
                                         font=("Segoe UI", 9), bg=COLORS['card'], fg=COLORS['text'],
                                         selectcolor=COLORS['accent'], activebackground=COLORS['card'],
                                         cursor="hand2")
        self.alpha_check.pack(side=tk.LEFT, padx=5)
        
        self.crop_check = tk.Checkbutton(top, text=get_text('auto_crop', lang),
                                        variable=self.auto_crop,
                                        font=("Segoe UI", 9), bg=COLORS['card'], fg=COLORS['text'],
                                        selectcolor=COLORS['accent'], activebackground=COLORS['card'],
                                        cursor="hand2")
        self.crop_check.pack(side=tk.LEFT, padx=5)
        
        self.grid_check = tk.Checkbutton(top, text=get_text('transparency_grid', lang),
                                        variable=self.transparency_grid,
                                        font=("Segoe UI", 9), bg=COLORS['card'], fg=COLORS['text'],
                                        selectcolor=COLORS['accent'], activebackground=COLORS['card'],
                                        cursor="hand2")
        self.grid_check.pack(side=tk.LEFT, padx=5)
        
        tk.Frame(top, bg=COLORS['border'], width=1).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Edge Mode
        edge_frame = tk.Frame(top, bg=COLORS['card'])
        edge_frame.pack(side=tk.LEFT, padx=5)
        
        self.edge_label = tk.Label(edge_frame, text=get_text('edge', lang),
                                   font=("Segoe UI", 9),
                                   bg=COLORS['card'], fg=COLORS['text'])
        self.edge_label.pack(side=tk.LEFT, padx=(0, 5))
        
        self.edge_dropdown = ttk.Combobox(
            edge_frame,
            textvariable=self.edge_mode,
            values=[get_edge_mode_text(k, lang) for k in EDGE_MODES.keys()],
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
                self.edge_mode.set(self.edge_mode_keys[idx])
                if self.output_image:
                    import threading
                    threading.Thread(target=self.reapply_filters, daemon=True).start()
        
        self.edge_dropdown.bind('<<ComboboxSelected>>', on_edge_change)
        
        tk.Frame(top, bg=COLORS['border'], width=1).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Minimum Filter
        min_frame = tk.Frame(top, bg=COLORS['card'])
        min_frame.pack(side=tk.LEFT, padx=5)
        
        self.minimum_label_text = tk.Label(min_frame, text=get_text('minimum', lang),
                                          font=("Segoe UI", 9),
                                          bg=COLORS['card'], fg=COLORS['text'])
        self.minimum_label_text.pack(side=tk.LEFT, padx=(0, 5))
        
        self.minimum_scale = tk.Scale(min_frame, 
                                     from_=MINIMUM_FILTER_RANGE['min'], 
                                     to=MINIMUM_FILTER_RANGE['max'], 
                                     orient=tk.HORIZONTAL,
                                     variable=self.minimum_filter, length=120,
                                     bg=COLORS['card'], fg=COLORS['text'],
                                     highlightthickness=0, troughcolor=COLORS['bg'],
                                     activebackground=COLORS['accent'], cursor="hand2",
                                     command=self.on_minimum_change)
        self.minimum_scale.pack(side=tk.LEFT)
        
        self.minimum_value_label = tk.Label(min_frame, text="2 px", font=("Segoe UI", 8),
                                           bg=COLORS['card'], fg=COLORS['text_dim'], width=5)
        self.minimum_value_label.pack(side=tk.LEFT, padx=(5, 0))
        
        # Language button
        right = tk.Frame(top, bg=COLORS['card'])
        right.pack(side=tk.RIGHT, padx=12, pady=8)
        
        lang_text = '🌐 EN' if lang == 'th' else '🌐 TH'
        self.lang_btn = ModernButton(right, text=lang_text, command=self.toggle_language,
                                    bg_color=COLORS['accent'], 
                                    hover_color=COLORS['accent_hover'],
                                    width=65, height=36)
        self.lang_btn.pack(side=tk.RIGHT)
    
    def create_tabs(self):
        """สร้าง Tabs (ใช้โค้ดเดิมจาก v12.1 ที่ทำงานได้ดี)"""
        lang = self.current_lang
        
        main = tk.Frame(self.root, bg=COLORS['bg'])
        main.grid(row=1, column=0, sticky='nsew', padx=15, pady=5)
        
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
        
        # Tab 1: ต้นฉบับ
        tab1 = tk.Frame(self.notebook, bg=COLORS['bg'])
        self.notebook.add(tab1, text=get_text('tab_original', lang))
        
        card1 = tk.Frame(tab1, bg=COLORS['card'])
        card1.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.input_tab_header = tk.Label(card1, text=get_text('original_image', lang),
                                         font=("Segoe UI", 13, "bold"),
                                         bg=COLORS['card'], fg=COLORS['text'], pady=12)
        self.input_tab_header.pack()
        
        self.input_label = tk.Label(card1, text=get_text('no_image_selected', lang),
                                    bg='#1e1e1e', fg=COLORS['text_dim'], font=("Segoe UI", 11))
        self.input_label.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))
        
        # Tab 2: ผลลัพธ์
        tab2 = tk.Frame(self.notebook, bg=COLORS['bg'])
        self.notebook.add(tab2, text=get_text('tab_result', lang))
        
        card2 = tk.Frame(tab2, bg=COLORS['card'])
        card2.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.output_tab_header = tk.Label(card2, text=get_text('result_image', lang),
                                          font=("Segoe UI", 13, "bold"),
                                          bg=COLORS['card'], fg=COLORS['text'], pady=12)
        self.output_tab_header.pack()
        
        self.output_label = tk.Label(card2, text=get_text('waiting_result', lang),
                                     bg='#1e1e1e', fg=COLORS['text_dim'], font=("Segoe UI", 11))
        self.output_label.pack(fill=tk.BOTH, expand=True, padx=12, pady=(0, 12))
        
        # Tab 3: เปรียบเทียบ
        tab3 = tk.Frame(self.notebook, bg=COLORS['bg'])
        self.notebook.add(tab3, text=get_text('tab_compare', lang))
        
        compare_frame = tk.Frame(tab3, bg=COLORS['bg'])
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
    
    def create_bottom_bar(self):
        """สร้างแถบด้านล่าง - ใช้ Circular Progress"""
        lang = self.current_lang
        
        bottom = tk.Frame(self.root, bg=COLORS['card'], height=60)
        bottom.grid(row=2, column=0, sticky='ews')
        bottom.grid_propagate(False)
        
        # Circular Progress Bar (ประหยัดพื้นที่)
        prog_container = tk.Frame(bottom, bg=COLORS['card'])
        prog_container.pack(side=tk.LEFT, padx=15, pady=5)
        
        self.progress = CircularProgress(
            prog_container, 
            size=50,
            width=4,
            bg_color=COLORS['card'],
            fg_color=COLORS['accent'],
            text_color=COLORS['text']
        )
        self.progress.pack()
        
        # Status
        status_frame = tk.Frame(bottom, bg=COLORS['card'])
        status_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.status_label = tk.Label(status_frame, text=get_text('select_image', lang),
                                     font=('Segoe UI', 8),
                                     bg=COLORS['card'], fg='#9ca3af', anchor=tk.W)
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
        
        tk.Frame(status_frame, bg='#2d3748', width=1).pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        self.info_label = tk.Label(status_frame, text="JPG, PNG, BMP → PNG",
                                   font=('Segoe UI', 7),
                                   bg=COLORS['card'], fg='#6b7280')
        self.info_label.pack(side=tk.LEFT, padx=8)
        
        # Buttons
        right = tk.Frame(bottom, bg=COLORS['card'])
        right.pack(side=tk.RIGHT, padx=12, pady=8)
        
        # ปรับแสง/สี
        adj_frame = tk.Frame(right, bg=COLORS['card'])
        adj_frame.pack(side=tk.LEFT, padx=(10, 10), pady=5)

        tk.Label(adj_frame, text=get_text('adjust_label', lang), font=("Segoe UI", 11, "bold"),
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
                command=lambda v: self.apply_global_adjust()
            ).pack(side=tk.LEFT)

        make_compact_slider(adj_frame, get_text('brightness', lang), self.brightness_var)
        make_compact_slider(adj_frame, get_text('contrast', lang), self.contrast_var)
        make_compact_slider(adj_frame, get_text('saturation', lang), self.saturation_var)

        tk.Button(
            adj_frame, text="↺", command=self.reset_adjust,
            font=("Segoe UI", 10, "bold"),
            bg=COLORS['card'], fg=COLORS['text'],
            cursor="hand2", relief=tk.FLAT, width=2
        ).pack(side=tk.LEFT, padx=(6, 0))
 
        # Transform tools
        tf = tk.Frame(right, bg=COLORS['card'])
        tf.pack(side=tk.LEFT, padx=(0, 15))
        
        for txt, cmd in [("↻", self.rotate_image), ("↔", self.flip_horizontal), 
                         ("↕", self.flip_vertical)]:
            tk.Button(tf, text=txt, command=cmd, font=("Segoe UI", 16),
                     bg=COLORS['card'], fg=COLORS['text'], cursor="hand2",
                     relief=tk.FLAT, width=2, height=1).pack(side=tk.LEFT, padx=2)
        
        # เส้นแบ่ง
        tk.Frame(right, bg=COLORS['border'], width=1, height=30).pack(side=tk.LEFT, padx=8)
        
        self.select_btn = ModernButton(right, text=get_text('select_image', lang),
                                       command=self.select_image,
                                       bg_color=COLORS['accent'], 
                                       hover_color=COLORS['accent_hover'],
                                       width=85, height=36)
        self.select_btn.pack(side=tk.LEFT, padx=2)
        
        self.remove_btn = ModernButton(right, text=get_text('remove_bg', lang), 
                                       command=self.remove_background,
                                       bg_color=COLORS['warning'], 
                                       hover_color=COLORS['warning_hover'],
                                       width=105, height=36)
        self.remove_btn.pack(side=tk.LEFT, padx=2)
        self.remove_btn.set_enabled(False)
        
        self.save_btn = ModernButton(right, text=get_text('save', lang),
                                     command=self.save_image,
                                     bg_color=COLORS['success'], 
                                     hover_color=COLORS['success_hover'],
                                     width=85, height=36)
        self.save_btn.pack(side=tk.LEFT, padx=2)
        self.save_btn.set_enabled(False)
    
    # ==================== Language Management ====================
    
    def toggle_language(self):
        """สลับภาษา"""
        self.current_lang = 'en' if self.current_lang == 'th' else 'th'
        self.root.title(get_text('window_title', self.current_lang))
        self.refresh_ui_texts()
        msg = get_text('language_changed', self.current_lang)
        self.update_status(msg, COLORS['success'])
        self.model_manager.lang = self.current_lang
    
    def refresh_ui_texts(self):
        """รีเฟรช UI texts"""
        lang = self.current_lang
        
        # Top bar
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
        current_key = self.edge_mode.get()
        for i, key in enumerate(EDGE_MODES.keys()):
            if key == current_key:
                self.edge_dropdown.current(i)
                break
        
        # Tabs
        self.notebook.tab(0, text=get_text('tab_original', lang))
        self.notebook.tab(1, text=get_text('tab_result', lang))
        self.notebook.tab(2, text=get_text('tab_compare', lang))
        
        self.input_tab_header.config(text=get_text('original_image', lang))
        self.output_tab_header.config(text=get_text('result_image', lang))
        self.compare_before_label.config(text=get_text('before', lang))
        self.compare_after_label.config(text=get_text('after', lang))
        
        # Buttons
        self.select_btn.update_text(get_text('select_image', lang))
        self.remove_btn.update_text(get_text('remove_bg', lang))
        self.save_btn.update_text(get_text('save', lang))
        
        new_lang_text = '🌐 EN' if lang == 'th' else '🌐 TH'
        self.lang_btn.update_text(new_lang_text)
        
        # Placeholders
        if not self.input_image:
            self.input_label.config(text=get_text('no_image_selected', lang))
        if not self.output_image:
            self.output_label.config(text=get_text('waiting_result', lang))
    
    #==================== Helper Methods ====================
    
    def update_model_label(self):
        display_name = get_model_display_name(self.model_choice.get(), AI_MODELS)
        self.model_label.config(text=display_name)
    
    def on_model_changed(self):
        new_model = self.model_choice.get()
        
        def on_switch_complete():
            recommended = self.model_manager.get_recommended_minimum()
            self.minimum_filter.set(recommended)
            self.minimum_value_label.config(text=f"{recommended} px")
        
        self.model_manager.switch_model(new_model, on_complete=on_switch_complete)
    
    def update_status(self, text, color="#9ca3af"):
        self.status_label.config(text=text, fg=color)
    
    def update_info(self):
        info_text = "JPG, PNG, BMP → PNG"
        if self.auto_crop.get():
            info_text += "  • ✂️ Crop"
        if self.transparency_grid.get():
            info_text += "  • 🔲 Grid"
        self.info_label.config(text=info_text)
    
    def on_minimum_change(self, value):
        value = int(float(value))
        self.minimum_value_label.config(text=f"{value} px")
        if self.output_image and self.input_image:
            msg = get_text('minimum_applying', self.current_lang).format(value)
            self.update_status(msg, COLORS['warning'])
            import threading
            threading.Thread(target=self.reapply_filters, daemon=True).start()
    
    def refresh_output_display(self):
        if self.output_image:
            self.display_output_image()
            self.update_compare()
    
    def reapply_filters(self):
        try:
            if not self.original_output_image:
                return
            
            processed_image = self.original_output_image.copy()
            
            min_value = self.minimum_filter.get()
            if min_value > 0:
                processed_image = apply_minimum_filter(processed_image, iterations=min_value)
            
            if self.auto_crop.get():
                processed_image = crop_transparent(processed_image)
            
            self.output_image = processed_image
            self.cropped_output_image = self.output_image.copy()
            
            self.root.after(0, lambda: self.display_output_image())
            self.root.after(0, lambda: self.update_compare())
            
            msg = get_text('minimum_applied', self.current_lang).format(min_value)
            self.root.after(0, lambda: self.update_status(msg, COLORS['success']))
            
        except Exception as e:
            print(f"Reapply filters error: {e}")
    
    def apply_global_adjust(self):
        """อัปเดตภาพเมื่อปรับ Brightness / Contrast / Saturation"""
        if not hasattr(self, "cropped_output_image") or self.cropped_output_image is None:
            return

        base_img = self.cropped_output_image.copy()

        bright = self.brightness_var.get()
        contrast = self.contrast_var.get()
        satur = self.saturation_var.get()

        img = ImageEnhance.Brightness(base_img).enhance(bright)
        img = ImageEnhance.Contrast(img).enhance(contrast)
        img = ImageEnhance.Color(img).enhance(satur)

        self.output_image = img
        self.display_output_image()
        self.update_compare()

        msg = get_text('adjust_applied', self.current_lang).format(bright, contrast, satur)
        self.update_status(msg, COLORS['success'])

    def reset_adjust(self):
        """รีเซ็ตค่าการปรับแสงโดยไม่กระทบการ Crop"""
        self.brightness_var.set(1.0)
        self.contrast_var.set(1.0)
        self.saturation_var.set(1.0)

        if hasattr(self, "cropped_output_image") and self.cropped_output_image is not None:
            self.output_image = self.cropped_output_image.copy()
            self.display_output_image()
            self.update_compare()

        msg = get_text('adjust_reset', self.current_lang)
        self.update_status(msg, COLORS['success'])
    
    def rotate_image(self):
        """หมุนภาพ 90 องศา"""
        if self.output_image:
            self.output_image = self.output_image.rotate(-90, expand=True)
            if hasattr(self, "cropped_output_image") and self.cropped_output_image:
                self.cropped_output_image = self.cropped_output_image.rotate(-90, expand=True)
            self.display_output_image()
            self.update_compare()
            msg = get_text('rotate', self.current_lang)
            self.update_status(msg, COLORS['success'])
        elif self.input_image:
            self.input_image = self.input_image.rotate(-90, expand=True)
            self.display_input_image()
            self.update_compare()
            msg = get_text('rotate', self.current_lang)
            self.update_status(msg, COLORS['success'])
    
    def flip_horizontal(self):
        """พลิกภาพซ้าย-ขวา"""
        if self.output_image:
            self.output_image = ImageOps.mirror(self.output_image)
            if hasattr(self, "cropped_output_image") and self.cropped_output_image:
                self.cropped_output_image = ImageOps.mirror(self.cropped_output_image)
            self.display_output_image()
            self.update_compare()
            msg = get_text('flip_h', self.current_lang)
            self.update_status(msg, COLORS['success'])
        elif self.input_image:
            self.input_image = ImageOps.mirror(self.input_image)
            self.display_input_image()
            self.update_compare()
            msg = get_text('flip_h', self.current_lang)
            self.update_status(msg, COLORS['success'])
    
    def flip_vertical(self):
        """พลิกภาพบน-ล่าง"""
        if self.output_image:
            self.output_image = ImageOps.flip(self.output_image)
            if hasattr(self, "cropped_output_image") and self.cropped_output_image:
                self.cropped_output_image = ImageOps.flip(self.cropped_output_image)
            self.display_output_image()
            self.update_compare()
            msg = get_text('flip_v', self.current_lang)
            self.update_status(msg, COLORS['success'])
        elif self.input_image:
            self.input_image = ImageOps.flip(self.input_image)
            self.display_input_image()
            self.update_compare()
            msg = get_text('flip_v', self.current_lang)
            self.update_status(msg, COLORS['success'])
    
    def display_input_image(self):
        if not self.input_image:
            return
        
        lw = self.input_label.winfo_width()
        lh = self.input_label.winfo_height()
        
        if lw <= 1:
            lw = 800
        if lh <= 1:
            lh = 600
        
        img = self.input_image.copy()
        scale = calculate_fit_to_screen_scale(img.width, img.height, lw, lh, 0.95)
        
        new_width = int(img.width * scale)
        new_height = int(img.height * scale)
        
        if new_width > 0 and new_height > 0:
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        photo = ImageTk.PhotoImage(img)
        self.input_label.config(image=photo, text='')
        self.input_label.image = photo
    
    def display_output_image(self):
        if not self.output_image:
            return
        
        lw = self.output_label.winfo_width()
        lh = self.output_label.winfo_height()
        
        if lw <= 1:
            lw = 800
        if lh <= 1:
            lh = 600
        
        img = self.output_image.copy()
        scale = calculate_fit_to_screen_scale(img.width, img.height, lw, lh, 0.95)
        
        new_width = int(img.width * scale)
        new_height = int(img.height * scale)
        
        if new_width > 0 and new_height > 0:
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        if self.transparency_grid.get() and img.mode == 'RGBA':
            grid = create_transparency_grid(new_width, new_height)
            grid.paste(img, (0, 0), img)
            img = grid
        
        photo = ImageTk.PhotoImage(img)
        self.output_label.config(image=photo, text='')
        self.output_label.image = photo
    
    def update_compare(self):
        self.root.after(50, self._update_compare_images)
    
    def _update_compare_images(self):
        if self.input_image:
            cw = self.compare_input_label.winfo_width()
            ch = self.compare_input_label.winfo_height()
            
            if cw <= 1:
                cw = 700
            if ch <= 1:
                ch = 800
            
            img = self.input_image.copy()
            scale = calculate_fit_to_screen_scale(img.width, img.height, cw, ch, 0.98)
            
            new_width = int(img.width * scale)
            new_height = int(img.height * scale)
            
            if new_width > 0 and new_height > 0:
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            photo = ImageTk.PhotoImage(img)
            self.compare_input_label.config(image=photo, text='')
            self.compare_input_label.image = photo
        
        if self.output_image:
            cw = self.compare_output_label.winfo_width()
            ch = self.compare_output_label.winfo_height()
            
            if cw <= 1:
                cw = 700
            if ch <= 1:
                ch = 800
            
            img = self.output_image.copy()
            scale = calculate_fit_to_screen_scale(img.width, img.height, cw, ch, 0.98)
            
            new_width = int(img.width * scale)
            new_height = int(img.height * scale)
            
            if new_width > 0 and new_height > 0:
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            if self.transparency_grid.get() and img.mode == 'RGBA':
                grid = create_transparency_grid(new_width, new_height)
                grid.paste(img, (0, 0), img)
                img = grid
            
            photo = ImageTk.PhotoImage(img)
            self.compare_output_label.config(image=photo, text='')
            self.compare_output_label.image = photo
    
    # ==================== Main Actions ====================
    
    def select_image(self):
        lang = self.current_lang
        title = get_text('select_image_title', lang)
        
        file_path = filedialog.askopenfilename(
            title=title,
            filetypes=FILE_DIALOG_TYPES
        )
        
        if file_path:
            try:
                self.input_path = file_path
                self.input_image = Image.open(file_path)
                
                self.root.after(100, lambda: self.display_input_image())
                self.root.after(150, self.update_compare)
                
                self.remove_btn.set_enabled(True)
                
                filename = os.path.basename(file_path)
                msg = get_text('image_loaded', lang).format(filename)
                self.update_status(msg, COLORS['success'])
                
                # Reset output
                self.output_image = None
                self.output_label.config(image='', text=get_text('waiting_result', lang))
                self.compare_output_label.config(image='', text='')
                self.save_btn.set_enabled(False)
                self.original_output_image = None
                
            except Exception as e:
                error_msg = str(e)
                title = get_text('error', lang)
                msg = get_text('load_image_failed', lang).format(error_msg)
                messagebox.showerror(title, msg)

    def remove_background(self):
        lang = self.current_lang
        
        if not self.input_image:
            title = get_text('warning', lang)
            msg = get_text('no_image', lang)
            messagebox.showwarning(title, msg)
            return
        
        if not self.model_manager.is_ready():
            title = get_text('warning', lang)
            messagebox.showwarning(title, "AI Model is not ready yet")
            return
        
        self.remove_btn.set_enabled(False)
        self.progress.reset()
        
        def on_progress(percentage):
            self.progress.set_progress(percentage)
        
        def on_complete(output_img):
            self.output_image = output_img
            self.original_output_image = self.output_image.copy()
            
            min_value = self.minimum_filter.get()
            if min_value > 0:
                self.output_image = apply_minimum_filter(self.output_image, iterations=min_value)
            
            if self.auto_crop.get():
                self.output_image = crop_transparent(self.output_image)
            
            self.cropped_output_image = self.output_image.copy()
            self.original_output_image = self.output_image.copy()

            self.display_output_image()
            self.update_compare()
            
            self.save_btn.set_enabled(True)
            self.remove_btn.set_enabled(True)
            
            self.notebook.select(2)
        
        def on_error(error_msg):
            self.progress.reset()
            self.remove_btn.set_enabled(True)
            title = get_text('error', lang)
            messagebox.showerror(title, error_msg)
        
        self.model_manager.remove_background(
            input_image=self.input_image,
            alpha_matting=self.alpha_matting.get(),
            on_progress=on_progress,
            on_complete=on_complete,
            on_error=on_error
        )
    
    def save_image(self):
        lang = self.current_lang
        
        if not self.output_image:
            title = get_text('warning', lang)
            msg = get_text('no_output', lang)
            messagebox.showwarning(title, msg)
            return
        
        if self.input_path:
            input_name = Path(self.input_path).stem
            default_name = f"{input_name}_no_bg.png"
        else:
            default_name = "output_no_bg.png"
        
        title = get_text('save_image_title', lang)
        file_path = filedialog.asksaveasfilename(
            title=title,
            defaultextension=SUPPORTED_FORMATS['output'],
            initialfile=default_name,
            filetypes=[
                ("PNG files", "*.png"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                self.output_image.save(file_path)
                
                title = get_text('success', lang)
                msg = get_text('save_success', lang).format(file_path)
                messagebox.showinfo(title, msg)
                
                filename = os.path.basename(file_path)
                status_msg = get_text('file_saved', lang).format(filename)
                self.update_status(status_msg, COLORS['success'])
                
            except Exception as e:
                error_msg = str(e)
                title = get_text('error', lang)
                msg = get_text('save_image_failed', lang).format(error_msg)
                messagebox.showerror(title, msg)


# ==================== Main Entry Point ====================

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()