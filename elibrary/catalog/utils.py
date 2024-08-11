import fitz

def extract_cover_image(pdf_path, image_path):
    pdf_document = fitz.open(pdf_path)
    
    first_page = pdf_document.load_page(0)
    
    pix = first_page.get_pixmap()
    
    pix.save(image_path)
    
    pdf_document.close()

extract_cover_image('example.pdf', 'cover_image.png')
