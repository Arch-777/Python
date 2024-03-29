class Area:
    def rec(self,  height, width):
        return "Area of Rectangle - ", height * width

    def squ(self, side):
        return "Area of Square - ", side * side


Obj = Area()
print(Obj.rec(4, 6))
print(Obj.squ(4))
