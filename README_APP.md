# Markdown to PDF Converter - macOS App

A standalone macOS application for converting Markdown files to beautifully styled PDFs.

## Features

- **Standalone App**: No Python installation required
- **GUI Support**: Double-click to open file dialog (requires tkinter)
- **Command Line**: Use from terminal with drag-and-drop support
- **Styled Output**: Professional PDFs with colored tables, headers, and formatting

## Distribution

The app is located in `dist/MarkdownToPDF.app` and can be distributed as-is.

### For Distribution:

1. **Copy the app**: The `MarkdownToPDF.app` folder contains everything needed
2. **Zip it**: Create a zip file for easy distribution
   ```bash
   cd dist
   zip -r MarkdownToPDF.zip MarkdownToPDF.app
   ```
3. **Share**: Users can unzip and drag the app to their Applications folder

### Usage

**GUI Mode (Double-click):**
- Double-click `MarkdownToPDF.app`
- Select a Markdown file
- Choose where to save the PDF

**Command Line Mode:**
```bash
# Direct usage
/Applications/MarkdownToPDF.app/Contents/MacOS/MarkdownToPDF input.md

# Or create an alias
alias md2pdf="/Applications/MarkdownToPDF.app/Contents/MacOS/MarkdownToPDF"
md2pdf document.md output.pdf
```

**Drag and Drop:**
- Drag a `.md` file onto the app icon
- PDF will be created in the same location

## Building from Source

If you want to rebuild the app:

```bash
# Setup environment
./setup_pdf_converter.sh

# Build app
source pdf_converter_env/bin/activate
pyinstaller build_app_onedir.spec --clean
```

## Requirements

- macOS 10.13 or later
- No additional dependencies needed (all bundled in the app)

## Notes

- The app bundle is ~45MB (includes Python runtime and all dependencies)
- First launch may take a moment to start (app is self-contained)
- If macOS warns about unidentified developer, right-click → Open (first time only)

