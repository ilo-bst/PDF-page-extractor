import PyPDF2
import argparse
import os

def extract_pages(input_pdf_path, output_pdf_path, start_page, end_page):
    # If the output path is a directory, create a default filename
    if os.path.isdir(output_pdf_path):
        output_pdf_path = os.path.join(output_pdf_path, f'extracted_pages_{start_page}_to_{end_page}.pdf')
    
    with open(input_pdf_path, 'rb') as input_pdf_file:
        pdf_reader = PyPDF2.PdfReader(input_pdf_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Ensure the end_page is within the range of the PDF
        end_page = min(end_page, len(pdf_reader.pages))
        
        for page_num in range(start_page-1, end_page):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdf_writer.write(output_pdf_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract specific pages from a PDF.')
    parser.add_argument('input_pdf_path', type=str, help='Path to the input PDF file.')
    parser.add_argument('output_pdf_path', type=str, help='Path to save the extracted PDF pages.')
    parser.add_argument('start_page', type=int, help='Start page number (1-based).')
    parser.add_argument('end_page', type=int, help='End page number (1-based).')

    args = parser.parse_args()

    extract_pages(args.input_pdf_path, args.output_pdf_path, args.start_page, args.end_page)