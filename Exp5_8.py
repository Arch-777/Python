def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(is_palindrome(121))  # True
print(is_palindrome(123))  # False
