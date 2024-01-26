import random

fruits = ["banana", "Apple", "Orange"]
X, Y, Z = "Chicken", "Fish", "Eggs"
a = b = "Quantity - 5 "
x, y, z = fruits
print(x)
print(y)
print(z)
print(X)
print(Y)
print(Z)
print(X, " ", a)


def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)

print(random.randrange(1, 10))
