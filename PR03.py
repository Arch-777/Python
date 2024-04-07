# Practical 3

# 1
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# 2
a = 1234
rev = 0

while (a > 0):
    a = a % 10
    rev = rev * 10 + a
    s = a // 10

print(rev)


# 3
def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = 12345
print(getSum(n))

# 4
def is_palindrome(n):
    return str(n) == str(n)[::-1]


print(is_palindrome(121))  # True
print(is_palindrome(123))  # False

