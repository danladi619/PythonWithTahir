from PIL import Image

img = Image.open('362.jpg')

area = (50, 50, 200, 150)
cropped_image = img.crop(area)

img.show()
cropped_image.show()

