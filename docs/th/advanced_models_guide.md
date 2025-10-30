# 🚀 Advanced Models Guide

คู่มือสำหรับเปิดใช้งาน AI Models ขั้นสูง (BiRefNet, DIS Series)

**Version**: 12.2  
**Last Updated**: 2024

---

## ⚠️ ปัญหาที่พบ

บาง Models ต้องการไฟล์เพิ่มเติมหรือ **rembg เวอร์ชันใหม่** ซึ่งอาจทำให้เกิด error:

```
No session class found for model 'dis-general-use'
No session class found for model 'dis-anime'
No session class found for model 'birefnet-general-lite'
```

---

## 🔧 วิธีแก้ไข (3 ขั้นตอน)

### ขั้นตอนที่ 1: อัปเดต rembg

```bash
# อัปเดตเป็นเวอร์ชันล่าสุด
pip install --upgrade rembg

# หรือติดตั้งเวอร์ชันเฉพาะ
pip install rembg>=2.0.50
```

### ขั้นตอนที่ 2: ติดตั้ง Dependencies เพิ่มเติม

```bash
# ติดตั้ง ONNX Runtime
pip install onnxruntime

# สำหรับ GPU (ถ้ามี NVIDIA GPU)
pip install onnxruntime-gpu
```

### ขั้นตอนที่ 3: เปิดใช้งาน Models ใน config.py

เปิดไฟล์ `config.py` และแก้ไข section `AI_MODELS`:

```python
# ==================== AI Models Configuration ====================
AI_MODELS = {
    # U2-Net Series (เสถียรที่สุด)
    "u2net": "U2-Net ⭐ (Stable + General)",
    "u2netp": "U2-Net Portrait (Face)",
    "u2net_human_seg": "U2-Net Human (Full Body)",
    
    # Silueta (เร็วมาก)
    "silueta": "Silueta (Very Fast)",
    
    # IS-Net Series (คุณภาพสูง)
    "isnet-general-use": "IS-Net General ⭐ (High Quality)",
    "isnet-anime": "IS-Net Anime (Anime)",
    
    # 👇 เอา comment ออกเพื่อเปิดใช้งาน (Advanced Models)
    # "dis-general-use": "DIS General ⭐ (Stable)",
    # "dis-anime": "DIS Anime (Anime)",
    # "birefnet-general-lite": "BiRefNet Lite ⭐ (Fast + High Quality)",
    # "birefnet-portrait": "BiRefNet Portrait (Face HD)",
}
```

**หมายเหตุ:** ลบ `#` ข้างหน้าเพื่อเปิดใช้งาน model ขั้นสูง

---

## ✅ ทดสอบว่า Models ใช้งานได้

รันคำสั่งนี้ใน Terminal:

```bash
python -c "from rembg import new_session; print(new_session('dis-general-use'))"
```

ถ้าไม่มี error แสดงว่าใช้งานได้แล้ว!

---

## 📊 เปรียบเทียบ Models

| Model | ความเร็ว | คุณภาพ | เสถียรภาพ | ต้องการไฟล์เพิ่ม |
|-------|---------|---------|-----------|----------------|
| **U2-Net** ⭐ | ดี | ดี | ⭐⭐⭐⭐⭐ | ไม่ต้อง |
| **IS-Net** | ดี | ดีมาก | ⭐⭐⭐⭐ | ไม่ต้อง |
| **Silueta** | เร็วมาก | พอใช้ | ⭐⭐⭐ | ไม่ต้อง |
| **DIS** | ดี | ดีเยี่ยม | ⭐⭐⭐⭐ | **ต้องการ** |
| **BiRefNet** | ดี | ดีที่สุด | ⭐⭐⭐⭐ | **ต้องการ** |

---

## 🎯 Models ที่แนะนำสำหรับแต่ละงาน

### ใช้งานทั่วไป (เริ่มต้น)
- **U2-Net** - เสถียรสุด ไม่มีปัญหา ✅
- **IS-Net General** - คุณภาพสูงกว่า U2-Net

### ภาพคน/ใบหน้า
- **U2-Net Portrait** - เสถียร ใช้งานง่าย
- **BiRefNet Portrait** - คุณภาพ HD (ต้องการไฟล์เพิ่ม)

