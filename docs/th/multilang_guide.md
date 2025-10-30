# 🌐 Multi-language Guide

คู่มือการใช้งานระบบหลายภาษา (EN/TH) - AI Background Remover v12.2

**Version**: 12.2  
**Last Updated**: 2024

---

## 🎯 ภาพรวม

โปรแกรมรองรับ 2 ภาษา:
- 🇬🇧 **English (EN)** - ภาษาอังกฤษ
- 🇹🇭 **ไทย (TH)** - ภาษาไทย

**สลับภาษาได้ทันทีโดยไม่ต้อง restart!**

---

## 🚀 วิธีใช้งาน

### วิธีที่ 1: สลับภาษาจากโปรแกรม (แนะนำ)

1. เปิดโปรแกรม
2. มองหา **ปุ่ม 🌐** ที่มุมบนขวา
3. คลิกปุ่มเพื่อสลับภาษา:
   - กำลังใช้ไทย → แสดง "🌐 EN" (คลิกเพื่อเปลี่ยนเป็นอังกฤษ)
   - กำลังใช้อังกฤษ → แสดง "🌐 TH" (คลิกเพื่อเปลี่ยนเป็นไทย)
4. UI จะเปลี่ยนภาษาทันที!

**ดูใน**: `main.py` → `toggle_language()`

### วิธีที่ 2: ตั้งค่าภาษาเริ่มต้น

แก้ไขไฟล์ `config.py`:

```python
# ==================== Language Configuration ====================
# Default language - change to 'en' or 'th'
DEFAULT_LANGUAGE = 'en'  # 'th' = ไทย, 'en' = English
```

**Options:**
- `'th'` - ไทย (เริ่มต้นเป็นภาษาไทย)
- `'en'` - English (เริ่มต้นเป็นภาษาอังกฤษ)

---

## 📝 รายการข้อความที่รองรับ

### Top Bar (แถบด้านบน)

| Key | ไทย | English |
|-----|-----|---------|
| `settings` | ⚙️ การตั้งค่า | ⚙️ Settings |
| `ai_model` | 🤖 AI Model: | 🤖 AI Model: |
| `alpha_matting` | ✨ Alpha Matting | ✨ Alpha Matting |
| `auto_crop` | ✂️ ตัดขอบอัตโนมัติ | ✂️ Auto Crop |
| `transparency_grid` | 🔲 ตารางโปร่งใส | 🔲 Transparency Grid |
| `edge` | 🎨 ขอบ: | 🎨 Edge: |
| `minimum` | 🔻 Minimum: | 🔻 Minimum: |

### Tabs (แท็บ)

| Key | ไทย | English |
|-----|-----|---------|
| `tab_original` | 📸 ต้นฉบับ | 📸 Original |
| `tab_result` | ✨ ผลลัพธ์ | ✨ Result |
| `tab_compare` | 🔄 เปรียบเทียบ | 🔄 Compare |

### Tab Headers

| Key | ไทย | English |
|-----|-----|---------|
| `original_image` | 📸 รูปภาพต้นฉบับ | 📸 Original Image |
| `result_image` | ✨ ผลลัพธ์ | ✨ Result |
| `before` | 📸 ก่อน | 📸 Before |
| `after` | ✨ หลัง | ✨ After |

### Buttons (ปุ่ม)

| Key | ไทย | English |
|-----|-----|---------|
| `select_image` | 🖼 เลือก | 🖼 Select |
| `remove_bg` | 🔮 ลบพื้นหลัง | 🔮 Remove BG |
| `save` | 💾 บันทึก | 💾 Save |
| `language` | 🌐 EN | 🌐 TH |

### Adjust Controls

| Key | ไทย | English |
|-----|-----|---------|
| `adjust_label` | 🎚️ | 🎚️ |
| `brightness` | B | B |
| `contrast` | C | C |
| `saturation` | S | S |

### Placeholders

