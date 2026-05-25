import keyword
all_keyy = keyword.kwlist
print(all_keyy)
print(len(all_keyy))


soft_key = keyword.softkwlist
print(soft_key)

import string

lower_case = string.ascii_lowercase
print(len(lower_case))

upper_case = string.ascii_uppercase
print(upper_case)

total = lower_case+upper_case
print(len(total))


digits = string.digits
print(len(digits))

print(string.hexdigits)
print(string.octdigits)


print(string.punctuation)
print(string.printable)

# a = 3
# b = 5.9
# print(a+b)

# a = "9"
# c= int(a)
# b = 9
# print(a+b)

print("Welcome to Python")
print("My name is Ruchi")
print("I will become a Python developer")

print("\n======= MY INTORDUCTION =======")
print("Name: Ruchi")
print("City: Bhopal")
print("Goal: Data Analyst")
print("Skill:Python")
print("=================================")