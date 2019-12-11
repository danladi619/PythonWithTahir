first = int(input("Enter the starting number: "))
last = int(input("Enter the maximum number: "))
increment = int(input("Enter the increment number: "))

for num in range(first, last, increment):
    print(num)