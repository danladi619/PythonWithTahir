from PIL import Image

img = Image.open("362.jpg")
print(img.size)
print(img.format)

img.show()