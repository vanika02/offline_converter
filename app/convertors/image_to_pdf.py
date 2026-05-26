from PIL import Image
import img2pdf
import os


# img = PIL.Image.open("pic.jpg").convert("RGB")
# img.save("out.pdf", save_all=True)

# storing image path
img_path = "/mnt/c/Users/Prans/Downloads/img.jpeg"
# print(img_path)

# storing pdf path
pdf_path = "/mnt/c/Users/Prans/Downloads/imgzz.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file 
file = open(pdf_path, "wb")

# writing pdf files with chunks 
file.write(pdf_bytes)

# closing image file 
image.close()

# closing pdf file 
file.close()

# output
print("Successfully made pdf file")

