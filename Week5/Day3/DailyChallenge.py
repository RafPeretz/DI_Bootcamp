import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        pi = math.pi
        area = pi * self.radius ** 2

    def print_circle(self):
        print(""""
        
                  ***  
                 *   * 
                *     *
                *     *
                *     *
                 *   * 
                  ***

        """)

    def __add__(self, other):
        if isinstance(other, int):
            self.radius += other
            print(self.amount)

        elif isinstance(other, float):
            self.radius += other
            print(self.amount)

        else:
            self.radius += other.radius
            print(self.radius)

    def __eq__(self, other):
        if (isinstance(other, Circle)):
            if self.radius > other.radius:
                print("First circle is bigger")
            elif self.radius < other.radius:
                print("Second Cercle is bigger")
            else:
                print("The are the same")


circle = Circle(2)
circle.print_circle()

list = [Circle(6), Circle(4), Circle(9), Circle(4), Circle(10), Circle(3), Circle(6)]
new_list = sorted(list, key=lambda x: x.radius)
print(newlist[0])
