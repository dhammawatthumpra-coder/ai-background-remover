"""
Custom UI Widgets Module - Background Remover v12.2
Custom components สำหรับ UI (รองรับ Multi-language)
"""

import tkinter as tk
from tkinter import ttk
import math


class ModernButton(tk.Frame):
    """ปุ่มสไตล์ Modern พร้อม Hover Effect และการเปลี่ยนข้อความ"""
    
    def __init__(self, parent, text, command, bg_color, hover_color, width=100, height=40):
        super().__init__(parent, bg=parent['bg'])
        
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.command = command
        self.is_enabled = True
        
        self.button = tk.Button(
            self,
            text=text,
            command=self._on_click,
            bg=bg_color,
            fg='#ffffff',
            font=('Segoe UI', 10, 'bold'),
            relief=tk.FLAT,
            cursor='hand2',
            width=width,
            height=height,
            padx=10,
            pady=5
        )
        self.button.pack()
        
        # Bind hover events
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
        """อัปเดตข้อความปุ่ม (สำหรับ Multi-language)"""
        self.button.config(text=new_text)


class CircularProgress(tk.Canvas):
    """Progress Bar แบบวงกลม (Circular) ประหยัดพื้นที่"""
    
    def __init__(self, parent, size=50, width=4, bg_color='#1e1e1e', 
                 fg_color='#7c3aed', text_color='#f3f4f6'):
        """
        สร้าง Circular Progress Bar
        
        Args:
            parent: parent widget
            size: ขนาดเส้นผ่านศูนย์กลาง (pixel)
            width: ความหนาของวงกลม
            bg_color: สีพื้นหลัง
            fg_color: สีของ progress
            text_color: สีข้อความ
        """
        super().__init__(parent, width=size, height=size, 
                        bg=bg_color, highlightthickness=0)
        
        self.size = size
        self.width = width
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.text_color = text_color
        self.progress = 0
        
        # สร้างวงกลมพื้นหลัง
        padding = 2
        self.bg_arc = self.create_arc(
            padding, padding, 
            size - padding, size - padding,
            start=90, extent=0,
            outline='#2d3748',
            width=width,
            style=tk.ARC
        )
        
        # สร้างวงกลม progress
        self.fg_arc = self.create_arc(
            padding, padding,
            size - padding, size - padding,
            start=90, extent=0,
            outline=fg_color,
            width=width,
            style=tk.ARC
        )
        
        # สร้างข้อความแสดง %
        self.text = self.create_text(
            size // 2, size // 2,
            text="0%",
            fill=text_color,
            font=('Segoe UI', 8, 'bold')
        )
    
    def set_progress(self, value):
        """
        ตั้งค่า progress (0-100)
        
        Args:
            value: ค่า progress (0-100)
        """
        self.progress = max(0, min(100, value))
        
        # คำนวณมุม (วงกลมเต็ม = -360 องศา)
        extent = -360 * (self.progress / 100)
        
        # อัปเดตวงกลม
        self.itemconfig(self.fg_arc, extent=extent)
        
        # อัปเดตข้อความ
        self.itemconfig(self.text, text=f"{int(self.progress)}%")
    
    def reset(self):
        """รีเซ็ต progress เป็น 0"""
        self.set_progress(0)


class CompactProgress(tk.Frame):
    """Progress Bar แบบ Compact (แนวนอน แต่สั้นลง)"""
    
    def __init__(self, parent, length=100, height=4, bg_color='#1e1e1e', 
                 fg_color='#7c3aed'):
        """
        สร้าง Compact Progress Bar
        
        Args:
            parent: parent widget
            length: ความยาว (pixel)
            height: ความสูง (pixel)
            bg_color: สีพื้นหลัง
            fg_color: สี progress
        """
        super().__init__(parent, bg=bg_color)
        
        self.length = length
        self.progress_value = 0
        
        # Style
        style = ttk.Style()
        style.configure("Compact.Horizontal.TProgressbar",
                       troughcolor=bg_color,
                       background=fg_color,
                       borderwidth=0,
                       thickness=height)
        
        self.progress = ttk.Progressbar(
            self,
            mode='determinate',
            length=length,
            style="Compact.Horizontal.TProgressbar"
        )
        self.progress.pack()
    
    def set_progress(self, value):
        """ตั้งค่า progress (0-100)"""
        self.progress_value = max(0, min(100, value))
        self.progress['value'] = self.progress_value
    
    def config(self, **kwargs):
        """อัปเดตค่าต่างๆ (เพื่อความ compatible กับโค้ดเดิม)"""
        if 'value' in kwargs:
            self.set_progress(kwargs['value'])
    
    def reset(self):
        """รีเซ็ต progress"""
        self.set_progress(0)


