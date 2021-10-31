import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        self.radius / 2 * math.pi

    def area(self):
        return self.radius ** 2 * math.pi

    def definiton(self):
        print(
            "A circle is a shape consisting of all points in a plane that are at a given distance from a given point, the centre; equivalently it is the curve traced out by a point that moves in a plane so that its distance from a given point is constant.")


circle = Circle(2)
print(circle.radius)
print(circle.area())
print(circle.perimeter())
circle2 = Circle(4)
print(circle2.radius)
print(circle2.area())
print(circle2.perimeter())
circle2.definiton()
