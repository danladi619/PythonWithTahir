numbersTaken = [3,5,4,12,19,20]

print("Here are the numbers still available")

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)