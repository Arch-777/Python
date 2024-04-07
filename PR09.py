# Practical 9

# 1
import math


def circle(r):
    p = math.pi
    area = p*r**2
    circum = 2*p*r
    print("Area - ", area, " Circumference - ", circum)


circle(4)

# 2
import calendar


yyyy = 2024
mm = 3
print(calendar.month(yyyy, mm))
