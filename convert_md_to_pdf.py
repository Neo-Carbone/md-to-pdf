#!/usr/bin/env python3
"""
Convert Markdown file to styled PDF.

Usage:
    python3 convert_md_to_pdf.py input.md [output.pdf]
    
If output.pdf is not specified, it will use the same name as input.md with .pdf extension.
"""

import os
import sys
from pathlib import Path

import bleach
import markdown
from weasyprint import HTML

# Security-related configuration
ALLOWED_EXTENSIONS = {".md", ".markdown"}
MAX_INPUT_BYTES = int(os.environ.get("MD2PDF_MAX_INPUT_SIZE", 10 * 1024 * 1024))  # default 10MB
ALLOW_OVERWRITE = os.environ.get("MD2PDF_ALLOW_OVERWRITE", "0") == "1"
BASE_DIR_ENV = os.environ.get("MD2PDF_BASE_DIR")
ALLOWED_BASE_DIR = Path(BASE_DIR_ENV).resolve() if BASE_DIR_ENV else None
ALLOW_OUTSIDE_BASE = os.environ.get("MD2PDF_ALLOW_OUTSIDE_BASE", "0") == "1"

# Markdown extensions for fidelity (lists, code, tables, explicit line breaks, checkboxes)
MARKDOWN_EXTENSIONS = [
    "tables",
    "fenced_code",
    "sane_lists",
    "nl2br",
    "pymdownx.tasklist",  # Enable checkbox support
]

# Allow basic formatting while stripping scripts/unsafe HTML
ALLOWED_TAGS = sorted(
    set(bleach.sanitizer.ALLOWED_TAGS)
    | {"p", "pre", "h1", "h2", "h3", "h4", "h5", "h6", "table", "thead", "tbody", "tr", "th", "td", "code", "hr", "br", "input"}
)
ALLOWED_ATTRIBUTES = dict(bleach.sanitizer.ALLOWED_ATTRIBUTES)
ALLOWED_ATTRIBUTES.update({
    "a": ["href", "title", "name"],
    "img": ["src", "alt", "title"],
    "input": ["type", "checked", "disabled"],
})

def _enforce_base_dir(resolved_path: Path, original: str) -> None:
    """
    Ensure the resolved path does not escape an allowed base directory.
    If ALLOWED_BASE_DIR is not set, prevent relative paths from escaping the current working directory.
    """
    if ALLOWED_BASE_DIR and not ALLOW_OUTSIDE_BASE:
        try:
            resolved_path.relative_to(ALLOWED_BASE_DIR)
        except ValueError:
            raise ValueError(f"Path '{original}' is outside the allowed base directory.")
    elif not Path(original).expanduser().is_absolute():
        # For relative paths, make sure they stay under the current working directory to prevent traversal.
        cwd = Path.cwd().resolve()
        try:
            resolved_path.relative_to(cwd)
        except ValueError:
            raise ValueError("Relative path escapes the current working directory; use an absolute path instead.")


def _resolve_path(path_str: str) -> Path:
    """Resolve user-provided path safely with basic traversal checks."""
    candidate = Path(path_str).expanduser()
    resolved = candidate.resolve(strict=False)
    _enforce_base_dir(resolved, path_str)
    return resolved


def _validate_input_path(input_path: Path) -> None:
    """Validate existence, type, extension, and size of the input file."""
    if not input_path.exists() or not input_path.is_file():
        raise FileNotFoundError(f"Input file '{input_path}' not found or is not a file.")

    if input_path.suffix.lower() not in ALLOWED_EXTENSIONS:
        raise ValueError("Input file must be a Markdown file (.md or .markdown).")

    try:
        file_size = input_path.stat().st_size
    except OSError:
        raise ValueError("Unable to read input file size for validation.")

    if file_size > MAX_INPUT_BYTES:
        raise ValueError(f"Input file exceeds the maximum allowed size of {MAX_INPUT_BYTES // (1024 * 1024)} MB.")


def _prepare_output_path(output_path: Path) -> None:
    """Ensure output path is valid, parent exists, and overwrite rules are honored."""
    if output_path.exists():
        if output_path.is_dir():
            raise ValueError("Output path points to a directory, not a file.")
        if not ALLOW_OVERWRITE:
            raise FileExistsError(
                f"Output file '{output_path}' already exists. Set MD2PDF_ALLOW_OVERWRITE=1 to allow replacing it."
            )

    if not output_path.parent.exists():
        raise ValueError(f"Output directory '{output_path.parent}' does not exist.")


def convert_markdown_to_pdf(input_file, output_file=None):
    """Convert a Markdown file to a styled PDF."""
    
    try:
        input_path = _resolve_path(str(input_file))
        _validate_input_path(input_path)

        # Determine output file path
        if output_file:
            output_path = _resolve_path(str(output_file))
        else:
            output_path = input_path.with_suffix('.pdf')

        _prepare_output_path(output_path)

        # Read the markdown file
        with open(input_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Convert markdown to sanitized HTML
        html_content = markdown.markdown(
            md_content,
            extensions=MARKDOWN_EXTENSIONS,
            output_format='xhtml',
            enable_attributes=False,
        )
        safe_html_content = bleach.clean(
            html_content,
            tags=ALLOWED_TAGS,
            attributes=ALLOWED_ATTRIBUTES,
            strip=True,
        )
        
        # Add CSS styling for better formatting
        styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        @page {{
            size: letter;
            margin: 1in;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 100%;
        }}
        p {{
            margin: 0 0 14px;
        }}
        h1 {{
            color: #2c3e50;
            margin-bottom: 10px;
            margin-top: 0;
            font-size: 24px;
        }}
        h2 {{
            color: #34495e;
            margin-bottom: 8px;
            margin-top: 22px;
            font-size: 20px;
        }}
        h3 {{
            color: #555;
            margin-top: 18px;
            font-size: 17px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            page-break-inside: avoid;
            break-inside: avoid;
            border: none;
            font-size: 14px;
        }}
        th, td {{
            border: none;
            border-bottom: 1px solid #999;
            padding: 8px 6px;
            text-align: left;
            vertical-align: top;
            page-break-inside: avoid;
            break-inside: avoid;
        }}
        th {{
            font-weight: 700;
            border-top: 1px solid #999;
            background-color: #f7f7f7;
            color: #2c3e50;
        }}
        tr {{
            page-break-inside: avoid;
            break-inside: avoid;
        }}
        code {{
            background-color: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ecf0f1;
            margin: 30px 0;
        }}
        ul, ol {{
            margin: 10px 0;
            padding-left: 30px;
            font-size: 15px;
        }}
        li {{
            margin: 5px 0;
        }}
        input[type="checkbox"] {{
            margin-right: 8px;
            width: 16px;
            height: 16px;
            vertical-align: middle;
            cursor: default;
        }}
        strong {{
            color: #2c3e50;
        }}
    </style>
</head>
<body>
{safe_html_content}
</body>
</html>
"""
        
        # Convert HTML to PDF
        HTML(string=styled_html).write_pdf(output_path)
        print(f"✓ PDF created successfully: {output_path}")
    except (ValueError, FileNotFoundError, FileExistsError) as err:
        print(f"Error: {err}")
        sys.exit(1)
    except Exception:
        # Avoid leaking internal details
        print("Error: Conversion failed due to an unexpected internal issue.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_markdown_to_pdf(input_file, output_file)

