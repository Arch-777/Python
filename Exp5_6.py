def reverse_number(n):
    reversed_number = 0
    while n > 0:
        remainder = n % 10
        reversed_number = (reversed_number * 10) + remainder
        n = n // 10
    return reversed_number


print(reverse_number(12345))
