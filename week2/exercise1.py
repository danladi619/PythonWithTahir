message = "keep moving and don't stop"

print(message.capitalize())
print(message.casefold())
print(message.center(20,'!'))
print(message.count('o'))
print(message.endswith(" "))
print(message.find('e'))
print(message.index('t'))
alpha_num = '123456xyz'

print(alpha_num.isalnum())
print(alpha_num.isalpha())
print(alpha_num.isascii())
print(alpha_num.isdecimal())
print(alpha_num.isdigit())
print(message.islower())
print(message.istitle())

up_low_case = "Don't Believe Everything They Say"
print(up_low_case.lower())
print(up_low_case.replace('Everything', 'Somethings'))
print(message.rfind('t'))

space_text = '  This is a space text  '
print(space_text.rsplit())
print(space_text.rstrip())
print(message.startswith('k'))
print(space_text.split())
print(space_text.lstrip())
print(space_text.strip())
print(space_text.title())
print(up_low_case.swapcase())
