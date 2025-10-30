# Changelog

All notable changes to AI Background Remover will be documented in this file.

## [12.2] - 2024-12-XX

### ✨ Added
- **Multi-language support** - Switch between English and Thai instantly
- **Circular progress bar** - Modern, space-saving progress indicator
- **Image adjustment controls** - Brightness, Contrast, Saturation sliders
- **Edge processing modes** - 3 modes: Smooth, Sharp, None
- **Local models folder support** - Store models locally for faster loading
- **Complete documentation** - Guides in both Thai and English
  - Advanced Models Guide
  - Local Models Guide
  - Multi-language Guide
  - Portable Setup Guide

### 🔧 Improved
- **Model management** - Better error handling and automatic fallback to U2-Net
- **UI/UX** - Cleaner interface with better organization
- **Status messages** - More informative feedback in multiple languages
- **Performance** - Optimized image processing pipeline
- **Code structure** - Modular architecture with separated concerns
  - `config.py` - All configuration and text
  - `models.py` - AI model management
  - `utils.py` - Utility functions
  - `widgets.py` - Custom UI components
  - `image_handler.py` - Image processing

### 🐛 Fixed
- Model switching issues when advanced models fail
- Minimum filter application on cropped images
- Transparency grid not updating properly
- Edge mode selection not persisting
- Zoom level reset issues

### 📦 Technical
- Added `setup_local_models_path()` for model discovery
- Implemented automatic fallback mechanism for failed models
- Added PyInstaller support with `main.spec`
- Environment variable configuration for CUDA and model paths
- Better error handling throughout the application

---

## [12.1] - 2024-11-XX

### ✨ Added
- Minimum Filter slider (0-20 px)
- Edge processing options
- Zoom controls for input and output images
- Transform tools (Rotate, Flip H/V)
- Auto Crop with padding
- Transparency Grid toggle

### 🔧 Improved
- Better model loading with progress indication
- Improved image display with fit-to-screen
- Enhanced error messages

### 🐛 Fixed
- Image aspect ratio preservation
- Canvas resize issues
- Model caching problems

---

## [12.0] - 2024-10-XX

### ✨ Added
- Initial release
- 6 AI Models support
  - U2-Net (General, Portrait, Human Segmentation)
  - IS-Net (General, Anime)
  - Silueta
- Alpha Matting option
- Auto Crop feature
- Basic UI with Tkinter

### 📦 Dependencies
- rembg >= 2.0.50
- Pillow >= 10.0.0
- numpy >= 1.24.0
- scipy >= 1.11.0
- onnxruntime >= 1.16.0

---

## Upcoming Features 🚀

### [12.3] - Planned
- [ ] Batch processing for multiple images
- [ ] Custom background colors/images
- [ ] History/Undo functionality
- [ ] Preset configurations
- [ ] Command-line interface
- [ ] More language support (Chinese, Japanese, Korean)

### [13.0] - Future
- [ ] Advanced hair/fur detection
- [ ] Smart object selection
- [ ] Background blur effects
- [ ] Cloud processing option
- [ ] Plugin system for extensions

---

## Version Naming

- **Major** (X.0.0) - Breaking changes, major new features
- **Minor** (0.X.0) - New features, improvements
- **Patch** (0.0.X) - Bug fixes, small improvements

---

**Current Version**: 12.2  
**Last Updated**: 2024

For detailed changes, see [commit history](https://github.com/YOUR_USERNAME/ai-background-remover/commits/main)
