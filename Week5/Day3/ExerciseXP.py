# Exercise 1 : Built-In Functions

class Number:
    """Hey this program is for fun"""

    def do_nothing(self):
        pass

    def __init__(self, number):
        self.number = number

    def __abs__(self):
        return 2 * self.number

    def __int__(self):
        return int(self.number)


print(Number.__doc__)


# Exercise 2: Currencies

class Currency:
    def __init__(self, monney_type, amount):
        self.monney_type = monney_type
        self.amount = amount

    def __str__(self):
        return f"{self.amount}  {self.monney_type}"

    def __int__(self):
        return int(self.amount)

    def __repr__(self):
        return f"{self.amount}  {self.monney_type}"

    def __add__(self, other):

        if isinstance(other, int):
            self.amount += other
            print(self.amount)
        elif isinstance(other, float):
            self.amount += other
            print(self.amount)
        else:
            if self.monney_type != other.monney_type:
                raise TypeError(f"Cannot add between Currency type{self.monney_type}  and {other.monney_type}")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))

c1 + 5
c1 + c2

print(c1)

c1 + c3
