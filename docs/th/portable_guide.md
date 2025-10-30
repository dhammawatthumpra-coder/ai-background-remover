# 🎒 Portable Setup Guide

คู่มือสร้าง AI Background Remover แบบ Portable (พกพาได้)

**Version**: 12.2  
**Last Updated**: 2024

---

## 🎯 เป้าหมาย

สร้างโปรแกรมที่:
- ✅ ไม่ต้องติดตั้ง Python
- ✅ ไม่ต้องติดตั้ง Dependencies
- ✅ ไม่ต้องดาวน์โหลด Models
- ✅ ใช้งานได้ทันที (Extract & Run)
- ✅ พกพาได้ (USB Drive, Cloud, etc.)
- ✅ รองรับหลายภาษา (EN/TH)

---

## 🔧 วิธีที่ 1: PyInstaller (แนะนำ) ⭐

### ขั้นตอนที่ 1: ติดตั้ง PyInstaller

```bash
pip install pyinstaller
```

### ขั้นตอนที่ 2: เตรียม Models

```bash
# สร้าง models folder
mkdir models

# ดาวน์โหลด models ที่ต้องการ
python -c "from rembg import new_session; new_session('u2net')"
python -c "from rembg import new_session; new_session('u2netp')"
python -c "from rembg import new_session; new_session('isnet-general-use')"

# คัดลอกเข้า models/
cp ~/.u2net/*.onnx models/
```

### ขั้นตอนที่ 3: ใช้ไฟล์ main.spec ที่มีอยู่

โปรเจคมี `main.spec` อยู่แล้ว:

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('models', 'models')],  # รวม models folder
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # ไม่แสดง console
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
    name='main',
)
```

### ขั้นตอนที่ 4: Build

```bash
# Build ด้วย spec file ที่มีอยู่
pyinstaller main.spec

# หรือ Build แบบ One Folder (แนะนำ)
pyinstaller --onedir --windowed --add-data "models:models" --name "AI_Background_Remover" main.py
```

**สำหรับ Windows:**
```cmd
pyinstaller --onedir --windowed --add-data "models;models" --name "AI_Background_Remover" main.py
```

### ขั้นตอนที่ 5: ผลลัพธ์

```
dist/
├── main/                          👈 Portable Folder!
│   ├── main.exe                    (Windows)
│   ├── models/                     (รวม models)
│   │   ├── u2net.onnx
│   │   ├── u2netp.onnx
│   │   └── ...
│   └── _internal/                  (Dependencies)
│       ├── config.py
│       ├── models.py
│       ├── utils.py
│       ├── widgets.py
│       └── ...
```

### ขั้นตอนที่ 6: ทดสอบ

```bash
# รันโปรแกรม
cd dist/main
./main.exe  # Windows
./main      # macOS/Linux

# ควรเปิดได้ทันที!
```

---

## 🔧 วิธีที่ 2: Python Embedded (Windows) 💻

### ขั้นตอนที่ 1: ดาวน์โหลด Python Embedded

```
https://www.python.org/downloads/windows/
→ เลือก "Windows embeddable package"
→ ดาวน์โหลด python-3.11.x-embed-amd64.zip
```

### ขั้นตอนที่ 2: สร้างโครงสร้าง Portable

```
AI_Background_Remover_Portable/
├── python/                    👈 แตก Python embedded
│   ├── python.exe
│   ├── python311.zip
│   └── ...
├── app/                       👈 โค้ดของเรา
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── utils.py
│   ├── widgets.py
│   ├── image_handler.py
│   └── models/                👈 Models folder
│       ├── u2net.onnx
│       └── ...
├── Lib/                       👈 Dependencies
│   └── site-packages/
│       ├── rembg/
│       ├── PIL/
│       └── ...
├── run.bat                    👈 สคริปต์เปิด
└── README.txt
```

### ขั้นตอนที่ 3: ติดตั้ง Dependencies

```bash
# เปิด Command Prompt ใน folder
cd AI_Background_Remover_Portable

# ติดตั้ง pip ใน embedded python
python\python.exe -m ensurepip

# ติดตั้ง dependencies
python\python.exe -m pip install rembg pillow numpy scipy

# ย้าย site-packages
move python\Lib\site-packages Lib\site-packages
```

### ขั้นตอนที่ 4: สร้าง run.bat

```batch
@echo off
REM AI Background Remover v12.2 - Portable Version
echo Starting AI Background Remover...

REM ตั้งค่า Python Path
set PYTHONHOME=%~dp0python
set PYTHONPATH=%~dp0app;%~dp0Lib\site-packages
set PATH=%~dp0python;%PATH%
set U2NET_HOME=%~dp0app\models

REM ปิด CUDA (ใช้ CPU เท่านั้น)
set CUDA_VISIBLE_DEVICES=-1

REM รันโปรแกรม
python\python.exe app\main.py

