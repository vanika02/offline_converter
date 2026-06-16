from PIL import Image
from pdf2image import convert_from_path

def convert_pdf_to_image(pdf_path, img_path):
    image = convert_from_path(pdf_path)

    image[0].save(img_path)

    return True

def get_pdf_file():
    return file