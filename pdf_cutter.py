import PyPDF2

def extract_pages(input_pdf_path, output_pdf_path, start_page, end_page):
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

input_pdf_path = '/Users/ilona/Documents/AIRI speech-to-latex/Datasets_new/Calculus-9th-Edition-by-Ron-Larson-Bruce-H.-Edwards.pdf'
output_pdf_path = 'math_pdfs/pages_32_33.pdf'
start_page = 32
end_page = 33

extract_pages(input_pdf_path, output_pdf_path, start_page, end_page)