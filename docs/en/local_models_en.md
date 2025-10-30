# 📁 Local Models Guide

Guide for Using Local Models Folder

**Version**: 12.2  
**Last Updated**: 2024

---

## 🎯 How It Works

Program searches for models in this order:

1. **`./models/`** - Folder in same location as script (✅ Recommended)
2. **`~/.u2net/`** - Default cache folder
3. **Bundled models** - For PyInstaller

**See**: `models.py` → `setup_local_models_path()`

---

## 📦 Setup Local Models Folder

### Step 1: Create Folder

```bash
# Create models folder
mkdir models
```

Or create with File Explorer/Finder:
```
project/
├── models/          👈 Create this folder
├── config.py
├── main.py
├── models.py
├── utils.py
├── widgets.py
└── image_handler.py
```

### Step 2: Download Model Files

**Method 1: Use rembg to download**

```bash
# Download u2net (Recommended)
python -c "from rembg import new_session; new_session('u2net')"

# Download isnet-general-use
python -c "from rembg import new_session; new_session('isnet-general-use')"

# Download u2netp
python -c "from rembg import new_session; new_session('u2netp')"
```

Models will be downloaded to `~/.u2net/`

**Method 2: Download from GitHub**

Download from:
- https://github.com/danielgatis/rembg/releases
- https://huggingface.co/briaai/RMBG-1.4/tree/main

### Step 3: Copy Files to models/

**Windows:**
```cmd
copy %USERPROFILE%\.u2net\*.onnx models\
```

**macOS/Linux:**
```bash
cp ~/.u2net/*.onnx models/
```

**Or copy manually:**
```
~/.u2net/u2net.onnx           → ./models/u2net.onnx
~/.u2net/u2netp.onnx          → ./models/u2netp.onnx
~/.u2net/u2net_human_seg.onnx → ./models/u2net_human_seg.onnx
~/.u2net/isnet-general-use.onnx → ./models/isnet-general-use.onnx
```

### Step 4: Verify Structure

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

### Step 5: Run Program

```bash
python main.py
```

**You should see:**
```
✅ Using local models from: /path/to/project/models
```

---

## 🔍 Verify Local Models Work

When opening program, check **Terminal/Console**:

- **Using local models:** `✅ Using local models from: ./models`
- **Using cache:** `ℹ️ Using default cache: ~/.u2net`

---

## 📋 Required Model Files

| Model Key | Filename | Size | Notes |
|-----------|----------|------|-------|
| u2net | u2net.onnx | ~176 MB | Recommended ⭐ |
| u2netp | u2netp.onnx | ~4.7 MB | Smallest |
| u2net_human_seg | u2net_human_seg.onnx | ~176 MB | Full body |
| isnet-general-use | isnet-general-use.onnx | ~172 MB | High quality ⭐ |
| isnet-anime | isnet-anime.onnx | ~172 MB | Anime |
| silueta | silueta.onnx | ~43 MB | Very fast |

---

## ⚙️ Advantages of Local Models

### ✅ Pros

1. **No re-download** - Faster program startup
2. **Full control** - Know exactly what models you have
3. **Easy sharing** - Copy single folder
4. **Works offline** - No internet required
5. **Portable** - Move anywhere

### ⚠️ Considerations

1. **Large size** - All models ~700 MB
2. **Manual updates** - Need to download new versions yourself
3. **Must copy all files** - Missing files won't load

---

## 🚀 Use Cases

### 1. Development
- Put models in folder
- No re-download each time
- Faster testing

### 2. Distribution
- Include models with program
- Users don't need to download
- Works immediately

### 3. Offline Use
- No internet required
- Works anywhere

### 4. Multiple Projects
- Share models across projects
- Save storage space

---

## 🔧 Troubleshooting

### 1. models folder not found

**Cause:** No `models/` folder or no `.onnx` files

**Solution:**
```bash
# Check if folder exists
ls models/

# Check for .onnx files
ls models/*.onnx
```

### 2. Program still downloads models

**Cause:** Files don't match or wrong names

**Solution:**
- Verify filenames match table above
- Verify extension is `.onnx` (not `.onnx.txt`)

### 3. Model won't load

**Cause:** Corrupted file or wrong version

**Solution:**
```bash
# Remove old files
rm models/*.onnx

# Re-download
python -c "from rembg import new_session; new_session('u2net')"

# Copy again
cp ~/.u2net/*.onnx models/
```

### 4. Need newer model versions

**Update process:**
```bash
# 1. Update rembg
pip install --upgrade rembg

# 2. Remove old cache
rm -rf ~/.u2net/

# 3. Re-download
python -c "from rembg import new_session; new_session('u2net')"

# 4. Copy to models/
cp ~/.u2net/*.onnx models/
```

---

## 📊 Comparison

| Method | Speed | Storage | Offline | Share |
|--------|-------|---------|---------|-------|
| **Local models/** | ⭐⭐⭐⭐⭐ | 💾💾 | ✅ | ✅ |
| **Cache ~/.u2net/** | ⭐⭐⭐⭐ | 💾💾 | ✅ | ❌ |
| **Download each time** | ⭐ | 💾 | ❌ | ❌ |

---

## 💡 Tips

1. **Start with u2net** - Single file, 176 MB ✅
2. **Add models as needed** - Based on usage
3. **Backup models/** - Save for reuse
4. **Share with team** - Copy single folder
5. **Symlink works** - `ln -s ~/.u2net/ models/`

---

## 🔗 Download Models

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

## 🎓 Example: First-Time Setup

```bash
# 1. Create folder
mkdir models

# 2. Download u2net
python -c "from rembg import new_session; new_session('u2net')"

# 3. Copy to models/
cp ~/.u2net/u2net.onnx models/

# 4. Run program
python main.py

# 5. Check console
# ✅ Using local models from: /path/to/models
```

**Done!** You're now using local models 🎉

---

## 🔍 Technical Details

### Environment Variable

Program sets `U2NET_HOME` environment variable:

```python
# In models.py
os.environ['U2NET_HOME'] = str(local_models)
```

### Path Priority

```python
def setup_local_models_path():
    # 1. Try ./models/ first
    if local_models.exists():
        return str(local_models)
    
    # 2. Try bundled models (PyInstaller)
    if getattr(sys, 'frozen', False):
        return str(bundle_dir / '.u2net')
    
    # 3. Use default cache
    return str(Path.home() / '.u2net')
```

---

## 📦 For PyInstaller

To build as executable:

### main.spec

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('models', 'models')],  # 👈 Include models folder
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

**See more**: `portable_guide.md`

---

## ✅ Checklist

- [ ] Created `models/` folder
- [ ] Downloaded model files
- [ ] Copied `.onnx` files to `models/`
- [ ] Verified filenames are correct
- [ ] Ran program and saw "Using local models"
- [ ] Tested that models work

---

## 🎯 Quick Start (Summary)

```bash
# 1. Create folder
mkdir models

# 2. Download u2net (Recommended)
python -c "from rembg import new_session; new_session('u2net')"

# 3. Copy
cp ~/.u2net/u2net.onnx models/

# 4. Run
python main.py

# Done! 🎉
```

---

## 📝 Notes

- **Filenames must match** - e.g., `u2net.onnx` (not `u2net-model.onnx`)
- **Extension must be .onnx** - Not `.onnx.txt` or others
- **Works on all OS** - Windows, macOS, Linux
- **PyInstaller support** - Can bundle models in executable

---

**© 2024 AI Background Remover v12.2**
