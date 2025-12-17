# Markdown to PDF Converter - CLI Tool

A command-line utility for converting Markdown files to beautifully styled PDFs with professional formatting.

## Features

- **Command Line Interface**: Simple CLI tool for batch processing
- **Styled Output**: Professional PDFs with colored tables, headers, and formatting
- **Security**: Input validation and HTML sanitization
- **macOS Quick Action**: Right-click any `.md` file to convert to PDF
- **Flexible Configuration**: Environment variables for customization

## Installation

### Option 1: Automated Setup (Recommended)

Run the setup script to create a virtual environment and install dependencies:

```bash
./setup_pdf_converter.sh
```

This creates a `pdf_converter_env/` virtual environment and installs all required packages.

### Option 2: Manual Installation

If you have Python 3.8+ installed:

```bash
# Create virtual environment (optional but recommended)
python3 -m venv pdf_converter_env
source pdf_converter_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
# Using the wrapper script (recommended)
./convert_md_to_pdf.sh input.md
./convert_md_to_pdf.sh input.md output.pdf

# Direct Python execution
python3 convert_md_to_pdf.py input.md
python3 convert_md_to_pdf.py input.md output.pdf
```

If no output file is specified, the PDF will be created in the same directory as the input file with a `.pdf` extension.

### Examples

```bash
# Convert a single file
./convert_md_to_pdf.sh document.md

# Convert with custom output location
./convert_md_to_pdf.sh document.md ~/Desktop/document.pdf

# Convert multiple files (use a loop in shell)
for file in *.md; do ./convert_md_to_pdf.sh "$file"; done
```

## Configuration

Customize behavior using environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `MD2PDF_MAX_INPUT_SIZE` | 10485760 (10MB) | Maximum input file size in bytes |
| `MD2PDF_ALLOW_OVERWRITE` | 0 | Set to 1 to allow overwriting existing PDF files |
| `MD2PDF_BASE_DIR` | (none) | Restrict file operations to this directory |
| `MD2PDF_ALLOW_OUTSIDE_BASE` | 0 | Set to 1 to allow operations outside base directory |

Example:
```bash
# Allow overwriting and increase max file size to 50MB
export MD2PDF_ALLOW_OVERWRITE=1
export MD2PDF_MAX_INPUT_SIZE=52428800
./convert_md_to_pdf.sh large_document.md
```

## macOS Quick Action Integration

Enable right-click "Convert Markdown to PDF" functionality:

### Installation

1. Copy the workflow to your Services folder:
   ```bash
   cp -r "Convert Markdown to PDF.workflow" ~/Library/Services/
   ```

2. **Important**: The workflow needs to know where your CLI tool is located. You have two options:

   **Option A: Install system-wide (recommended)**
   ```bash
   # Copy the converter to /usr/local/bin (requires sudo)
   sudo cp convert_md_to_pdf.py /usr/local/bin/
   sudo cp convert_md_to_pdf.sh /usr/local/bin/
   sudo chmod +x /usr/local/bin/convert_md_to_pdf.sh
   ```

   **Option B: Modify the workflow to use absolute paths**
   - Open `~/Library/Services/Convert Markdown to PDF.workflow` in Automator
   - Edit the shell script to use the full path to your converter
   - Save the workflow

### Usage

1. Right-click any `.md` or `.markdown` file in Finder
2. Go to **Quick Look** → **Convert Markdown to PDF**
3. The PDF will be created in the same directory as the source file

## Requirements

- **Python**: 3.8 or later
- **Dependencies**: See `requirements.txt`
- **macOS**: 10.13 or later (for Quick Action integration)

## Security

- Input files are limited to `.md` and `.markdown` extensions
- HTML content is sanitized to prevent XSS attacks
- File size limits prevent resource exhaustion
- Optional base directory restrictions for sandboxing

## Troubleshooting

### "Command not found" error
Make sure you're using the wrapper script or have activated the virtual environment:
```bash
# Use wrapper script
./convert_md_to_pdf.sh input.md

# Or activate environment first
source pdf_converter_env/bin/activate
python3 convert_md_to_pdf.py input.md
```

### Permission denied
Ensure the script files have execute permissions:
```bash
chmod +x convert_md_to_pdf.sh setup_pdf_converter.sh
```

### Quick Action not appearing
- Make sure the workflow was copied to `~/Library/Services/`
- Restart Finder or log out/in
- Check that the workflow script has the correct path to your converter