class ImageCanvas(tk.Frame):
    """Canvas สำหรับแสดงภาพพร้อม Scrollbar"""
    
    def __init__(self, parent, bg_color, placeholder_text):
        super().__init__(parent, bg=bg_color)
        
        self.bg_color = bg_color
        self.placeholder_text = placeholder_text
        self.photo = None
        self.on_resize = None
        
        # Canvas
        self.canvas = tk.Canvas(self, bg='#1e1e1e', highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky='nsew')
        
        # Scrollbars
        self.v_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.v_scrollbar.grid(row=0, column=1, sticky='ns')
        
        self.h_scrollbar = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.h_scrollbar.grid(row=1, column=0, sticky='ew')
        
        self.canvas.configure(yscrollcommand=self.v_scrollbar.set, 
                            xscrollcommand=self.h_scrollbar.set)
        
        # Grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Canvas item
        self.canvas_id = self.canvas.create_image(0, 0, anchor=tk.NW)
        
        # Placeholder
        self.set_placeholder(placeholder_text)
        
        # Bind resize
        self.canvas.bind('<Configure>', self._on_canvas_resize)
    
    def _on_canvas_resize(self, event):
        if self.on_resize:
            self.on_resize(event)
    
    def set_image(self, photo):
        """ตั้งค่าภาพ"""
        self.photo = photo
        self.canvas.itemconfig(self.canvas_id, image=photo)
    
    def set_placeholder(self, text):
        """ตั้งค่า placeholder text (สำหรับ Multi-language)"""
        self.placeholder_text = text
        self.canvas.delete('placeholder')
        self.canvas.create_text(
            self.canvas.winfo_width() // 2 if self.canvas.winfo_width() > 1 else 325,
            self.canvas.winfo_height() // 2 if self.canvas.winfo_height() > 1 else 360,
            text=text,
            fill='#6b7280',
            font=('Segoe UI', 12),
            tags='placeholder'
        )
    
    def configure_scrollregion(self, width, height):
        """ตั้งค่า scroll region"""
        self.canvas.configure(scrollregion=(0, 0, width, height))


class ZoomControls(tk.Frame):
    """ควบคุม Zoom (+, -, Reset)"""
    
    def __init__(self, parent, bg_color, fg_color, zoom_in_cmd, zoom_out_cmd, zoom_reset_cmd):
        super().__init__(parent, bg=bg_color)
        
        self.zoom_label = tk.Label(self, text="100%", font=('Segoe UI', 9),
                                   bg=bg_color, fg=fg_color)
        self.zoom_label.pack(side=tk.LEFT, padx=5)
        
        tk.Button(self, text="−", command=zoom_out_cmd,
                 font=('Segoe UI', 12, 'bold'),
                 bg=bg_color, fg=fg_color, cursor='hand2',
                 relief=tk.FLAT, width=2).pack(side=tk.LEFT, padx=2)
        
        tk.Button(self, text="⊙", command=zoom_reset_cmd,
                 font=('Segoe UI', 12),
                 bg=bg_color, fg=fg_color, cursor='hand2',
                 relief=tk.FLAT, width=2).pack(side=tk.LEFT, padx=2)
        
        tk.Button(self, text="+", command=zoom_in_cmd,
                 font=('Segoe UI', 12, 'bold'),
                 bg=bg_color, fg=fg_color, cursor='hand2',
                 relief=tk.FLAT, width=2).pack(side=tk.LEFT, padx=2)
    
    def update_label(self, zoom_level):
        """อัปเดต label แสดง %"""
        self.zoom_label.config(text=f"{int(zoom_level * 100)}%")


class StatusBar(tk.Frame):
    """แถบสถานะด้านล่าง"""
    
    def __init__(self, parent, bg_color, fg_color):
        super().__init__(parent, bg=bg_color)
        
        self.status_label = tk.Label(self, text="Ready", 
                                     font=('Segoe UI', 8),
                                     bg=bg_color, fg='#9ca3af', anchor=tk.W)
        self.status_label.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=8)
        
        tk.Frame(self, bg='#2d3748', width=1).pack(side=tk.LEFT, fill=tk.Y, padx=5)
        
        self.info_label = tk.Label(self, text="JPG, PNG, BMP → PNG",
                                   font=('Segoe UI', 7),
                                   bg=bg_color, fg='#6b7280')
        self.info_label.pack(side=tk.LEFT, padx=8)
    
    def update_status(self, text, color='#9ca3af'):
        """อัปเดตข้อความสถานะ"""
        self.status_label.config(text=text, fg=color)
    
    def update_info(self, text):
        """อัปเดตข้อมูลเพิ่มเติม"""
        self.info_label.config(text=text)