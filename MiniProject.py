first = input("Enter First Number : ")
operator = input("Enter Operator (+,_,*,/,%) : ")
second = input("Enter Second Number : ")
first = int(first)
second = int(second)
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operator")
