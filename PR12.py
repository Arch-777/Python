# Practical 12

class A:
    def fun(self):
        print("Hello")


class B(A):
    def fun2(self):
        print("world")


class C:
    def fun3(self):
        print("Multiple")


class D(B, C):
    def fun4(self):
        print("Derived Class")


obj = D()
obj.fun()
obj.fun2()
obj.fun3()
obj.fun4()