### อนิเมะ/การ์ตูน
- **IS-Net Anime** - เสถียร คุณภาพดี
- **DIS Anime** - คุณภาพสูงสุด (ต้องการไฟล์เพิ่ม)

### ต้องการความเร็ว
- **Silueta** - เร็วที่สุด แต่คุณภาพต่ำกว่า

### ต้องการคุณภาพสูงสุด
- **BiRefNet General** - ช้าที่สุด แต่คุณภาพดีที่สุด (ต้องการไฟล์เพิ่ม)

---

## 🐛 แก้ไขปัญหาที่พบบ่อย

### 1. "No session class found"

**สาเหตุ**: rembg เวอร์ชันเก่า

**วิธีแก้**:
```bash
pip install --upgrade rembg
```

### 2. "Cannot parse data from external tensors"

**สาเหตุ**: Model ต้องการไฟล์ external data

**วิธีแก้**:
1. ใช้ Model อื่นแทน (U2-Net, IS-Net) ✅
2. หรือ download model files ด้วยตนเอง:
```bash
# Model จะดาวน์โหลดอัตโนมัติครั้งแรกที่ใช้
python -c "from rembg import remove, new_session; new_session('dis-general-use')"
```

### 3. "Model loads too slowly"

**สาเหตุ**: โหลดครั้งแรกต้องดาวน์โหลด

**วิธีแก้**: รอให้ดาวน์โหลดเสร็จ model จะถูกเก็บใน cache

### 4. Model เปลี่ยนไม่ได้

**สาเหตุ**: Model ใหม่มีปัญหา โปรแกรมจะ fallback ไป U2-Net อัตโนมัติ

**วิธีแก้**: ตรวจสอบ Status Bar จะแจ้งว่า "Using U2-Net instead"

---

## 📁 ตำแหน่งไฟล์ Model Cache

Models จะถูกเก็บไว้ที่:

**Windows:**
```
C:\Users\<username>\.u2net\
```

**macOS/Linux:**
```
~/.u2net/
```

---

## 🔄 Reset Models

ถ้าต้องการดาวน์โหลด models ใหม่:

**Windows:**
```cmd
rmdir /s %USERPROFILE%\.u2net
```

**macOS/Linux:**
```bash
rm -rf ~/.u2net/
```

---

## 💡 Tips

1. **เริ่มต้นด้วย U2-Net** - เสถียรที่สุด ไม่มีปัญหา ✅
2. **อัปเดต rembg เป็นประจำ** - `pip install --upgrade rembg`
3. **ใช้ IS-Net แทน DIS** - คุณภาพใกล้เคียง แต่เสถียรกว่า
4. **เปิดใช้ Models ขั้นสูงทีละตัว** - เพื่อดูว่าตัวไหนทำงานได้
5. **Minimum Filter = 0-2 px** - ค่าที่แนะนำสำหรับ models ขั้นสูง
6. **ใช้ Local Models Folder** - ดูคู่มือ `local_models_guide.md`

---

## 🆘 ยังมีปัญหา?

### ตรวจสอบเวอร์ชัน:
```bash
pip show rembg
```

### อัปเดตทุกอย่าง:
```bash
pip install --upgrade rembg pillow numpy scipy onnxruntime
```

### ใช้ Model พื้นฐานแทน:
- ✅ U2-Net (แนะนำ)
- ✅ IS-Net General
- ✅ Silueta

---

## 📝 Model Status Messages

โปรแกรมจะแจ้งสถานะผ่าน Status Bar:

- ✅ **"โหลด AI Model: XXX สำเร็จ"** - Model พร้อมใช้งาน
- ⚠️ **"XXX ต้องการไฟล์เพิ่มเติม - ใช้ U2-Net แทน"** - Fallback อัตโนมัติ
- ❌ **"ไม่สามารถโหลด Model ได้"** - ต้องแก้ไข rembg

---

## 🔗 ข้อมูลเพิ่มเติม

- **rembg GitHub**: https://github.com/danielgatis/rembg
- **Local Models Guide**: `local_models_guide.md`
- **Multi-language Guide**: `multilang_guide.md`

---

**© 2024 AI Background Remover v12.2**
