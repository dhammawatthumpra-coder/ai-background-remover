# 📁 Local Models Guide

คู่มือการใช้งาน Local Models Folder

**Version**: 12.2  
**Last Updated**: 2024

---

## 🎯 วิธีการทำงาน

โปรแกรมจะค้นหา models ตามลำดับ:

1. **`./models/`** - Folder ในตำแหน่งเดียวกับ script (✅ แนะนำ)
2. **`~/.u2net/`** - Default cache folder
3. **Bundled models** - สำหรับ PyInstaller

**ดูใน**: `models.py` → `setup_local_models_path()`

---

## 📦 วิธีตั้งค่า Local Models Folder

### ขั้นตอนที่ 1: สร้าง Folder

```bash
# สร้าง models folder
mkdir models
```

หรือสร้างด้วย File Explorer/Finder:
```
project/
├── models/          👈 สร้าง folder นี้
├── config.py
├── main.py
├── models.py
├── utils.py
├── widgets.py
└── image_handler.py
```

### ขั้นตอนที่ 2: ดาวน์โหลด Model Files

**วิธีที่ 1: ใช้ rembg ดาวน์โหลดให้**

```bash
# ดาวน์โหลด u2net (แนะนำ)
python -c "from rembg import new_session; new_session('u2net')"

# ดาวน์โหลด isnet-general-use
python -c "from rembg import new_session; new_session('isnet-general-use')"

# ดาวน์โหลด u2netp
python -c "from rembg import new_session; new_session('u2netp')"
```

Models จะถูกดาวน์โหลดไปที่ `~/.u2net/`

**วิธีที่ 2: Download จาก GitHub**

ดาวน์โหลดจาก:
- https://github.com/danielgatis/rembg/releases
- https://huggingface.co/briaai/RMBG-1.4/tree/main

### ขั้นตอนที่ 3: คัดลอกไฟล์เข้า models/

**Windows:**
```cmd
copy %USERPROFILE%\.u2net\*.onnx models\
```

**macOS/Linux:**
```bash
cp ~/.u2net/*.onnx models/
```

**หรือคัดลอกด้วยมือ:**
```
~/.u2net/u2net.onnx           → ./models/u2net.onnx
~/.u2net/u2netp.onnx          → ./models/u2netp.onnx
~/.u2net/u2net_human_seg.onnx → ./models/u2net_human_seg.onnx
~/.u2net/isnet-general-use.onnx → ./models/isnet-general-use.onnx
```

### ขั้นตอนที่ 4: ตรวจสอบโครงสร้าง

```
project/
├── models/
│   ├── u2net.onnx                    ✅
│   ├── u2netp.onnx                   ✅
│   ├── u2net_human_seg.onnx          ✅
│   ├── isnet-general-use.onnx        ✅
│   ├── isnet-anime.onnx              ✅
│   └── silueta.onnx                  ✅
├── main.py
├── config.py
├── models.py
└── ...
```

### ขั้นตอนที่ 5: รันโปรแกรม

```bash
python main.py
```

**คุณจะเห็นข้อความ:**
```
✅ Using local models from: /path/to/project/models
```

---

## 🔍 ตรวจสอบว่า Local Models ทำงาน

เมื่อเปิดโปรแกรม ดูที่ **Terminal/Console**:

- **ใช้ local models:** `✅ Using local models from: ./models`
- **ใช้ cache:** `ℹ️ Using default cache: ~/.u2net`

---

## 📋 Model Files ที่ต้องการ

| Model Key | Filename | ขนาด | หมายเหตุ |
|-----------|----------|------|----------|
| u2net | u2net.onnx | ~176 MB | แนะนำ ⭐ |
| u2netp | u2netp.onnx | ~4.7 MB | เล็กสุด |
| u2net_human_seg | u2net_human_seg.onnx | ~176 MB | คนทั้งตัว |
| isnet-general-use | isnet-general-use.onnx | ~172 MB | คุณภาพสูง ⭐ |
| isnet-anime | isnet-anime.onnx | ~172 MB | อนิเมะ |
| silueta | silueta.onnx | ~43 MB | เร็วมาก |

