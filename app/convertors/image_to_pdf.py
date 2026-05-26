from PIL import Image

img = PIL.Image.open("pic.jpg").convert("RGB")
img.save("out.pdf", save_all=True)