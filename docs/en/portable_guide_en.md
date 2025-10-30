# 🎒 Portable Setup Guide

Guide for Creating Portable AI Background Remover

**Version**: 12.2  
**Last Updated**: 2024

---

## 🎯 Goals

Create a program that:
- ✅ No Python installation required
- ✅ No dependencies installation required
- ✅ No models download required
- ✅ Works immediately (Extract & Run)
- ✅ Portable (USB Drive, Cloud, etc.)
- ✅ Multi-language support (EN/TH)

---

## 🔧 Method 1: PyInstaller (Recommended) ⭐

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Prepare Models

```bash
# Create models folder
mkdir models

# Download required models
python -c "from rembg import new_session; new_session('u2net')"
python -c "from rembg import new_session; new_session('u2netp')"
python -c "from rembg import new_session; new_session('isnet-general-use')"

# Copy to models/
cp ~/.u2net/*.onnx models/
```

### Step 3: Use Existing main.spec

Project already has `main.spec`:

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('models', 'models')],  # Include models folder
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
    console=False,  # No console window
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

### Step 4: Build

```bash
# Build with existing spec file
pyinstaller main.spec

# Or build as One Folder (Recommended)
pyinstaller --onedir --windowed --add-data "models:models" --name "AI_Background_Remover" main.py
```

**For Windows:**
```cmd
pyinstaller --onedir --windowed --add-data "models;models" --name "AI_Background_Remover" main.py
```

### Step 5: Output

```
dist/
├── main/                          👈 Portable Folder!
│   ├── main.exe                    (Windows)
│   ├── models/                     (Models included)
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

### Step 6: Test

```bash
# Run program
cd dist/main
./main.exe  # Windows
./main      # macOS/Linux

# Should open immediately!
```

---

## 🔧 Method 2: Python Embedded (Windows) 💻

### Step 1: Download Python Embedded

```
https://www.python.org/downloads/windows/
→ Select "Windows embeddable package"
→ Download python-3.11.x-embed-amd64.zip
```

### Step 2: Create Portable Structure

```
AI_Background_Remover_Portable/
├── python/                    👈 Extract Python embedded
│   ├── python.exe
│   ├── python311.zip
│   └── ...
├── app/                       👈 Our code
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
├── run.bat                    👈 Launch script
└── README.txt
```

### Step 3: Install Dependencies

```bash
# Open Command Prompt in folder
cd AI_Background_Remover_Portable

# Install pip in embedded python
python\python.exe -m ensurepip

# Install dependencies
python\python.exe -m pip install rembg pillow numpy scipy

# Move site-packages
move python\Lib\site-packages Lib\site-packages
```

### Step 4: Create run.bat

```batch
@echo off
REM AI Background Remover v12.2 - Portable Version
echo Starting AI Background Remover...

REM Set Python Path
set PYTHONHOME=%~dp0python
set PYTHONPATH=%~dp0app;%~dp0Lib\site-packages
set PATH=%~dp0python;%PATH%
set U2NET_HOME=%~dp0app\models

REM Disable CUDA (CPU only)
set CUDA_VISIBLE_DEVICES=-1

REM Run program
python\python.exe app\main.py

if errorlevel 1 pause
```

### Step 5: Create run.sh (macOS/Linux)

```bash
#!/bin/bash
# AI Background Remover v12.2 - Portable Launcher

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Set Environment
export PYTHONHOME="$SCRIPT_DIR/python"
export PYTHONPATH="$SCRIPT_DIR/app:$SCRIPT_DIR/Lib/site-packages"
export PATH="$SCRIPT_DIR/python/bin:$PATH"
export U2NET_HOME="$SCRIPT_DIR/app/models"
export CUDA_VISIBLE_DEVICES=-1

# Run program
echo "Starting AI Background Remover..."
python3 "$SCRIPT_DIR/app/main.py"
```

### Step 6: Test

```bash
# Windows
run.bat

