import img2pdf
from PIL import Image

path = '/path/to/files'
images = [
    "image1.jpeg",
    "image2.jpeg"
]

for image_file in images:
    image = Image.open(path + image_file)
    pdf_bytes = img2pdf.convert(image.filename)
    file = open(path + image_file + ".PDF", "wb")
    file.write(pdf_bytes)
    image.close()
    file.close()

# output
print("Successfully made pdf file")
