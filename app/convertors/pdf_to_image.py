from PIL import Image
from pdf2image import convert_from_path

def convert_pdf_to_image(pdf_path, img_path)
    pdf = Image.open(pdf_path)
    image_bytes = convert_from_path(pdf.filename)

    with open(img_path, "wb") as file:
        file.write(image_bytes)
    
    image.close()

    return True