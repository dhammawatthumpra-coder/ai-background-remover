# 🌐 Multi-language Guide

Multi-language System Guide (EN/TH) - AI Background Remover v12.2

**Version**: 12.2  
**Last Updated**: 2024

---

## 🎯 Overview

Program supports 2 languages:
- 🇬🇧 **English (EN)** - English language
- 🇹🇭 **ไทย (TH)** - Thai language

**Switch languages instantly without restart!**

---

## 🚀 Usage

### Method 1: Switch Language from Program (Recommended)

1. Open program
2. Look for **🌐 button** in top-right corner
3. Click button to switch language:
   - Using Thai → Shows "🌐 EN" (click to change to English)
   - Using English → Shows "🌐 TH" (click to change to Thai)
4. UI will change language immediately!

**See**: `main.py` → `toggle_language()`

### Method 2: Set Default Language

Edit `config.py` file:

```python
# ==================== Language Configuration ====================
# Default language - change to 'en' or 'th'
DEFAULT_LANGUAGE = 'en'  # 'th' = Thai, 'en' = English
```

**Options:**
- `'th'` - Thai (start with Thai language)
- `'en'` - English (start with English language)

---

## 📝 Supported Text List

### Top Bar

| Key | Thai | English |
|-----|------|---------|
| `settings` | ⚙️ การตั้งค่า | ⚙️ Settings |
| `ai_model` | 🤖 AI Model: | 🤖 AI Model: |
| `alpha_matting` | ✨ Alpha Matting | ✨ Alpha Matting |
| `auto_crop` | ✂️ ตัดขอบอัตโนมัติ | ✂️ Auto Crop |
| `transparency_grid` | 🔲 ตารางโปร่งใส | 🔲 Transparency Grid |
| `edge` | 🎨 ขอบ: | 🎨 Edge: |
| `minimum` | 🔻 Minimum: | 🔻 Minimum: |

### Tabs

| Key | Thai | English |
|-----|------|---------|
| `tab_original` | 📸 ต้นฉบับ | 📸 Original |
| `tab_result` | ✨ ผลลัพธ์ | ✨ Result |
| `tab_compare` | 🔄 เปรียบเทียบ | 🔄 Compare |

### Tab Headers

| Key | Thai | English |
|-----|------|---------|
| `original_image` | 📸 รูปภาพต้นฉบับ | 📸 Original Image |
| `result_image` | ✨ ผลลัพธ์ | ✨ Result |
| `before` | 📸 ก่อน | 📸 Before |
| `after` | ✨ หลัง | ✨ After |

### Buttons

| Key | Thai | English |
|-----|------|---------|
| `select_image` | 🖼 เลือก | 🖼 Select |
| `remove_bg` | 🔮 ลบพื้นหลัง | 🔮 Remove BG |
| `save` | 💾 บันทึก | 💾 Save |
| `language` | 🌐 EN | 🌐 TH |

### Adjust Controls

| Key | Thai | English |
|-----|------|---------|
| `adjust_label` | 🎚️ | 🎚️ |
| `brightness` | B | B |
| `contrast` | C | C |
| `saturation` | S | S |

### Placeholders

| Key | Thai | English |
|-----|------|---------|
| `no_image_selected` | ยังไม่ได้เลือกรูปภาพ<br><br>คลิก "เลือก" เพื่อเริ่มต้น | No image selected<br><br>Click "Select" to start |
| `waiting_result` | รอการประมวลผล<br><br>คลิก "ลบพื้นหลัง" เพื่อเริ่มต้น | Waiting for result<br><br>Click "Remove BG" to start |

### Status Messages

| Key | Thai | English |
|-----|------|---------|
| `model_loading` | ⏳ กำลังโหลด {}... | ⏳ Loading {}... |
| `model_loaded` | ✅ โหลด AI Model: {} สำเร็จ | ✅ Loaded AI Model: {} |
| `model_ready` | ✅ โหลด AI Model สำเร็จ - พร้อมใช้งาน | ✅ AI Model loaded successfully - Ready to use |
| `select_image` | 🎯 เลือกรูปภาพเพื่อเริ่มต้น | 🎯 Select an image to get started |
| `processing` | 🔮 กำลังประมวลผลด้วย {}... กรุณารอสักครู่ | 🔮 Processing with {}... Please wait |
| `success` | 🎉 ลบพื้นหลังสำเร็จ! พร้อมบันทึกไฟล์ | 🎉 Background removed successfully! Ready to save |
| `minimum_applying` | 🔄 กำลังปรับ Minimum Filter: {} px... | 🔄 Applying Minimum Filter: {} px... |
| `minimum_applied` | ✅ ปรับ Minimum Filter ({} px) สำเร็จ | ✅ Minimum Filter ({} px) applied |
| `error` | ❌ เกิดข้อผิดพลาดในการประมวลผล | ❌ Processing error |
| `image_loaded` | ✅ โหลดรูปภาพสำเร็จ: {} | ✅ Image loaded: {} |
| `file_saved` | 💾 บันทึกไฟล์: {} | 💾 File saved: {} |
| `rotate` | 🔄 หมุนภาพ 90° แล้ว | 🔄 Rotated 90° clockwise |
| `flip_h` | ↔️ พลิกภาพซ้าย-ขวาแล้ว | ↔️ Flipped horizontally |
| `flip_v` | ↕️ พลิกภาพบน-ล่างแล้ว | ↕️ Flipped vertically |
| `adjust_applied` | 🎛 ปรับภาพ: B={:.1f}, C={:.1f}, S={:.1f} | 🎛 Adjusted: B={:.1f}, C={:.1f}, S={:.1f} |
| `adjust_reset` | 🎛 รีเซ็ตการปรับแสงแล้ว | 🎛 Adjustments reset |
| `language_changed` | 🌐 เปลี่ยนภาษาเป็นไทยแล้ว | 🌐 Language changed to English |