if errorlevel 1 pause
```

### ขั้นตอนที่ 5: สร้าง run.sh (macOS/Linux)

```bash
#!/bin/bash
# AI Background Remover v12.2 - Portable Launcher

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ตั้งค่า Environment
export PYTHONHOME="$SCRIPT_DIR/python"
export PYTHONPATH="$SCRIPT_DIR/app:$SCRIPT_DIR/Lib/site-packages"
export PATH="$SCRIPT_DIR/python/bin:$PATH"
export U2NET_HOME="$SCRIPT_DIR/app/models"
export CUDA_VISIBLE_DEVICES=-1

# รันโปรแกรม
echo "Starting AI Background Remover..."
python3 "$SCRIPT_DIR/app/main.py"
```

### ขั้นตอนที่ 6: ทดสอบ

```bash
# Windows
run.bat

# macOS/Linux
chmod +x run.sh
./run.sh
```

---

## 📦 โครงสร้าง Portable ที่สมบูรณ์

```
AI_Background_Remover_Portable_v12.2/
├── 📁 app/
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── utils.py
│   ├── widgets.py
│   ├── image_handler.py
│   └── 📁 models/              ✅ Models (750 MB)
│       ├── u2net.onnx
│       ├── u2netp.onnx
│       ├── u2net_human_seg.onnx
│       ├── isnet-general-use.onnx
│       └── isnet-anime.onnx
│
├── 📁 python/                   ✅ Python Embedded (50 MB)
│   ├── python.exe
│   └── ...
│
├── 📁 Lib/                      ✅ Dependencies (200 MB)
│   └── site-packages/
│       ├── rembg/
│       ├── PIL/
│       ├── numpy/
│       └── ...
│
├── 🚀 run.bat                   ✅ Start Script (Windows)
├── 🚀 run.sh                    ✅ Start Script (Linux/Mac)
├── 📄 README.txt
├── 📄 LICENSE.txt
└── 📄 CHANGELOG.txt

รวม: ~1 GB
```

---

## 📋 README.txt สำหรับผู้ใช้

```text
=====================================
AI Background Remover v12.2 - Portable
=====================================

🎯 วิธีใช้งาน (Windows):
1. Double-click "run.bat"
2. รอโปรแกรมเปิด
3. เลือกรูปภาพ → ลบพื้นหลัง → บันทึก

🍎 วิธีใช้งาน (macOS/Linux):
1. เปิด Terminal
2. cd ไปยัง folder นี้
3. chmod +x run.sh
4. ./run.sh

💡 Features:
- รองรับ 6 AI Models
- ลบพื้นหลังอัตโนมัติ
- Alpha Matting (ขอบละเอียด)
- Auto Crop (ตัดขอบโปร่งใส)
- Transparency Grid
- Minimum Filter (ปรับขอบ)
- Edge Processing (3 โหมด)
- Brightness/Contrast/Saturation
- หมุน/พลิกภาพ
- Multi-language (EN/TH) 🌐

📁 โครงสร้าง:
- app/        → โปรแกรมหลัก
- models/     → AI Models
- python/     → Python Runtime
- Lib/        → Dependencies

⚠️ ข้อกำหนด:
- Windows 10/11 64-bit (หรือ macOS/Linux)
- RAM: 4 GB ขึ้นไป
- Storage: 1 GB ว่าง

🐛 แก้ไขปัญหา:
- ถ้าเปิดไม่ได้: ตรวจสอบ Windows Defender
- ถ้า Model หายไป: ตรวจสอบ app/models/
- ถ้าช้า: ใช้ Model Silueta
- เปลี่ยนภาษา: คลิกปุ่ม 🌐 ที่มุมบนขวา

📞 Support:
- GitHub: [your-repo-url]
- Email: [your-email]

=====================================
© 2024 AI Background Remover Team
=====================================
```

---

## 🎁 Distribution

### ขั้นตอนที่ 1: Compress

**Windows:**
```cmd
# สร้าง ZIP
"C:\Program Files\7-Zip\7z.exe" a -tzip AI_Background_Remover_v12.2_Portable.zip AI_Background_Remover_Portable\

# หรือ PowerShell
Compress-Archive -Path AI_Background_Remover_Portable\ -DestinationPath AI_Background_Remover_v12.2_Portable.zip
```

**Linux/macOS:**
```bash
tar -czf AI_Background_Remover_v12.2_Portable.tar.gz AI_Background_Remover_Portable/

# หรือ zip
zip -r AI_Background_Remover_v12.2_Portable.zip AI_Background_Remover_Portable/
```

### ขั้นตอนที่ 2: Upload

- **GitHub Releases**: Upload .zip เป็น Release
- **Google Drive / Dropbox**: แชร์ link
- **Website**: Host สำหรับ download

---

## 📊 ขนาดไฟล์

| Component | ขนาด | หมายเหตุ |
|-----------|------|----------|
| Python Embedded | 50 MB | Runtime |
| Dependencies | 200 MB | rembg, PIL, numpy |
| **AI Models** | **750 MB** | **ตัวใหญ่สุด** |
| App Code | 1 MB | Python scripts |
| **Total** | **~1 GB** | **Compressed: ~600 MB** |

---

## ⚡ Optimization Tips

### ลดขนาด Models

```bash
# เลือกเฉพาะที่ต้องการ
models/
├── u2net.onnx           # 176 MB - เก็บไว้ (หลัก) ⭐
├── u2netp.onnx          # 4.7 MB - เก็บไว้ (เล็ก) ⭐
└── (ลบที่เหลือถ้าไม่ใช้)

