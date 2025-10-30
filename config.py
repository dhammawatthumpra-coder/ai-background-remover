"""
Configuration Module - Background Remover v12.2
การตั้งค่าทั้งหมดของโปรแกรม + Multi-language Support
"""

# ==================== Language Configuration ====================
# Default language - change to 'en' or 'th'
DEFAULT_LANGUAGE = 'en'  # 'th' = ไทย, 'en' = English

# ==================== AI Models Configuration ====================
AI_MODELS = {
    "u2net": "U2-Net ⭐ (Stable + General)",
    "u2netp": "U2-Net Portrait (Face)",
    "u2net_human_seg": "U2-Net Human (Full Body)",
    "silueta": "Silueta (Very Fast)",
    "isnet-general-use": "IS-Net General ⭐ (High Quality)",
    "isnet-anime": "IS-Net Anime (Anime)",
}

MODEL_MINIMUM_DEFAULTS = {
    "birefnet-general-lite": 1,
    "birefnet-portrait": 1,
    "birefnet-general": 1,
    "dis-general-use": 1,
    "dis-anime": 1,
    "isnet-general-use": 1,
    "isnet-anime": 1,
    "u2net": 2,
    "u2netp": 1,
    "u2net_human_seg": 2,
    "silueta": 3,
}

# ==================== UI Colors (Dark Theme) ====================
COLORS = {
    'bg': '#121212',
    'card': '#1e1e1e',
    'accent': '#7c3aed',
    'accent_hover': '#6d28d9',
    'success': '#22c55e',
    'success_hover': '#16a34a',
    'warning': '#facc15',
    'warning_hover': '#eab308',
    'text': '#f3f4f6',
    'text_dim': '#9ca3af',
    'border': '#2d3748'
}

# ==================== Processing Settings ====================
ZOOM_SETTINGS = {
    'min': 0.25,
    'max': 3.0,
    'default': 1.0
}

MINIMUM_FILTER_RANGE = {
    'min': 0,
    'max': 20,
    'default': 0
}

TRANSPARENCY_GRID = {
    'size': 20,
    'color1': (204, 204, 204),
    'color2': (255, 255, 255)
}

AUTO_CROP_PADDING = 20

# ==================== File Settings ====================
SUPPORTED_FORMATS = {
    'input': ['*.jpg', '*.jpeg', '*.png', '*.bmp'],
    'output': '.png'
}

FILE_DIALOG_TYPES = [
    ("Image files", "*.jpg *.jpeg *.png *.bmp"),
    ("All files", "*.*")
]

# ==================== Alpha Matting Settings ====================
ALPHA_MATTING_CONFIG = {
    'foreground_threshold': 240,
    'background_threshold': 10,
    'erode_size': 10
}

# ==================== Progress Bar Settings ====================
PROGRESS_BAR = {
    'length': 180,
    'steps': 10,
    'delay': 0.2
}

# ==================== Window Settings ====================
WINDOW_CONFIG = {
    'title': {
        'en': 'AI Background Remover v12.2 - Multi-language Edition',
        'th': 'โปรแกรมลบพื้นหลังรูปภาพ v12.2 - รองรับหลายภาษา'
    },
    'state': 'zoomed'
}

# ==================== Canvas Settings ====================
CANVAS_DEFAULT_SIZE = {
    'width': 650,
    'height': 720
}

# ==================== Edge Processing Modes ====================
EDGE_MODES = {
    'smooth': {
        'en': 'Smooth (Blur+Threshold)',
        'th': 'นุ่ม (Blur+Threshold)'
    },
    'sharp': {
        'en': 'Sharp (Binary Erode)',
        'th': 'คม (Binary Erode)'
    },
    'none': {
        'en': 'None (AI Only)',
        'th': 'ไม่มี (AI เท่านั้น)'
    }
}