### Edge Modes

| Key | Thai | English |
|-----|------|---------|
| `smooth` | นุ่ม (Blur+Threshold) | Smooth (Blur+Threshold) |
| `sharp` | คม (Binary Erode) | Sharp (Binary Erode) |
| `none` | ไม่มี (AI เท่านั้น) | None (AI Only) |

---

## 🔧 How It Works

### 1. Configuration (`config.py`)

```python
# Set default language
DEFAULT_LANGUAGE = 'en'  # or 'th'

# Dictionary for UI text
UI_TEXT = {
    'settings': {
        'en': '⚙️ Settings',
        'th': '⚙️ การตั้งค่า'
    },
    # ... more texts
}

# Function to get text
def get_text(key, lang=None):
    if lang is None:
        lang = DEFAULT_LANGUAGE
    return UI_TEXT[key].get(lang, UI_TEXT[key].get('en', key))
```

### 2. Main Application (`main.py`)

```python
class BackgroundRemoverApp:
    def __init__(self, root):
        self.current_lang = DEFAULT_LANGUAGE  # Store current language
        
    def toggle_language(self):
        # Switch language
        self.current_lang = 'en' if self.current_lang == 'th' else 'th'
        
        # Update window title
        self.root.title(get_text('window_title', self.current_lang))
        
        # Refresh all UI
        self.refresh_ui_texts()
        
        # Show notification
        msg = get_text('language_changed', self.current_lang)
        self.update_status(msg, COLORS['success'])
        
        # Update model manager
        self.model_manager.lang = self.current_lang
    
    def refresh_ui_texts(self):
        # Refresh Top Bar
        self.settings_label.config(text=get_text('settings', lang))
        self.ai_model_label.config(text=get_text('ai_model', lang))
        # ... update all widgets
        
        # Refresh Tabs
        self.notebook.tab(0, text=get_text('tab_original', lang))
        # ... and more
```

### 3. Model Manager (`models.py`)

```python
class AIModelManager:
    def __init__(self, root, status_callback, lang='th'):
        self.lang = lang  # Store current language
    
    def _load_model(self, model_key):
        # Use get_text() to show messages in current language
        msg = get_text('model_loading', self.lang).format(model_name)
        self.root.after(0, lambda: self.status_callback(msg))
```

---

## 📋 Adding New Text

### Step 1: Add to `config.py`

```python
UI_TEXT = {
    # Add new key
    'new_feature': {
        'en': 'New Feature',
        'th': 'ฟีเจอร์ใหม่'
    },
}
```

### Step 2: Use in Code

```python
# In main.py or other modules
text = get_text('new_feature', self.current_lang)
label.config(text=text)
```

### Step 3: Add to refresh_ui_texts()

```python
def refresh_ui_texts(self, lang):
    # Add new widget update
    self.new_label.config(text=get_text('new_feature', lang))
```

---

## 🎨 Usage Examples

### Example 1: Create Multi-language Button

```python
# In main.py
lang = self.current_lang

# Create button
self.my_button = ModernButton(
    parent,
    text=get_text('button_key', lang),
    command=self.my_function,
    bg_color=COLORS['accent'],
    hover_color=COLORS['accent_hover']
)

# Refresh when language changes
def refresh_ui_texts(self, lang):
    self.my_button.update_text(get_text('button_key', lang))
```

### Example 2: Show Messages by Language

```python
# Show status message
msg = get_text('processing', self.current_lang).format(model_name)
self.update_status(msg, COLORS['warning'])

# Show messagebox
title = get_text('error', self.current_lang)
message = get_text('no_image', self.current_lang)
messagebox.showerror(title, message)
```

### Example 3: Multi-language Placeholders

```python
# In __init__
placeholder = get_text('no_image_selected', self.current_lang)
self.label.config(text=placeholder)

# In refresh_ui_texts()
if not self.input_image:
    placeholder = get_text('no_image_selected', lang)
    self.label.config(text=placeholder)
```

---

## 🔍 Structure Overview