| Key | ไทย | English |
|-----|-----|---------|
| `no_image_selected` | ยังไม่ได้เลือกรูปภาพ<br><br>คลิก "เลือก" เพื่อเริ่มต้น | No image selected<br><br>Click "Select" to start |
| `waiting_result` | รอการประมวลผล<br><br>คลิก "ลบพื้นหลัง" เพื่อเริ่มต้น | Waiting for result<br><br>Click "Remove BG" to start |

### Status Messages

| Key | ไทย | English |
|-----|-----|---------|
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

| Key | ไทย | English |
|-----|-----|---------|
| `smooth` | นุ่ม (Blur+Threshold) | Smooth (Blur+Threshold) |
| `sharp` | คม (Binary Erode) | Sharp (Binary Erode) |
| `none` | ไม่มี (AI เท่านั้น) | None (AI Only) |

---

## 🔧 วิธีการทำงาน

### 1. Configuration (`config.py`)

```python
# กำหนดภาษาเริ่มต้น
DEFAULT_LANGUAGE = 'en'  # or 'th'

# Dictionary สำหรับข้อความ UI
UI_TEXT = {
    'settings': {
        'en': '⚙️ Settings',
        'th': '⚙️ การตั้งค่า'
    },
    # ... more texts
}

# ฟังก์ชันดึงข้อความ
def get_text(key, lang=None):
    if lang is None:
        lang = DEFAULT_LANGUAGE
    return UI_TEXT[key].get(lang, UI_TEXT[key].get('en', key))
```

### 2. Main Application (`main.py`)

```python
class BackgroundRemoverApp:
    def __init__(self, root):
        self.current_lang = DEFAULT_LANGUAGE  # เก็บภาษาปัจจุบัน
        
    def toggle_language(self):
        # สลับภาษา
        self.current_lang = 'en' if self.current_lang == 'th' else 'th'
        
        # อัปเดต window title
        self.root.title(get_text('window_title', self.current_lang))
        
        # รีเฟรช UI ทั้งหมด
        self.refresh_ui_texts()
        
        # แจ้งเตือน
        msg = get_text('language_changed', self.current_lang)
        self.update_status(msg, COLORS['success'])
        
        # อัปเดต model manager
        self.model_manager.lang = self.current_lang
    
    def refresh_ui_texts(self):
        # รีเฟรช Top Bar
        self.settings_label.config(text=get_text('settings', lang))
        self.ai_model_label.config(text=get_text('ai_model', lang))
        # ... อัปเดตทุก widget
        
        # รีเฟรช Tabs
        self.notebook.tab(0, text=get_text('tab_original', lang))
        # ... และอื่นๆ
```

### 3. Model Manager (`models.py`)

```python
class AIModelManager:
    def __init__(self, root, status_callback, lang='th'):
        self.lang = lang  # เก็บภาษาปัจจุบัน
    
    def _load_model(self, model_key):
        # ใช้ get_text() เพื่อแสดงข้อความตามภาษา
        msg = get_text('model_loading', self.lang).format(model_name)
        self.root.after(0, lambda: self.status_callback(msg))
```

---

## 📋 การเพิ่มข้อความใหม่

### ขั้นตอนที่ 1: เพิ่มใน `config.py`

```python
UI_TEXT = {
    # เพิ่ม key ใหม่
    'new_feature': {
        'en': 'New Feature',
        'th': 'ฟีเจอร์ใหม่'
    },
}
```

### ขั้นตอนที่ 2: ใช้ใน Code

```python
# ใน main.py หรือ module อื่นๆ
text = get_text('new_feature', self.current_lang)
label.config(text=text)
```

### ขั้นตอนที่ 3: เพิ่มใน refresh_ui_texts()

```python
def refresh_ui_texts(self, lang):
    # เพิ่มการอัปเดต widget ใหม่
    self.new_label.config(text=get_text('new_feature', lang))
```

---

## 🎨 ตัวอย่างการใช้งาน

