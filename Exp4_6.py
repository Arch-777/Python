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