```
config.py
├── DEFAULT_LANGUAGE          # Default language ('en' or 'th')
├── UI_TEXT                   # UI text
├── MESSAGES                  # Status messages
├── ERROR_MESSAGES            # Error messages
├── EDGE_MODES                # Edge modes
├── WINDOW_CONFIG['title']    # Window title
└── get_text()                # Function to get text

main.py
├── BackgroundRemoverApp
│   ├── current_lang          # Current language
│   ├── toggle_language()     # Switch language
│   └── refresh_ui_texts()    # Refresh UI

models.py
├── AIModelManager
│   └── lang                  # Language for status messages

widgets.py
└── ModernButton
    └── update_text()          # Update button text
```

---

## 💡 Tips

### 1. Use Template Strings

```python
# Good - use .format() for variables
MESSAGES = {
    'processing': {
        'en': '🔮 Processing with {}... Please wait',
        'th': '🔮 กำลังประมวลผลด้วย {}... กรุณารอสักครู่'
    }
}

# Usage
msg = get_text('processing', lang).format(model_name)
```

### 2. Store Language in Instance

```python
class MyClass:
    def __init__(self, app):
        self.app = app
        self.lang = app.current_lang  # Store reference
    
    def show_message(self):
        msg = get_text('message_key', self.lang)
```

### 3. Create Helper Function

```python
def get_localized_text(self, key):
    """Helper to get text in current language"""
    return get_text(key, self.current_lang)

# Usage
text = self.get_localized_text('settings')
```

### 4. Group Related Texts

```python
# Good - group related texts
UI_TEXT = {
    'button_select': {...},
    'button_remove': {...},
    'button_save': {...},
}
```

---

## 🐛 Troubleshooting

### 1. Text Doesn't Change

**Cause:** Forgot to add to `refresh_ui_texts()`

**Fix:**
```python
def refresh_ui_texts(self, lang):
    # Add missing widget
    self.my_label.config(text=get_text('my_key', lang))
```

### 2. KeyError When Calling get_text()

**Cause:** Key doesn't exist in dictionary

**Fix:**
```python
# Check if key exists in config.py
UI_TEXT = {
    'your_key': {
        'en': 'Text',
        'th': 'ข้อความ'
    }
}
```

### 3. Wrong Language Displayed

**Cause:** Didn't pass lang parameter

**Fix:**
```python
# Bad
text = get_text('key')  # Uses DEFAULT_LANGUAGE

# Good
text = get_text('key', self.current_lang)  # Uses current language
```

---

## 📝 Checklist for Adding New Language

- [ ] Add text in `config.py` (UI_TEXT, MESSAGES, ERROR_MESSAGES)
- [ ] Update `refresh_ui_texts()` in `main.py`
- [ ] Test language switching via 🌐 button
- [ ] Test all text sections (buttons, labels, status, errors)
- [ ] Check placeholders change with language
- [ ] Check edge modes change with language
- [ ] Verify window title changes with language

---

## 🌍 Adding New Languages (Future)

To add other languages like Chinese, Japanese:

### Step 1: Edit config.py

```python
# Add new language
DEFAULT_LANGUAGE = 'en'  # 'en', 'th', 'zh', 'ja'

UI_TEXT = {
    'settings': {
        'en': '⚙️ Settings',
        'th': '⚙️ การตั้งค่า',
        'zh': '⚙️ 设置',      # Add
        'ja': '⚙️ 設定'       # Add
    },
    # ... add for all keys
}
```

### Step 2: Edit toggle_language()

```python
def toggle_language(self):
    # Cycle through languages
    languages = ['en', 'th', 'zh', 'ja']
    current_index = languages.index(self.current_lang)
    next_index = (current_index + 1) % len(languages)
    self.current_lang = languages[next_index]
    
    self.refresh_ui_texts()
```

### Step 3: Update Language Button

```python
# Show next language name
language_names = {
    'en': '🌐 TH',
    'th': '🌐 ZH',
    'zh': '🌐 JA',
    'ja': '🌐 EN'
}
button_text = language_names.get(self.current_lang, '🌐')
```

---

## 📊 Related Files

| File | Purpose | Multi-language Support |
|------|---------|----------------------|
| `config.py` | Store all language text | ✅ Full |
| `main.py` | Main UI + toggle language | ✅ Full |
| `models.py` | Status messages | ✅ Full |
| `widgets.py` | Custom widgets | ✅ Partial (update_text()) |
| `utils.py` | Utility functions | ❌ No text |
| `image_handler.py` | Image processing | ❌ No text |

---

## 🎯 Quick Reference

### Get Text
```python
text = get_text('key', lang)
```

### Switch Language
```python
self.toggle_language()
```

### Update Widget
```python
widget.config(text=get_text('key', lang))
button.update_text(get_text('key', lang))
```

### Show Message
```python
msg = get_text('message', lang).format(value)
self.update_status(msg, color)
```

---

## 🔗 Additional Resources

- **config.py**: See `UI_TEXT`, `MESSAGES`, `ERROR_MESSAGES`
- **main.py**: See `toggle_language()`, `refresh_ui_texts()`
- **models.py**: See `AIModelManager.__init__()`

---

**© 2024 AI Background Remover v12.2**