### Example 1: สร้างปุ่มแบบ Multi-language

```python
# ใน main.py
lang = self.current_lang

# สร้างปุ่ม
self.my_button = ModernButton(
    parent,
    text=get_text('button_key', lang),
    command=self.my_function,
    bg_color=COLORS['accent'],
    hover_color=COLORS['accent_hover']
)

# รีเฟรชเมื่อเปลี่ยนภาษา
def refresh_ui_texts(self, lang):
    self.my_button.update_text(get_text('button_key', lang))
```

### Example 2: แสดง Message ตามภาษา

```python
# แสดง status message
msg = get_text('processing', self.current_lang).format(model_name)
self.update_status(msg, COLORS['warning'])

# แสดง messagebox
title = get_text('error', self.current_lang)
message = get_text('no_image', self.current_lang)
messagebox.showerror(title, message)
```

### Example 3: Placeholder แบบ Multi-language

```python
# ใน __init__
placeholder = get_text('no_image_selected', self.current_lang)
self.label.config(text=placeholder)

# ใน refresh_ui_texts()
if not self.input_image:
    placeholder = get_text('no_image_selected', lang)
    self.label.config(text=placeholder)
```

---

## 🔍 Structure Overview

```
config.py
├── DEFAULT_LANGUAGE          # ภาษาเริ่มต้น ('en' or 'th')
├── UI_TEXT                   # ข้อความ UI
├── MESSAGES                  # ข้อความ Status
├── ERROR_MESSAGES            # ข้อความ Error
├── EDGE_MODES                # โหมดขอบ
├── WINDOW_CONFIG['title']    # ชื่อ window
└── get_text()                # ฟังก์ชันดึงข้อความ

main.py
├── BackgroundRemoverApp
│   ├── current_lang          # ภาษาปัจจุบัน
│   ├── toggle_language()     # สลับภาษา
│   └── refresh_ui_texts()    # รีเฟรช UI

models.py
├── AIModelManager
│   └── lang                  # ภาษาสำหรับ status messages

widgets.py
└── ModernButton
    └── update_text()          # อัปเดตข้อความปุ่ม
```

---

## 💡 Tips

### 1. ใช้ Template Strings

```python
# ดี - ใช้ .format() สำหรับค่าแปรผัน
MESSAGES = {
    'processing': {
        'en': '🔮 Processing with {}... Please wait',
        'th': '🔮 กำลังประมวลผลด้วย {}... กรุณารอสักครู่'
    }
}

# ใช้งาน
msg = get_text('processing', lang).format(model_name)
```

### 2. เก็บภาษาใน Instance

```python
class MyClass:
    def __init__(self, app):
        self.app = app
        self.lang = app.current_lang  # เก็บ reference
    
    def show_message(self):
        msg = get_text('message_key', self.lang)
```

### 3. สร้าง Helper Function

```python
def get_localized_text(self, key):
    """Helper สำหรับดึงข้อความตามภาษาปัจจุบัน"""
    return get_text(key, self.current_lang)

# ใช้งาน
text = self.get_localized_text('settings')
```

### 4. Group Related Texts

```python
# ดี - จัดกลุ่มข้อความที่เกี่ยวข้อง
UI_TEXT = {
    'button_select': {...},
    'button_remove': {...},
    'button_save': {...},
}
```

---

## 🐛 Troubleshooting

### 1. ข้อความไม่เปลี่ยน

**สาเหตุ:** ลืมเพิ่มใน `refresh_ui_texts()`

**แก้ไข:**
```python
def refresh_ui_texts(self, lang):
    # เพิ่ม widget ที่ขาด
    self.my_label.config(text=get_text('my_key', lang))
```

### 2. KeyError เมื่อเรียก get_text()

**สาเหตุ:** Key ไม่มีใน dictionary

**แก้ไข:**
```python
# ตรวจสอบว่ามี key ใน config.py
UI_TEXT = {
    'your_key': {
        'en': 'Text',
        'th': 'ข้อความ'
    }
}
```