---

## ⚙️ ข้อดีของ Local Models

### ✅ ข้อดี

1. **ไม่ต้องดาวน์โหลดซ้ำ** - เปิดโปรแกรมเร็วขึ้น
2. **ควบคุมได้** - รู้ว่ามี models อะไรบ้าง
3. **แชร์ได้ง่าย** - คัดลอก folder เดียวครบ
4. **ออฟไลน์ได้** - ไม่ต้องต่อเน็ต
5. **Portable** - ย้ายไปไหนก็ได้

### ⚠️ ข้อควรระวัง

1. **ขนาดใหญ่** - models ทั้งหมด ~700 MB
2. **อัปเดตด้วยตนเอง** - ต้องดาวน์โหลดเวอร์ชันใหม่เอง
3. **ต้องคัดลอกให้ครบ** - ขาดไฟล์จะโหลดไม่ได้

---

## 🚀 Use Cases

### 1. Development (พัฒนาโปรแกรม)
- ใส่ models ใน folder
- ไม่ต้องดาวน์โหลดซ้ำทุกครั้ง
- Test เร็วขึ้น

### 2. Distribution (แจกจ่าย)
- รวม models ไว้กับโปรแกรม
- ผู้ใช้ไม่ต้องดาวน์โหลดเอง
- เปิดใช้งานได้ทันที

### 3. Offline Use (ใช้งานออฟไลน์)
- ไม่ต้องต่ออินเทอร์เน็ต
- ใช้งานได้ทุกที่

### 4. Multiple Projects (หลายโปรเจค)
- แชร์ models ข้ามโปรเจค
- ประหยัดพื้นที่

---

## 🔧 แก้ไขปัญหา

### 1. ไม่เจอ models folder

**สาเหตุ:** ไม่มี folder `models/` หรือไม่มีไฟล์ `.onnx`

**วิธีแก้:**
```bash
# ตรวจสอบว่ามี folder
ls models/

# ตรวจสอบว่ามีไฟล์ .onnx
ls models/*.onnx
```

### 2. โปรแกรมยังดาวน์โหลด models

**สาเหตุ:** ไฟล์ไม่ตรงหรือชื่อไม่ถูกต้อง

**วิธีแก้:**
- ตรวจสอบชื่อไฟล์ว่าตรงกับตารางด้านบน
- ตรวจสอบ extension เป็น `.onnx` (ไม่ใช่ `.onnx.txt`)

### 3. Model โหลดไม่ได้

**สาเหตุ:** ไฟล์เสียหายหรือ version ไม่ตรง

**วิธีแก้:**
```bash
# ลบไฟล์เก่า
rm models/*.onnx

# ดาวน์โหลดใหม่
python -c "from rembg import new_session; new_session('u2net')"

# คัดลอกใหม่
cp ~/.u2net/*.onnx models/
```

### 4. ต้องการ models เวอร์ชันใหม่

**วิธีอัปเดต:**
```bash
# 1. อัปเดต rembg
pip install --upgrade rembg

# 2. ลบ cache เก่า
rm -rf ~/.u2net/

# 3. ดาวน์โหลดใหม่
python -c "from rembg import new_session; new_session('u2net')"

# 4. คัดลอกเข้า models/
cp ~/.u2net/*.onnx models/
```

---

## 📊 เปรียบเทียบ

