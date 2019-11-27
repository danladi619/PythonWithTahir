from PIL import Image

born = Image.open('born.jpg')
print(born.mode)

r, g, b = born.split()

new_img = Image.merge('RGB', (b, g, r))
new_img.show()