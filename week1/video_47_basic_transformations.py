from PIL import Image

born = Image.open('born.jpg')
square_born = born.resize((250, 250))
flip_born = born.transpose(Image.FLIP_LEFT_RIGHT)
spin_born = born.transpose(Image.ROTATE_90)

born.show()
square_born.show()
flip_born.show()
spin_born.show()