# ==================== Multi-language UI Text ====================
UI_TEXT = {
    # Top Bar
    'settings': {
        'en': '⚙️ Settings',
        'th': '⚙️ การตั้งค่า'
    },
    'ai_model': {
        'en': '🤖 AI Model:',
        'th': '🤖 AI Model:'
    },
    'alpha_matting': {
        'en': '✨ Alpha Matting',
        'th': '✨ Alpha Matting'
    },
    'auto_crop': {
        'en': '✂️ Auto Crop',
        'th': '✂️ ตัดขอบอัตโนมัติ'
    },
    'transparency_grid': {
        'en': '🔲 Transparency Grid',
        'th': '🔲 ตารางโปร่งใส'
    },
    'edge': {
        'en': '🎨 Edge:',
        'th': '🎨 ขอบ:'
    },
    'minimum': {
        'en': '🔻 Minimum:',
        'th': '🔻 Minimum:'
    },
    
    # Tabs
    'tab_original': {
        'en': '📸 Original',
        'th': '📸 ต้นฉบับ'
    },
    'tab_result': {
        'en': '✨ Result',
        'th': '✨ ผลลัพธ์'
    },
    'tab_compare': {
        'en': '🔄 Compare',
        'th': '🔄 เปรียบเทียบ'
    },
    
    # Tab Headers
    'original_image': {
        'en': '📸 Original Image',
        'th': '📸 รูปภาพต้นฉบับ'
    },
    'result_image': {
        'en': '✨ Result',
        'th': '✨ ผลลัพธ์'
    },
    'before': {
        'en': '📸 Before',
        'th': '📸 ก่อน'
    },
    'after': {
        'en': '✨ After',
        'th': '✨ หลัง'
    },
    
    # Buttons
    'select_image': {
        'en': '🖼 Select',
        'th': '🖼 เลือก'
    },
    'remove_bg': {
        'en': '🔮 Remove BG',
        'th': '🔮 ลบพื้นหลัง'
    },
    'save': {
        'en': '💾 Save',
        'th': '💾 บันทึก'
    },
    'language': {
        'en': '🌐 TH',
        'th': '🌐 EN'
    },
    
    # Adjust controls
    'adjust_label': {
        'en': '🎚️',
        'th': '🎚️'
    },
    'brightness': {
        'en': 'B',
        'th': 'B'
    },
    'contrast': {
        'en': 'C',
        'th': 'C'
    },
    'saturation': {
        'en': 'S',
        'th': 'S'
    },
    
    # Placeholders
    'no_image_selected': {
        'en': 'No image selected\n\nClick "Select" to start',
        'th': 'ยังไม่ได้เลือกรูปภาพ\n\nคลิก "เลือก" เพื่อเริ่มต้น'
    },
    'waiting_result': {
        'en': 'Waiting for result\n\nClick "Remove BG" to start',
        'th': 'รอการประมวลผล\n\nคลิก "ลบพื้นหลัง" เพื่อเริ่มต้น'
    },
    
    # Dialog titles
    'select_image_title': {
        'en': 'Select Image',
        'th': 'เลือกรูปภาพ'
    },
    'save_image_title': {
        'en': 'Save Image',
        'th': 'บันทึกรูปภาพ'
    }
}

# ==================== Multi-language Messages ====================
MESSAGES = {
    'model_loading': {
        'en': '⏳ Loading {}...',
        'th': '⏳ กำลังโหลด {}...'
    },
    'model_loaded': {
        'en': '✅ Loaded AI Model: {}',
        'th': '✅ โหลด AI Model: {} สำเร็จ'
    },
    'model_ready': {
        'en': '✅ AI Model loaded successfully - Ready to use',
        'th': '✅ โหลด AI Model สำเร็จ - พร้อมใช้งาน'
    },
    'select_image': {
        'en': '🎯 Select an image to get started',
        'th': '🎯 เลือกรูปภาพเพื่อเริ่มต้น'
    },
    'processing': {
        'en': '🔮 Processing with {}... Please wait',
        'th': '🔮 กำลังประมวลผลด้วย {}... กรุณารอสักครู่'
    },
    'success': {
        'en': '🎉 Background removed successfully! Ready to save',
        'th': '🎉 ลบพื้นหลังสำเร็จ! พร้อมบันทึกไฟล์'
    },
    'minimum_applying': {
        'en': '🔄 Applying Minimum Filter: {} px...',
        'th': '🔄 กำลังปรับ Minimum Filter: {} px...'
    },
    'minimum_applied': {
        'en': '✅ Minimum Filter ({} px) applied',
        'th': '✅ ปรับ Minimum Filter ({} px) สำเร็จ'
    },
    'error': {
        'en': '❌ Processing error',
        'th': '❌ เกิดข้อผิดพลาดในการประมวลผล'
    },
    'image_loaded': {
        'en': '✅ Image loaded: {}',
        'th': '✅ โหลดรูปภาพสำเร็จ: {}'
    },
    'file_saved': {
        'en': '💾 File saved: {}',
        'th': '💾 บันทึกไฟล์: {}'
    },
    'rotate': {
        'en': '🔄 Rotated 90° clockwise',
        'th': '🔄 หมุนภาพ 90° แล้ว'
    },
    'flip_h': {
        'en': '↔️ Flipped horizontally',
        'th': '↔️ พลิกภาพซ้าย-ขวาแล้ว'
    },
    'flip_v': {
        'en': '↕️ Flipped vertically',
        'th': '↕️ พลิกภาพบน-ล่างแล้ว'
    },
    'zoom_in': {
        'en': '🔍 Zoom in: {}%',
        'th': '🔍 ซูมเข้า: {}%'
    },
    'zoom_out': {
        'en': '🔍 Zoom out: {}%',
        'th': '🔍 ซูมออก: {}%'
    },
    'zoom_reset': {
        'en': '🔍 Reset zoom: {}%',
        'th': '🔍 รีเซ็ตซูม: {}%'
    },
    'adjust_applied': {
        'en': '🎛 Adjusted: B={:.1f}, C={:.1f}, S={:.1f}',
        'th': '🎛 ปรับภาพ: B={:.1f}, C={:.1f}, S={:.1f}'
    },
    'adjust_reset': {
        'en': '🎛 Adjustments reset',
        'th': '🎛 รีเซ็ตการปรับแสงแล้ว'
    },
    'language_changed': {
        'en': '🌐 Language changed to English',
        'th': '🌐 เปลี่ยนภาษาเป็นไทยแล้ว'
    }
}

