# Practical 1

# 1
a = int(input("Enter US dollar for conversion - "))
print("USD to IND - ", a * 83)

# 2
import math
num = int(input("Enter number to find out its Square Root - "))
print("Square root of entered num - ", math.sqrt(num))

# 3
a = 10
b = 20
area = a * b
print("Area of rectangle - ", area)

# 4
side = int(input("Enter the size of 1 side of Square - "))
print("Area - ", side**2)
print("Perimeter - ", side*4)

# 5
num1 = int(input("Enter first num - "))  # 10
num2 = int(input("Enter second num - "))  # 20
print("Num 1 before swap - ", num1)
print("Num 2 before swap - ", num2)
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("Num 1 after swap - ", num1)
print("Num 2 after swap - ", num2)