### 3. แสดงภาษาผิด

**สาเหตุ:** ไม่ได้ส่ง lang parameter

**แก้ไข:**
```python
# ไม่ดี
text = get_text('key')  # ใช้ DEFAULT_LANGUAGE

# ดี
text = get_text('key', self.current_lang)  # ใช้ภาษาปัจจุบัน
```

---

## 📝 Checklist สำหรับเพิ่มภาษาใหม่

- [ ] เพิ่มข้อความใน `config.py` (UI_TEXT, MESSAGES, ERROR_MESSAGES)
- [ ] อัปเดต `refresh_ui_texts()` ใน `main.py`
- [ ] ทดสอบสลับภาษาผ่านปุ่ม 🌐
- [ ] ทดสอบข้อความทุกส่วน (buttons, labels, status, errors)
- [ ] ตรวจสอบ placeholders เปลี่ยนตามภาษา
- [ ] ทดสอบ edge modes เปลี่ยนตามภาษา
- [ ] ตรวจสอบ window title เปลี่ยนตามภาษา

---

## 🌍 เพิ่มภาษาใหม่ (Future)

หากต้องการเพิ่มภาษาอื่นๆ เช่น จีน, ญี่ปุ่น:

### ขั้นตอนที่ 1: แก้ไข config.py

```python
# เพิ่มภาษาใหม่
DEFAULT_LANGUAGE = 'en'  # 'en', 'th', 'zh', 'ja'

UI_TEXT = {
    'settings': {
        'en': '⚙️ Settings',
        'th': '⚙️ การตั้งค่า',
        'zh': '⚙️ 设置',      # เพิ่ม
        'ja': '⚙️ 設定'       # เพิ่ม
    },
    # ... เพิ่มทุก key
}
```

### ขั้นตอนที่ 2: แก้ไข toggle_language()

```python
def toggle_language(self):
    # สลับแบบวนรอบ
    languages = ['en', 'th', 'zh', 'ja']
    current_index = languages.index(self.current_lang)
    next_index = (current_index + 1) % len(languages)
    self.current_lang = languages[next_index]
    
    self.refresh_ui_texts()
```

### ขั้นตอนที่ 3: อัปเดตปุ่มภาษา

```python
# แสดงชื่อภาษาถัดไป
language_names = {
    'en': '🌐 TH',
    'th': '🌐 ZH',
    'zh': '🌐 JA',
    'ja': '🌐 EN'
}
button_text = language_names.get(self.current_lang, '🌐')
```

---

## 📊 รายการไฟล์ที่เกี่ยวข้อง

| ไฟล์ | หน้าที่ | Multi-language Support |
|------|---------|----------------------|
| `config.py` | เก็บข้อความทุกภาษา | ✅ Full |
| `main.py` | UI หลัก + toggle language | ✅ Full |
| `models.py` | Status messages | ✅ Full |
| `widgets.py` | Custom widgets | ✅ Partial (update_text()) |
| `utils.py` | Utility functions | ❌ No text |
| `image_handler.py` | Image processing | ❌ No text |

---

## 🎯 Quick Reference

### ดึงข้อความ
```python
text = get_text('key', lang)
```

### สลับภาษา
```python
self.toggle_language()
```

### อัปเดต Widget
```python
widget.config(text=get_text('key', lang))
button.update_text(get_text('key', lang))
```

### แสดง Message
```python
msg = get_text('message', lang).format(value)
self.update_status(msg, color)
```

---

## 🔗 ข้อมูลเพิ่มเติม

- **config.py**: ดู `UI_TEXT`, `MESSAGES`, `ERROR_MESSAGES`
- **main.py**: ดู `toggle_language()`, `refresh_ui_texts()`
- **models.py**: ดู `AIModelManager.__init__()`

---

**© 2024 AI Background Remover v12.2**