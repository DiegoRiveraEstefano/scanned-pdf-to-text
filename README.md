# Scanned PDF to Text

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

A Python CLI tool that converts scanned PDFs/documents into searchable text with multiple output formats using OCR (Optical Character Recognition).

## Features ✨
- Converts scanned PDFs to `.txt`, `.docx`, `.md`, and `.json` formats
- Multiprocessing support for faster OCR processing
- Image preprocessing with OpenCV/PILLOW for enhanced OCR accuracy
- Supports 100+ languages via Tesseract OCR engine
- Custom page range selection
- Configurable output directory
- Verbose logging mode
- Automatic PDF-to-image conversion using Ghostscript

## Installation 📦

### Prerequisites
- **Python 3.8+**: [Installation Guide](https://www.python.org/downloads/)
- **Tesseract OCR**: [Installation Guide](https://github.com/tesseract-ocr/tesseract)

**Linux (Debian/Ubuntu):**
```bash
sudo apt install tesseract-ocr
# For additional languages:
sudo apt install tesseract-ocr-{fra,spa,deu,chi-sim}  # Example languages
```

**macOS (using Homebrew):**
```bash
brew install tesseract
```

**Windows (using Chocolatey):**
```bash
choco install tesseract
```

### Python Package
```bash
pip install scanned-pdf-to-text
```

## Usage

### Basic conversion:
```bash
pdf2text input.pdf --output output.txt
```

### Advanced example:
```bash
pdf2text scanned_document.pdf \
  --format docx md json \
  --lang eng+fra \
  --processes 4 \
  --output-dir converted_files \
  --pages 1-10,15,20-25 \
  --verbose
```

### CLI Options:

- --format TEXT           Output formats (comma-separated) [default: txt]
                        Options: txt, docx, md, json
- --lang TEXT             OCR language(s) [default: eng]
- --processes INTEGER     Number of parallel processes [default: CPU count]
- --output-dir DIRECTORY  Custom output directory [default: ./output]
- --pages TEXT            Page range (e.g., 1-5,7,10-15)
- --verbose               Enable verbose logging
- --help                  Show help message

## How It Works 🔍

**PDF to Images:** Convert PDF pages to high-resolution TIFF images

**Preprocessing:**

- Noise reduction

- Contrast enhancement

- Skew correction

- Binarization

**OCR Processing:** Parallel text extraction using Tesseract

**Post-processing:** Format-specific text organization

**Output Generation:** Create files in specified formats

## Contributing 🤝

We welcome contributions! Please follow these steps:

- Fork the repository

- Create a feature branch (git checkout -b feature/AmazingFeature)

- Commit your changes (git commit -m 'Add AmazingFeature')

- Push to the branch (git push origin feature/AmazingFeature)

- Open a Pull Request

## Development Setup:
```bash
git clone https://github.com/yourusername/scanned-pdf-to-text.git
cd scanned-pdf-to-text
pip install -e .[dev]
pre-commit install
```
## Roadmap 🗺️

1. [x] PDF/A compliance support

2. [x] Table recognition and formatting

3. [x] Handwriting recognition support

4. [x] Docker containerization

5. [x] Web interface (Flask/Django)

6. [x] Automated quality assessment

7. [x] Zonal OCR templates

8. [x] Benchmarking suite

9. [x] Troubleshooting 🔧

## Common Issues:

- Tesseract Not Found:

   * Verify installation path

   * Add Tesseract to system PATH

- Poor OCR Results:

   * Use higher quality scans

   * Experiment with preprocessing options

   * Try different language packs

## License 📄

This project is licensed under the GNU General Public License v3.0 - see LICENSE file for details.
Acknowledgements 🙏