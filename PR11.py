# Practical 11
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


# Example usage
rectangle = Rectangle(5, 4)
circle = Circle(3)

print("Rectangle area:", rectangle.area())
print("Circle area:", circle.area())

try:
    shape = Shape()
    shape.area()
except NotImplementedError as e:
    print(e)
