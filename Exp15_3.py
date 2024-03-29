class Add:
    def Add(self, a, b):
        print(a + b)


class Mul:
    def Mul(self, a, b):
        print(a * b)


class Derived(Add, Mul):
    def Devide(self,a ,b):
        print(a/b)


d = Derived()
d.Add(10, 20)
d.Mul(10, 20)
d.Devide(10, 20)
