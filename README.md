# PDF Page Extractor

This repository contains a simple Python script to extract specific pages from a PDF file using the `PyPDF2` library. 

## Features

- Extract a range of pages from a PDF file.
- Save the extracted pages as a new PDF file.

## Requirements

- Python 3.x
- PyPDF2 library

## Installation

First, ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

Next, install the `PyPDF2` library using pip:

```bash
pip install PyPDF2
```

## Usage

1. Clone this repository or download the script directly.

2. Modify the script with your desired input PDF path, output PDF path, and the range of pages you want to extract:

```python
input_pdf_path = '/path/to/your/input.pdf'
output_pdf_path = '/path/to/your/output.pdf'
start_page = 32  # Replace with your desired start page
end_page = 33    # Replace with your desired end page
```

3. Run the script:

```bash
python pdf_cutter.py
```

## Example

By default, the script is set to extract pages 32 and 33 from a sample PDF:

```python
input_pdf_path = '/Users/ilo-bst/Documents/Calculus-9th-Edition-by-Ron-Larson-Bruce-H.-Edwards.pdf'
output_pdf_path = '/Users/ilo-bst/Documents/math_pdfs/pages_32_33.pdf'
start_page = 32
end_page = 33
```

You can modify these variables to suit your needs.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
