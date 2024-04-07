# Practical 7

# 1
def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


input_string = input("Enter a string: ")
upper, lower = count_case(input_string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)

# 2
string = "Hello, World!"

print("Original String:", string)
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())
print("Capitalized:", string.capitalize())
print("Titlecased:", string.title())
print("Reversed:", string[::-1])
print("Split by comma:", string.split(","))


# 3

import math
number = 25
print("Square root:", math.sqrt(number))
print("Absolute value:", abs(-5))
print("Ceiling:", math.ceil(3.7))
print("Floor:", math.floor(3.7))
print("Power:", math.pow(2, 3))
print("Pi constant:", math.pi)