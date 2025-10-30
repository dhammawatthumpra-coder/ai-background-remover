# 🚀 Advanced Models Guide (English)

Guide for Enabling Advanced AI Models (BiRefNet, DIS Series)

**Version**: 12.2  
**Last Updated**: 2024

---

## ⚠️ Common Issues

Some models require additional files or **newer rembg version**, which may cause errors:

```
No session class found for model 'dis-general-use'
No session class found for model 'dis-anime'
No session class found for model 'birefnet-general-lite'
```

---

## 🔧 Solution (3 Steps)

### Step 1: Update rembg

```bash
# Update to latest version
pip install --upgrade rembg

# Or install specific version
pip install rembg>=2.0.50
```

### Step 2: Install Additional Dependencies

```bash
# Install ONNX Runtime
pip install onnxruntime

# For GPU (if you have NVIDIA GPU)
pip install onnxruntime-gpu
```

### Step 3: Enable Models in config.py

Open `config.py` and edit the `AI_MODELS` section:

```python
# ==================== AI Models Configuration ====================
AI_MODELS = {
    # U2-Net Series (Most Stable)
    "u2net": "U2-Net ⭐ (Stable + General)",
    "u2netp": "U2-Net Portrait (Face)",
    "u2net_human_seg": "U2-Net Human (Full Body)",
    
    # Silueta (Very Fast)
    "silueta": "Silueta (Very Fast)",
    
    # IS-Net Series (High Quality)
    "isnet-general-use": "IS-Net General ⭐ (High Quality)",
    "isnet-anime": "IS-Net Anime (Anime)",
    
    # 👇 Uncomment to enable (Advanced Models)
    # "dis-general-use": "DIS General ⭐ (Stable)",
    # "dis-anime": "DIS Anime (Anime)",
    # "birefnet-general-lite": "BiRefNet Lite ⭐ (Fast + High Quality)",
    # "birefnet-portrait": "BiRefNet Portrait (Face HD)",
}
```

**Note:** Remove `#` to enable advanced models

---

## ✅ Test if Models Work

Run this command in Terminal:

```bash
python -c "from rembg import new_session; print(new_session('dis-general-use'))"
```

If no errors appear, it works!

---

## 📊 Model Comparison

| Model | Speed | Quality | Stability | Requires Extra Files |
|-------|-------|---------|-----------|---------------------|
| **U2-Net** ⭐ | Good | Good | ⭐⭐⭐⭐⭐ | No |
| **IS-Net** | Good | Very Good | ⭐⭐⭐⭐ | No |
| **Silueta** | Very Fast | Fair | ⭐⭐⭐ | No |
| **DIS** | Good | Excellent | ⭐⭐⭐⭐ | **Yes** |
| **BiRefNet** | Good | Best | ⭐⭐⭐⭐ | **Yes** |

---

## 🎯 Recommended Models by Use Case

### General Use (Beginner)
- **U2-Net** - Most stable, no issues ✅
- **IS-Net General** - Better quality than U2-Net

### Portraits/Faces
- **U2-Net Portrait** - Stable and easy to use
- **BiRefNet Portrait** - HD quality (requires extra files)

### Anime/Cartoon
- **IS-Net Anime** - Stable, good quality
- **DIS Anime** - Best quality (requires extra files)

### Speed Priority
- **Silueta** - Fastest, but lower quality

### Maximum Quality
- **BiRefNet General** - Slowest, but best quality (requires extra files)

---

## 🐛 Troubleshooting

### 1. "No session class found"

**Cause**: Old rembg version

**Solution**:
```bash
pip install --upgrade rembg
```

### 2. "Cannot parse data from external tensors"

**Cause**: Model requires external data files

**Solution**:
1. Use another model instead (U2-Net, IS-Net) ✅
2. Or download model files manually:
```bash
# Models will download automatically on first use
python -c "from rembg import remove, new_session; new_session('dis-general-use')"
```

### 3. "Model loads too slowly"

**Cause**: First-time download

**Solution**: Wait for download to complete, models will be cached

### 4. Cannot Switch Models

**Cause**: New model has issues, program will fallback to U2-Net automatically

**Solution**: Check Status Bar for "Using U2-Net instead" message

---

## 📁 Model Cache Location

Models are stored at:

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

To re-download models:

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

1. **Start with U2-Net** - Most stable, no issues ✅
2. **Update rembg regularly** - `pip install --upgrade rembg`
3. **Use IS-Net instead of DIS** - Similar quality but more stable
4. **Enable advanced models one at a time** - To see which ones work
5. **Minimum Filter = 0-2 px** - Recommended for advanced models
6. **Use Local Models Folder** - See `local_models_guide.md`

---

## 🆘 Still Having Issues?

### Check Version:
```bash
pip show rembg
```

### Update Everything:
```bash
pip install --upgrade rembg pillow numpy scipy onnxruntime
```

### Use Basic Models Instead:
- ✅ U2-Net (Recommended)
- ✅ IS-Net General
- ✅ Silueta

---

## 📝 Model Status Messages

Program shows status via Status Bar:

- ✅ **"Loaded AI Model: XXX"** - Model ready
- ⚠️ **"XXX requires additional files - Using U2-Net instead"** - Auto fallback
- ❌ **"Cannot load Model"** - Need to fix rembg

---

## 🔗 Additional Resources

- **rembg GitHub**: https://github.com/danielgatis/rembg
- **Local Models Guide**: `local_models_guide_en.md`
- **Multi-language Guide**: `multilang_guide_en.md`

---

**© 2024 AI Background Remover v12.2**
