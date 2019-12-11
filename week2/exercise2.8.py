fix_lists = (23,21,34,55,45)
length = len(fix_lists)
#int_val = 0
total = 0
while int_val < length:
    total += fix_lists[int_val]
    int_val += 1
print(total)
total = 0
for fix_list in fix_lists:
    total += fix_list
print(total)



var_list = []
var = int(input("Enter numbers to sum and 0 when you are done:  "))
var_list.append(var)
while var != 0:
    var = int(input("Enter numbers to sum and 0 when you are done:  "))
    var_list.append(var)
length = len(var_list)

int_val = 0
total = 0
while int_val < length:
    total += var_list[int_val]
    int_val += 1
print(total)
total = 0

for var_lis in var_list:
    total += var_lis
print(total)


