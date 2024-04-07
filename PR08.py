# Practical 8

# 1

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


number = int(input("Enter a number: "))
if is_prime(number):
    print(number, "is prime.")
else:
    print(number, "is not prime.")


#2

def factorial(num):
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


number = int(input("Enter a number: "))
print("Factorial of", number, "is", factorial(number))


#3

def count_case(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


input_string = input("Enter a string: ")
upper, lower = count_case(input_string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
