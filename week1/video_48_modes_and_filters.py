from PIL import Image
from PIL import ImageFilter
born = Image.open('born.jpg')
black_and_white = born.convert('L')

black_and_white.show()

three_62 = Image.open('362.jpg')
blur = three_62.filter(ImageFilter.BLUR)
detail = three_62.filter(ImageFilter.DETAIL)
edges = three_62.filter(ImageFilter.FIND_EDGES)


blur.show()
detail.show()
edges.show()