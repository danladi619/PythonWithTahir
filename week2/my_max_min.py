def my_max(user_inputs):
    length = len(user_inputs)
    is_max = user_inputs[0]

    for i in range(length):
        if is_max < user_inputs[i]:
            is_max = user_inputs[i]
            i+1

    print(f"The maximum number is {is_max}")


def my_min(user_inputs):
    length = len(user_inputs)
    is_min = user_inputs[0]

    for i in range(length):
        if is_min > user_inputs[i]:
            is_max = user_inputs[i]
            i + 1

    print(f"The minimum number is {is_min}")


input_list = []

while True:
    value = input("Enter inputs ('.' to end): ")
    if value == '.':
        break
    else:
        input_list.append(value)

my_max(input_list)

