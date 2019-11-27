from PIL import Image

three_62 = Image.open('362.jpg')
born = Image.open('born.jpg')

area = (20, 20, 295,203)
born.paste(three_62, area)

born.show()