# ==================== Multi-language Error Messages ====================
ERROR_MESSAGES = {
    'model_load_failed': {
        'en': """❌ Cannot load AI Model

Cause: This model requires additional files or newer version

💡 Suggestions:
1. Use another model (Recommended: U2-Net or IS-Net General)
2. Update rembg: pip install --upgrade rembg
3. Install onnxruntime: pip install onnxruntime-gpu

Error details:
{}""",
        'th': """❌ ไม่สามารถโหลด AI Model ได้

สาเหตุ: Model นี้ต้องการไฟล์เพิ่มเติมหรือ Version ที่ใหม่กว่า

💡 คำแนะนำ:
1. ใช้ Model อื่นแทน (แนะนำ: U2-Net หรือ IS-Net General)
2. อัปเดต rembg: pip install --upgrade rembg
3. ติดตั้ง onnxruntime เพิ่มเติม: pip install onnxruntime-gpu

รายละเอียด Error:
{}"""
    },
    'model_not_supported': {
        'en': """Model not supported

This model has processing issues

💡 Suggestions:
• Try U2-Net or IS-Net General
• Update rembg: pip install --upgrade rembg""",
        'th': """Model ไม่รองรับ

Model นี้มีปัญหาในการประมวลผล

💡 แนะนำ:
• ลองเปลี่ยนเป็น U2-Net หรือ IS-Net General
• อัปเดต rembg: pip install --upgrade rembg"""
    },
    'no_image': {
        'en': 'Please select an image first or wait for AI Model to load',
        'th': 'กรุณาเลือกรูปภาพก่อน หรือรอให้ AI Model โหลดเสร็จ'
    },
    'no_output': {
        'en': 'No result image to save yet',
        'th': 'ยังไม่มีภาพผลลัพธ์ให้บันทึก'
    },
    'load_image_failed': {
        'en': 'Cannot load image:\n{}',
        'th': 'ไม่สามารถโหลดรูปภาพได้:\n{}'
    },
    'save_image_failed': {
        'en': 'Cannot save image:\n{}',
        'th': 'ไม่สามารถบันทึกรูปภาพได้:\n{}'
    },
    'processing_failed': {
        'en': 'Cannot remove background:\n{}',
        'th': 'ไม่สามารถลบพื้นหลังได้:\n{}'
    },
    'save_success': {
        'en': 'Image saved successfully:\n{}',
        'th': 'บันทึกรูปภาพสำเร็จ:\n{}'
    },
    'warning': {
        'en': 'Warning',
        'th': 'คำเตือน'
    },
    'error': {
        'en': 'Error',
        'th': 'ข้อผิดพลาด'
    },
    'success': {
        'en': 'Success',
        'th': 'สำเร็จ'
    }
}

# ==================== Default Settings ====================
DEFAULT_SETTINGS = {
    'model': 'u2net',
    'alpha_matting': False,
    'auto_crop': True,
    'transparency_grid': True,
    'minimum_filter': 0,
    'edge_mode': 'smooth'
}

# ==================== Language Helper Functions ====================
def get_text(key, lang=None):
    """
    Get translated text
    
    Args:
        key: text key (e.g., 'settings', 'select_image')
        lang: language code ('en' or 'th'), default from DEFAULT_LANGUAGE
    
    Returns:
        str: translated text
    """
    if lang is None:
        lang = DEFAULT_LANGUAGE
    
    # Try UI_TEXT first
    if key in UI_TEXT:
        return UI_TEXT[key].get(lang, UI_TEXT[key].get('en', key))
    
    # Try MESSAGES
    if key in MESSAGES:
        return MESSAGES[key].get(lang, MESSAGES[key].get('en', key))
    
    # Try ERROR_MESSAGES
    if key in ERROR_MESSAGES:
        return ERROR_MESSAGES[key].get(lang, ERROR_MESSAGES[key].get('en', key))
    
    # Try WINDOW_CONFIG
    if 'title' in WINDOW_CONFIG and key == 'window_title':
        return WINDOW_CONFIG['title'].get(lang, WINDOW_CONFIG['title'].get('en'))
    
    # Fallback
    return key


def get_edge_mode_text(mode, lang=None):
    """Get translated edge mode text"""
    if lang is None:
        lang = DEFAULT_LANGUAGE
    
    if mode in EDGE_MODES:
        return EDGE_MODES[mode].get(lang, EDGE_MODES[mode].get('en', mode))
    return mode