import fitz  # PyMuPDF
from PIL import Image
import os
import argparse

def split_pdf_to_images(pdf_path, output_dir, zoom_factor):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        mat = fitz.Matrix(zoom_factor, zoom_factor)  # Increase the resolution
        pix = page.get_pixmap(matrix=mat)

        # Convert pixmap to PIL Image
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Calculate the split points
        split_height = image.height // 2
        split_width = image.width // 2
        
        # Split the image into four quadrants
        upper_left = image.crop((0, 0, split_width, split_height))
        upper_right = image.crop((split_width, 0, image.width, split_height))
        lower_left = image.crop((0, split_height, split_width, image.height))
        lower_right = image.crop((split_width, split_height, image.width, image.height))
        
        # Save the quadrants as PNG files
        upper_left.save(os.path.join(output_dir, f"page_{page_num+1}_1.png"))
        upper_right.save(os.path.join(output_dir, f"page_{page_num+1}_2.png"))
        lower_left.save(os.path.join(output_dir, f"page_{page_num+1}_3.png"))
        lower_right.save(os.path.join(output_dir, f"page_{page_num+1}_4.png"))

    print(f"Images saved in directory: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split a PDF document into quarter-page PNG images.')
    parser.add_argument('pdf_path', type=str, help='Path to the input PDF file.')
    parser.add_argument('output_dir', type=str, help='Directory to save the output PNG images.')
    parser.add_argument('--zoom', type=float, default=2.0, help='Zoom factor to improve image quality (default is 2.0).')
    
    args = parser.parse_args()
    
    split_pdf_to_images(args.pdf_path, args.output_dir, args.zoom)