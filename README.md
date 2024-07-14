#  PDF page extractor

## Overview

This repository contains two Python scripts designed to manipulate PDF files. The first script, `pdf_splitter.py`, extracts specific pages from a PDF and saves them as a new PDF. The second script, `pdf2png_splitter.py`, splits each page of a PDF into four quadrant images and saves them as PNG files.

## Scripts

### 1. pdf_splitter.py

#### Description

`pdf_splitter.py` is a script that extracts specific pages from an input PDF file and saves them into a new PDF file. The script uses the `PyPDF2` library for PDF manipulation.

#### Usage

```sh
python pdf_splitter.py <input_pdf_path> <output_pdf_path> <start_page> <end_page>
```

#### Arguments

- `input_pdf_path`: Path to the input PDF file.
- `output_pdf_path`: Path to save the extracted PDF pages. If this is a directory, a default filename will be created.
- `start_page`: The start page number (1-based index).
- `end_page`: The end page number (1-based index).

#### Example

```sh
python pdf_splitter.py example.pdf extracted_pages.pdf 1 5
```

This command extracts pages 1 to 5 from `example.pdf` and saves them as `extracted_pages.pdf`.

### 2. pdf2png_splitter.py

#### Description

`pdf2png_splitter.py` is a script that splits each page of a PDF into four quadrant images and saves them as PNG files. The script uses the `PyMuPDF` (`fitz`) library for PDF manipulation and the `PIL` (Pillow) library for image processing.

#### Usage

```sh
python pdf2png_splitter.py <pdf_path> <output_dir> [--zoom <zoom_factor>]
```

#### Arguments

- `pdf_path`: Path to the input PDF file.
- `output_dir`: Directory to save the output PNG images.
- `--zoom`: Optional. Zoom factor to improve image quality. Default is 2.0.

#### Example

```sh
python pdf2png_splitter.py example.pdf output_images --zoom 3.0
```

This command splits each page of `example.pdf` into four quadrant images with a zoom factor of 3.0, saving the images in the `output_images` directory.

## Dependencies

Both scripts require Python 3 and the following Python libraries:

- `PyPDF2` for `pdf_splitter.py`
- `fitz` (PyMuPDF) and `PIL` (Pillow) for `pdf2png_splitter.py`

You can install the dependencies using pip:

```sh
pip install PyPDF2 PyMuPDF Pillow
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [PyPDF2](https://github.com/mstamy2/PyPDF2)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [Pillow](https://python-pillow.org/)