# macOS/Linux
chmod +x run.sh
./run.sh
```

---

## 📦 Complete Portable Structure

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

Total: ~1 GB
```

---

## 📋 README.txt for Users

```text
=====================================
AI Background Remover v12.2 - Portable
=====================================

🎯 How to Use (Windows):
1. Double-click "run.bat"
2. Wait for program to open
3. Select image → Remove BG → Save

🍎 How to Use (macOS/Linux):
1. Open Terminal
2. cd to this folder
3. chmod +x run.sh
4. ./run.sh

💡 Features:
- 6 AI Models support
- Automatic background removal
- Alpha Matting (detailed edges)
- Auto Crop (trim transparency)
- Transparency Grid
- Minimum Filter (edge adjustment)
- Edge Processing (3 modes)
- Brightness/Contrast/Saturation
- Rotate/Flip images
- Multi-language (EN/TH) 🌐

📁 Structure:
- app/        → Main program
- models/     → AI Models
- python/     → Python Runtime
- Lib/        → Dependencies

⚠️ Requirements:
- Windows 10/11 64-bit (or macOS/Linux)
- RAM: 4 GB or more
- Storage: 1 GB free

🐛 Troubleshooting:
- Won't open: Check Windows Defender
- Missing models: Check app/models/
- Slow performance: Use Silueta model
- Change language: Click 🌐 button in top-right

📞 Support:
- GitHub: [your-repo-url]
- Email: [your-email]

=====================================
© 2024 AI Background Remover Team
=====================================
```

---

## 🎁 Distribution

### Step 1: Compress

**Windows:**
```cmd
# Create ZIP
"C:\Program Files\7-Zip\7z.exe" a -tzip AI_Background_Remover_v12.2_Portable.zip AI_Background_Remover_Portable\

# Or PowerShell
Compress-Archive -Path AI_Background_Remover_Portable\ -DestinationPath AI_Background_Remover_v12.2_Portable.zip
```

**Linux/macOS:**
```bash
tar -czf AI_Background_Remover_v12.2_Portable.tar.gz AI_Background_Remover_Portable/

# Or zip
zip -r AI_Background_Remover_v12.2_Portable.zip AI_Background_Remover_Portable/
```

### Step 2: Upload

- **GitHub Releases**: Upload .zip as Release
- **Google Drive / Dropbox**: Share link
- **Website**: Host for download

---

## 📊 File Sizes

| Component | Size | Notes |
|-----------|------|-------|
| Python Embedded | 50 MB | Runtime |
| Dependencies | 200 MB | rembg, PIL, numpy |
| **AI Models** | **750 MB** | **Largest** |
| App Code | 1 MB | Python scripts |
| **Total** | **~1 GB** | **Compressed: ~600 MB** |

---

## ⚡ Optimization Tips

### Reduce Model Size

```bash
# Include only needed models
models/
├── u2net.onnx           # 176 MB - Keep (main) ⭐
├── u2netp.onnx          # 4.7 MB - Keep (small) ⭐
└── (delete others if not used)

# Total size: ~180 MB
# Portable size: ~450 MB
```

### UPX Compression

```bash
# Compress executable (PyInstaller)
pip install pyinstaller

# Build with UPX
pyinstaller --upx-dir=/path/to/upx main.spec
```

**Note:** UPX may trigger false positives in antivirus software

---

## ✅ Portable Checklist

- [ ] Program opens without Python installation
- [ ] Models are in folder
- [ ] Works offline (no internet required)
- [ ] Includes README.txt user guide
- [ ] Tested on machine without Python
- [ ] Tested on Windows 10/11
- [ ] Tested language switching EN/TH
- [ ] Tested all AI Models
- [ ] Compressed as .zip
- [ ] File size under 1 GB

---

## 🎯 Quick Start (Summary)

