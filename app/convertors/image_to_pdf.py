from PIL import Image
import img2pdf
# import os

def convert_image_to_pdf(img_path, pdf_path):
    image = Image.open(img_path)
    pdf_bytes - img2pdf.convert(image.filename)

    with open(pdf_path, "wb") as file:
        file.write(pdf_bytes)

    image.close()

    return True

