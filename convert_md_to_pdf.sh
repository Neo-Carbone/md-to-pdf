#!/bin/bash
# Wrapper script that handles virtual environment activation
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/pdf_converter_env"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Running setup..."
    "$SCRIPT_DIR/setup_pdf_converter.sh"
fi

# Activate virtual environment and run the converter
if [ ! -f "$VENV_DIR/bin/activate" ]; then
    echo "Error: virtual environment is incomplete or missing."
    exit 1
fi

source "$VENV_DIR/bin/activate"
python3 "$SCRIPT_DIR/convert_md_to_pdf.py" "$@"

