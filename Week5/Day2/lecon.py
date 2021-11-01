class Animal():
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def bark(self):
        print("{} barked, WAF !".format(self.name))


animal = Animal('Frog')
animal2 = Animal('Frog')
dog1 = Dog('Sparky')
dog1.bark()

import random
class Door:
    def __init__(self):
        self.is_opened = random.choice([False,True])

    def open_door(self):
        self.is_opened = True

    def close_door(self):
        self.is_opened = False

class BlockedDoor(Door):
    def open_door(self):
        print('a blocked door cannnot be opened or closed.')

    def close_door(self):
        self.open_door()

door = Door()
bdoor = BlockedDoor()

door.open_door()


