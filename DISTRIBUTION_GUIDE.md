# Markdown to PDF Converter - Distribution Guide

## ✅ What's Been Created

Your distributable macOS app is ready!

### App Location
- **App Bundle**: `dist/MarkdownToPDF.app` (~45MB)
- **Distribution Package**: `dist/MarkdownToPDF.zip` (~62MB compressed)

### Files Created
- `dist/MarkdownToPDF.app` - The standalone macOS application
- `dist/MarkdownToPDF.zip` - Ready-to-distribute zip file
- `convert_md_to_pdf_app.py` - Source code with GUI support
- `build_app_onedir.spec` - PyInstaller configuration
- `build_distribution.sh` - Script to rebuild the app

## 📦 How to Distribute

### Option 1: Share the Zip File
Simply share `dist/MarkdownToPDF.zip` with users. They can:
1. Download and unzip
2. Drag `MarkdownToPDF.app` to their Applications folder
3. Double-click to use

### Option 2: Direct App Bundle
Share the entire `MarkdownToPDF.app` folder (users can drag to Applications).

## 🚀 How Users Can Use It

### Method 1: Double-Click (GUI)
1. Double-click `MarkdownToPDF.app`
2. Select a Markdown file when prompted
3. Choose where to save the PDF
4. Done!

### Method 2: Command Line
```bash
# Direct path
/Applications/MarkdownToPDF.app/Contents/MacOS/MarkdownToPDF file.md

# Or create an alias
alias md2pdf="/Applications/MarkdownToPDF.app/Contents/MacOS/MarkdownToPDF"
md2pdf document.md output.pdf
```

### Method 3: Drag and Drop
- Drag a `.md` file onto the app icon
- PDF is created automatically in the same location

## 🔧 Rebuilding the App

If you need to rebuild:

```bash
./build_distribution.sh
```

This will:
1. Set up the environment (if needed)
2. Install dependencies
3. Build the app bundle
4. Create the distribution zip

## 📋 Requirements

- **For building**: macOS with Python 3
- **For users**: macOS 10.13+ (no Python needed - everything is bundled)

## ✨ Features

- ✅ Standalone - no dependencies needed
- ✅ GUI file picker (when double-clicked)
- ✅ Command-line support
- ✅ Drag-and-drop support
- ✅ Professional PDF styling (colored tables, headers, etc.)
- ✅ Self-contained (~45MB includes Python runtime)

## 🎯 Testing

The app has been tested and works correctly. It successfully converts Markdown files to styled PDFs with:
- Blue table headers
- Alternating row colors
- Styled headers with borders
- Professional typography

## 📝 Notes

- First launch may take 2-3 seconds (app is self-contained)
- macOS may warn about "unidentified developer" - users should right-click → Open (first time only)
- The app bundle is large (~45MB) because it includes Python and all dependencies