# ขนาดรวม: ~180 MB
# Portable size: ~450 MB
```

### UPX Compression

```bash
# Compress executable (PyInstaller)
pip install pyinstaller

# Build with UPX
pyinstaller --upx-dir=/path/to/upx main.spec
```

**หมายเหตุ:** UPX อาจทำให้ antivirus แจ้งเตือนผิดพลาด

---

## ✅ Checklist สำหรับ Portable

- [ ] โปรแกรมเปิดได้โดยไม่ต้องติดตั้ง Python
- [ ] Models อยู่ใน folder แล้ว
- [ ] ไม่ต้องต่ออินเทอร์เน็ต
- [ ] มี README.txt คู่มือใช้งาน
- [ ] ทดสอบบนเครื่องที่ไม่มี Python
- [ ] ทดสอบบน Windows 10/11
- [ ] ทดสอบสลับภาษา EN/TH
- [ ] ทดสอบทุก AI Models
- [ ] Compress เป็น .zip แล้ว
- [ ] ขนาดไฟล์ไม่เกิน 1 GB

---

## 🎯 Quick Start (สรุป)

```bash
# 1. เตรียม models
mkdir models
python -c "from rembg import new_session; new_session('u2net')"
cp ~/.u2net/*.onnx models/

# 2. Build with PyInstaller
pyinstaller main.spec

# 3. ทดสอบ
cd dist/main
./main.exe  # Windows

# 4. แจกจ่าย
zip -r AI_Background_Remover_Portable.zip main/

# เสร็จแล้ว! 🎉
```

---

## 🔍 Technical Details

### Environment Variables

โปรแกรมใช้ environment variables:

```python
# ใน models.py
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # ปิด GPU
os.environ['U2NET_HOME'] = str(models_path)  # Model path
```

### PyInstaller Integration

โปรแกรมรองรับ PyInstaller:

```python
# ใน models.py → setup_local_models_path()
if getattr(sys, 'frozen', False):
    bundle_dir = Path(sys._MEIPASS)
    model_dir = bundle_dir / '.u2net'
    if model_dir.exists():
        os.environ['U2NET_HOME'] = str(model_dir)
```

---

## 💡 Best Practices

1. **ใช้ main.spec ที่มีอยู่** - ตั้งค่าไว้แล้ว
2. **เก็บ models ใน folder** - ไม่ต้องดาวน์โหลดซ้ำ
3. **ทดสอบบนเครื่องสะอาด** - ไม่มี Python ติดตั้ง
4. **เพิ่ม README.txt** - คู่มือใช้งานชัดเจน
5. **Compress ก่อนแจก** - ลดขนาดไฟล์

---

## 🐛 แก้ไขปัญหา

### 1. โปรแกรมเปิดไม่ได้

**สาเหตุ:** Missing dependencies

**วิธีแก้:**
```bash
# Build ใหม่พร้อม hidden imports
pyinstaller --hidden-import=rembg --hidden-import=onnxruntime main.spec
```

### 2. Model โหลดไม่ได้

**สาเหตุ:** Models ไม่ได้ถูก bundle

**วิธีแก้:**
```python
# ตรวจสอบ main.spec
datas=[('models', 'models')],  # ต้องมีบรรทัดนี้
```

### 3. Antivirus แจ้งเตือน

**สาเหตุ:** UPX compression หรือ false positive

**วิธีแก้:**
- Build โดยไม่ใช้ UPX: `--noupx`
- เพิ่ม code signing certificate
- แจ้ง whitelist ให้ผู้ใช้

### 4. ขนาดไฟล์ใหญ่เกินไป

**วิธีแก้:**
- ลดจำนวน models (เก็บแค่ u2net)
- ใช้ `--onefile` แต่จะโหลดช้ากว่า
- Compress ด้วย 7zip หรือ tar.gz

---

## 📝 Additional Files

### LICENSE.txt

```text
MIT License

Copyright (c) 2024 AI Background Remover

Permission is hereby granted, free of charge...
[ใส่ license text ตามต้องการ]
```

### CHANGELOG.txt

```text
Version 12.2 (2024)
-------------------
✨ New Features:
- Multi-language support (EN/TH)
- Circular progress bar
- Image adjustment controls (Brightness/Contrast/Saturation)
- Edge processing modes

🔧 Improvements:
- Better model management
- Local models folder support
- Improved UI/UX

🐛 Bug Fixes:
- Fixed model switching issues
- Fixed minimum filter application
```

---

**ผลลัพธ์:** โปรแกรมที่ใครๆ ก็ใช้ได้ ไม่ต้องติดตั้งอะไร แค่แตก zip แล้ว double-click! 🚀

---

**© 2024 AI Background Remover v12.2**
