#!/bin/bash
# Build and package the Markdown to PDF converter app

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Building Markdown to PDF Converter App..."
echo ""

# Check if virtual environment exists
if [ ! -d "pdf_converter_env" ]; then
    echo "Setting up environment..."
    ./setup_pdf_converter.sh
fi

# Activate virtual environment
source pdf_converter_env/bin/activate

# Install PyInstaller if not already installed
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "Installing PyInstaller..."
    pip install pyinstaller --quiet
fi

# Build the app
echo "Building app bundle..."
pyinstaller build_app_onedir.spec --clean --noconfirm

# Create distribution zip
if [ -d "dist/MarkdownToPDF.app" ]; then
    echo ""
    echo "Creating distribution package..."
    cd dist
    zip -r MarkdownToPDF.zip MarkdownToPDF.app > /dev/null
    cd ..
    
    echo ""
    echo "✓ Build complete!"
    echo ""
    echo "App location: dist/MarkdownToPDF.app"
    echo "Distribution package: dist/MarkdownToPDF.zip"
    echo ""
    echo "To distribute: Share the MarkdownToPDF.zip file"
    echo "To use locally: Drag MarkdownToPDF.app to Applications folder"
else
    echo "Error: App bundle not found in dist/"
    exit 1
fi

