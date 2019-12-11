user_inps = list(input(" Enter any sentence  :"))
length = len(user_inps)

for user_inp in user_inps:
    print(user_inp)
print('\n')
charac = 0
while charac < length:
    print(user_inps[charac])
    charac += 1