| วิธี | ความเร็ว | พื้นที่ | ออฟไลน์ | แชร์ |
|------|---------|---------|---------|------|
| **Local models/** | ⭐⭐⭐⭐⭐ | 💾💾 | ✅ | ✅ |
| **Cache ~/.u2net/** | ⭐⭐⭐⭐ | 💾💾 | ✅ | ❌ |
| **Download ทุกครั้ง** | ⭐ | 💾 | ❌ | ❌ |

---

## 💡 Tips

1. **เริ่มด้วย u2net** - ไฟล์เดียว ขนาด 176 MB ✅
2. **เพิ่มทีละ model** - ตามที่ต้องการใช้
3. **Backup models/** - เก็บไว้ใช้ซ้ำ
4. **แชร์กับทีม** - คัดลอก folder เดียวครบ
5. **Symlink ได้** - `ln -s ~/.u2net/ models/`

---

## 🔗 ดาวน์โหลด Models

### Official Sources

1. **rembg GitHub**  
   https://github.com/danielgatis/rembg

2. **Hugging Face**  
   https://huggingface.co/models?search=rembg

3. **U2-Net Official**  
   https://github.com/xuebinqin/U-2-Net

### Download Links (Direct)

```bash
# U2-Net (176 MB)
wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net.onnx

# U2-Net Portrait (4.7 MB)
wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2netp.onnx

# U2-Net Human Segmentation (176 MB)
wget https://github.com/danielgatis/rembg/releases/download/v0.0.0/u2net_human_seg.onnx
```

---

## 🎓 Example: ตั้งค่าครั้งแรก

```bash
# 1. สร้าง folder
mkdir models

# 2. ดาวน์โหลด u2net
python -c "from rembg import new_session; new_session('u2net')"

# 3. คัดลอกเข้า models/
cp ~/.u2net/u2net.onnx models/

# 4. รันโปรแกรม
python main.py

# 5. ตรวจสอบ Console
# ✅ Using local models from: /path/to/models
```

**เสร็จแล้ว!** ตอนนี้คุณใช้ local models แล้ว 🎉

---

## 🔍 Technical Details

### Environment Variable

โปรแกรมตั้งค่า `U2NET_HOME` environment variable:

```python
# ใน models.py
os.environ['U2NET_HOME'] = str(local_models)
```

### Path Priority

```python
def setup_local_models_path():
    # 1. ลอง ./models/ ก่อน
    if local_models.exists():
        return str(local_models)
    
    # 2. ลอง bundled models (PyInstaller)
    if getattr(sys, 'frozen', False):
        return str(bundle_dir / '.u2net')
    
    # 3. ใช้ default cache
    return str(Path.home() / '.u2net')
```

---

## 📦 สำหรับ PyInstaller

ถ้าต้องการ build เป็น executable:

### main.spec

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('models', 'models')],  # 👈 รวม models folder
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AI_Background_Remover',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AI_Background_Remover',
)
```

### Build Command

```bash
# Build with spec
pyinstaller main.spec

# Output
dist/
└── AI_Background_Remover/
    ├── AI_Background_Remover.exe
    ├── models/                    👈 Models included!
    │   ├── u2net.onnx
    │   └── ...
    └── _internal/
```

**ดูเพิ่มเติม**: `portable_guide.md`

---

## ✅ Checklist

- [ ] สร้าง `models/` folder แล้ว
- [ ] ดาวน์โหลด model files แล้ว
- [ ] คัดลอกไฟล์ `.onnx` เข้า `models/` แล้ว
- [ ] ตรวจสอบชื่อไฟล์ถูกต้อง
- [ ] รันโปรแกรมและเห็น "Using local models" แล้ว
- [ ] ทดสอบ model ใช้งานได้

---

## 🎯 Quick Start (สรุป)

```bash
# 1. สร้าง folder
mkdir models

# 2. ดาวน์โหลด u2net (แนะนำ)
python -c "from rembg import new_session; new_session('u2net')"

# 3. คัดลอก
cp ~/.u2net/u2net.onnx models/

# 4. รัน
python main.py

# เสร็จแล้ว! 🎉
```

---

## 📝 Notes

- **ชื่อไฟล์ต้องตรง** - เช่น `u2net.onnx` (ไม่ใช่ `u2net-model.onnx`)
- **Extension ต้องเป็น .onnx** - ไม่ใช่ `.onnx.txt` หรืออื่นๆ
- **ใช้ได้กับทุก OS** - Windows, macOS, Linux
- **PyInstaller support** - รวม models ใน executable ได้

---

**© 2024 AI Background Remover v12.2**