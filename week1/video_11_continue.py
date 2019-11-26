magicNumber = 20

for n in range(100):
    if n is magicNumber:
        print(n,"is the magic Number!")
        break
    else:
        print(n)


for n in range(101):
    if n % 4 == 0:
        print(n)