```bash
# 1. Prepare models
mkdir models
python -c "from rembg import new_session; new_session('u2net')"
cp ~/.u2net/*.onnx models/

# 2. Build with PyInstaller
pyinstaller main.spec

# 3. Test
cd dist/main
./main.exe  # Windows

# 4. Distribute
zip -r AI_Background_Remover_Portable.zip main/

# Done! 🎉
```

---

## 🔍 Technical Details

### Environment Variables

Program uses environment variables:

```python
# In models.py
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"  # Disable GPU
os.environ['U2NET_HOME'] = str(models_path)  # Model path
```

### PyInstaller Integration

Program supports PyInstaller:

```python
# In models.py → setup_local_models_path()
if getattr(sys, 'frozen', False):
    bundle_dir = Path(sys._MEIPASS)
    model_dir = bundle_dir / '.u2net'
    if model_dir.exists():
        os.environ['U2NET_HOME'] = str(model_dir)
```

---

## 💡 Best Practices

1. **Use existing main.spec** - Already configured
2. **Keep models in folder** - No re-download needed
3. **Test on clean machine** - No Python installed
4. **Add README.txt** - Clear user instructions
5. **Compress before distribution** - Reduce file size

---

## 🐛 Troubleshooting

### 1. Program Won't Open

**Cause:** Missing dependencies

**Fix:**
```bash
# Rebuild with hidden imports
pyinstaller --hidden-import=rembg --hidden-import=onnxruntime main.spec
```

### 2. Models Won't Load

**Cause:** Models not bundled

**Fix:**
```python
# Check main.spec
datas=[('models', 'models')],  # Must have this line
```

### 3. Antivirus Warning

**Cause:** UPX compression or false positive

**Fix:**
- Build without UPX: `--noupx`
- Add code signing certificate
- Ask users to whitelist

### 4. File Size Too Large

**Fix:**
- Reduce number of models (keep only u2net)
- Use `--onefile` but slower startup
- Compress with 7zip or tar.gz

---

## 📝 Additional Files

### LICENSE.txt

```text
MIT License

Copyright (c) 2024 AI Background Remover

Permission is hereby granted, free of charge...
[Insert your license text]
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

## 🌍 Platform-Specific Notes

### Windows

- Use `run.bat` to launch
- May need to allow in Windows Defender
- Works on Windows 10/11 64-bit

### macOS

- Use `run.sh` to launch
- May need to allow in System Preferences > Security
- Requires macOS 10.13 or later

### Linux

- Use `run.sh` to launch
- May need to install tkinter: `sudo apt-get install python3-tk`
- Works on most modern distributions

---

## 📦 Advanced: Docker Container (Optional)

For true cross-platform portability:

### Dockerfile

```dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Pre-download models
RUN python -c "from rembg import new_session; new_session('u2net')"

# Run application
CMD ["python", "main.py"]
```

### Build & Run

```bash
# Build image
docker build -t ai-bg-remover .

# Run container
docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY ai-bg-remover
```

---

## 🔗 Related Guides

- **Local Models Guide**: `local_models_guide.md`
- **Multi-language Guide**: `multilang_guide.md`
- **Advanced Models Guide**: `advanced_models_guide.md`

---

## 📈 Comparison: Distribution Methods

| Method | Size | Speed | Compatibility | Ease of Use |
|--------|------|-------|---------------|-------------|
| **PyInstaller** | Medium | Fast | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Python Embedded** | Large | Fast | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Docker** | Large | Medium | ⭐⭐⭐ | ⭐⭐⭐ |
| **Source + Requirements** | Small | Slow | ⭐⭐ | ⭐⭐ |

**Recommendation:** Use PyInstaller for best results

---

## 🎓 Learning Resources

- **PyInstaller Documentation**: https://pyinstaller.org/
- **Python Embedded**: https://docs.python.org/3/using/windows.html#embedded-distribution
- **rembg GitHub**: https://github.com/danielgatis/rembg

---

**Result:** A program anyone can use, no installation required, just extract and double-click! 🚀

---

**© 2024 AI Background Remover v12.2**