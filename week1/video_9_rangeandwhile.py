numbersTaken = [1,2,5,7,8]

print("Here are the available numbers")

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)