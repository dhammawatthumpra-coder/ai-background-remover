# ======================================
# วิธีอัปโหลดโปรเจคขึ้น GitHub
# ======================================

# ขั้นตอนที่ 3: จัดโครงสร้างโปรเจค
# ======================================

# สร้างโครงสร้าง folder
mkdir -p docs/th docs/en models

# คัดลอกไฟล์ Python หลัก
cp /path/to/your/main.py .
cp /path/to/your/config.py .
cp /path/to/your/models.py .
cp /path/to/your/utils.py .
cp /path/to/your/widgets.py .
cp /path/to/your/image_handler.py .
cp /path/to/your/main.spec .

# คัดลอกคู่มือภาษาไทย
cp /path/to/your/advanced_models_guide.md docs/th/
cp /path/to/your/local_models_guide.md docs/th/
cp /path/to/your/multilang_guide.md docs/th/
cp /path/to/your/portable_guide.md docs/th/

# คัดลอกคู่มือภาษาอังกฤษ
cp /path/to/your/advanced_models_guide_en.md docs/en/
cp /path/to/your/local_models_guide_en.md docs/en/
cp /path/to/your/multilang_guide_en.md docs/en/
cp /path/to/your/portable_guide_en.md docs/en/

# (Optional) คัดลอก models ถ้าต้องการแจกพร้อม
# cp ~/.u2net/*.onnx models/

# ======================================
# ขั้นตอนที่ 4: สร้าง README.md
# ======================================

cat > README.md << 'EOF'
# 🎨 AI Background Remover v12.2

Remove image backgrounds automatically using AI - Multi-language Edition (EN/TH)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![rembg](https://img.shields.io/badge/rembg-2.0+-orange.svg)](https://github.com/danielgatis/rembg)

## ✨ Features

- 🤖 **6 AI Models** - U2-Net, IS-Net, Silueta, and more
- 🌐 **Multi-language** - English & Thai interface
- ✨ **Alpha Matting** - Detailed edge processing
- ✂️ **Auto Crop** - Trim transparency automatically
- 🎨 **Edge Modes** - 3 processing modes (Smooth/Sharp/None)
- 🎛️ **Image Adjustments** - Brightness, Contrast, Saturation
- 🔄 **Transform Tools** - Rotate, Flip, Zoom
- 📁 **Local Models** - Offline model support
- 🎒 **Portable** - PyInstaller support

## 📸 Screenshots

[Add screenshots here]

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/ai-background-remover.git
cd ai-background-remover

# Install dependencies
pip install -r requirements.txt

# Run program
python main.py
```

### First Use

1. Click **🖼 Select** to choose an image
2. Select AI Model (default: U2-Net)
3. Click **🔮 Remove BG** to process
4. Click **💾 Save** to export result
5. Switch language with **🌐** button

## 📋 Requirements

- Python 3.8+
- 4 GB RAM
- Windows 10/11, macOS 10.13+, or Linux

## 📦 Dependencies

```
rembg>=2.0.50
Pillow>=10.0.0
numpy>=1.24.0
scipy>=1.11.0
onnxruntime>=1.16.0
```

## 📚 Documentation

### Thai (ไทย) 🇹🇭
- [Advanced Models Guide](docs/th/advanced_models_guide.md)
- [Local Models Guide](docs/th/local_models_guide.md)
- [Multi-language Guide](docs/th/multilang_guide.md)
- [Portable Setup Guide](docs/th/portable_guide.md)

### English 🇬🇧
- [Advanced Models Guide](docs/en/advanced_models_guide_en.md)
- [Local Models Guide](docs/en/local_models_guide_en.md)
- [Multi-language Guide](docs/en/multilang_guide_en.md)
- [Portable Setup Guide](docs/en/portable_guide_en.md)

## 🎯 AI Models

| Model | Speed | Quality | Stability | Use Case |
|-------|-------|---------|-----------|----------|
| **U2-Net** ⭐ | Good | Good | ⭐⭐⭐⭐⭐ | General (Recommended) |
| **IS-Net** | Good | Very Good | ⭐⭐⭐⭐ | High quality |
| **Silueta** | Very Fast | Fair | ⭐⭐⭐ | Speed priority |
| U2-Net Portrait | Good | Good | ⭐⭐⭐⭐⭐ | Portraits |
| IS-Net Anime | Good | Very Good | ⭐⭐⭐⭐ | Anime/Cartoon |

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Default language
DEFAULT_LANGUAGE = 'en'  # 'en' or 'th'

# AI Models (enable/disable)
AI_MODELS = {
    "u2net": "U2-Net ⭐ (Stable + General)",
    # ... more models
}
```

## 🎒 Portable Version

Build standalone executable:

```bash
# Install PyInstaller
pip install pyinstaller

# Build
pyinstaller main.spec

# Output: dist/main/
```

See [Portable Guide](docs/en/portable_guide_en.md) for details.

## 🐛 Troubleshooting

### "No session class found"
```bash
pip install --upgrade rembg
```

### Models download slowly
Models are cached after first download (~180 MB for u2net)

### Program won't start
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) - Background removal library
- [U2-Net](https://github.com/xuebinqin/U-2-Net) - Deep learning model
- [Pillow](https://python-pillow.org/) - Image processing

## 📧 Contact

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- Email: your.email@example.com

## ⭐ Star History

If you find this project useful, please consider giving it a star ⭐

---

**© 2024 AI Background Remover v12.2**
EOF

# ======================================
# ขั้นตอนที่ 5: สร้าง requirements.txt
# ======================================

cat > requirements.txt << 'EOF'
rembg>=2.0.50
Pillow>=10.0.0
numpy>=1.24.0
scipy>=1.11.0
onnxruntime>=1.16.0
EOF

# ======================================
# ขั้นตอนที่ 6: สร้าง .gitignore
# ======================================

cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
models/*.onnx
*.png
*.jpg
*.jpeg
output/
temp/

# Logs
*.log
EOF

# ======================================
# ขั้นตอนที่ 7: Git Commands
# ======================================

# เพิ่มไฟล์ทั้งหมด
git add .

# Commit
git commit -m "Initial commit - AI Background Remover v12.2

✨ Features:
- Multi-language support (EN/TH)
- 6 AI Models (U2-Net, IS-Net, Silueta, etc.)
- Alpha Matting
- Auto Crop
- Edge processing modes
- Image adjustments (Brightness/Contrast/Saturation)
- Transform tools (Rotate/Flip/Zoom)
- Local models folder support
- Portable build support (PyInstaller)

📚 Documentation:
- Complete guides in Thai and English
- Advanced models setup
- Local models configuration
- Multi-language system
- Portable setup instructions"

# Push ขึ้น GitHub
git push origin main

# ======================================
# เสร็จแล้ว! 🎉
# ======================================

echo "✅ Successfully pushed to GitHub!"
echo "🌐 Check your repository at: https://github.com/YOUR_USERNAME/ai-background-remover"
