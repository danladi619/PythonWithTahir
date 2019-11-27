from PIL import Image

three_62 = Image.open('362.jpg')
born = Image.open('born.jpg')

r1, g1 ,b1 = three_62.split()
r2, g2, b2 = born.split()

new_img = Image.merge('RGB',(r2,g1,b2))

new_img.shoe()