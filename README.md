<div align="center">
  
  <img src="https://raw.githubusercontent.com/kael-privateresearchcore/Kael-Icon-Converter/refs/heads/main/icon.ico" width="80" alt="App Icon">
  
  # 🛡️ Kael-Icon Converter
  
  ### Professional Smart Icon Generator – Convert any image to Windows `.ico` format with custom size selection.
  
  [![GitHub Release](https://img.shields.io/github/v/release/kael-privateresearchcore/Kael-Icon-Converter?style=for-the-badge&logo=github&color=cyan)](https://github.com/kael-privateresearchcore/Kael-Icon-Converter/releases/latest)
  [![License](https://img.shields.io/github/license/kael-privateresearchcore/Kael-Icon-Converter?style=for-the-badge&logo=gnu&color=cyan)](LICENSE)
  [![Downloads](https://img.shields.io/github/downloads/kael-privateresearchcore/Kael-Icon-Converter/total?style=for-the-badge&logo=windows&color=cyan)](https://github.com/kael-privateresearchcore/Kael-Icon-Converter/releases)
  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://python.org)
  
</div>

---

## 📸 Screenshots

| Main Window | Size Selection Dialog |
|-------------|----------------------|
| ![Main Window](Screenshot%201.png) | ![Size Dialog](Screenshot%202.png) |


---

## ✨ Features

- 🖱️ **Drag & drop** or select an image (PNG, JPG, JPEG, BMP, WEBP)
- 📏 Choose exactly which icon sizes to include (16×16 up to 256×256)
- 🎨 **Live preview** before conversion
- 💎 Modern glass‑effect UI with smooth animations
- 🚫 Standalone executable – **no Python required**

---

## 📥 Download & Install

### Option 1 – Portable (recommended)
1. Go to the **[Releases](https://github.com/kael-privateresearchcore/Kael-Icon-Converter/releases)** page.
2. Download `Kael-Icon Converter.exe`.
3. Run it directly – no installation needed.

### Option 2 – Right‑click context menu (optional)
- Download `Add_Context_Menu.reg` from the same release.
- Double‑click to add **"Convert to ICO"** to the right‑click menu for image files.

---

## 🛠️ Usage

1. Launch `Kael-Icon Converter.exe`.
2. Drag & drop an image onto the window (or click **Select Image**).
3. In the dialog, tick the icon sizes you want.
4. Click **Convert To ICO** and choose a save location.
5. Your `.ico` file is ready!

---

## 🧰 Run from Source (for developers)

### Requirements
- Python 3.8+
- PyQt6
- Pillow

### Steps
```bash
git clone https://github.com/kael-privateresearchcore/Kael-Icon-Converter.git
cd Kael-Icon-Converter
pip install -r requirements.txt
python main.py
