# practical 2

# 1
num = int(input("Enter a number - "))
if num % 2 == 0:
    print("Num is even")
else:
    print("Num is odd")

# 2
a, b, c = 1000, 220, 30
if a > b:
    if a > c:
        print("A is greater")
elif b > c:
    if b > a:
        print("B is greater")
else:
    print("C is greater")

# 3
num = int(input("Enter a num - "))
if num > 0:
    print("+ve")
elif num < 0:
    print("-ve")
else:
    print("zer0")

# 4
s1 = int(input("Subject 1 marks - "))
s2 = int(input("Subject 2 marks - "))
s3 = int(input("Subject 3 marks - "))
s4 = int(input("Subject 4 marks - "))
s5 = int(input("Subject 5 marks - "))
total = s1 + s2 + s3 + s4 + s5
per = total / 5
if per >= 75:
    print(per, "Distinction")
elif per >= 60:
    print(per, "First class")
elif per >= 40:
    print(per, "Just pass")
else:
    print("fail")
