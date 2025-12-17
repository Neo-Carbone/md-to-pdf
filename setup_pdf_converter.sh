#!/bin/bash
# Setup script for Markdown to PDF converter
set -euo pipefail

echo "Setting up Markdown to PDF converter..."

# Create virtual environment if it doesn't exist
if [ ! -d "pdf_converter_env" ]; then
    echo "Creating virtual environment..."
    python3 -m venv pdf_converter_env
fi

if [ ! -f "requirements.txt" ]; then
    echo "Error: requirements.txt not found. Aborting."
    exit 1
fi

# Activate virtual environment and install packages
echo "Installing required packages..."
source pdf_converter_env/bin/activate
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

echo "✓ Setup complete!"
echo ""
echo "To use the converter, run:"
echo "  source pdf_converter_env/bin/activate"
echo "  python3 convert_md_to_pdf.py your_file.md"
echo ""
echo "Or use the wrapper script:"
echo "  ./convert_md_to_pdf.sh your_file.md"

