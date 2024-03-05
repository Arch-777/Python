import math


def circle(r):
    p = math.pi
    area = p*r**2
    circum = 2*p*r
    print("Area - ", area, " Circumference - ", circum)


circle(4)
