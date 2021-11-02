# Exercise 1 : Pets
class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sphynx(Cat):
    def sing(self, sounds):
        return f'{sounds}'


pet = Pets(["Girafe", "Raf"])
print(pet.animals)

cat1 = Sphynx('Egypt', 4)
cat2 = Chartreux('Sam', 7)
cat3 = Bengal("Bengal", 3)

cats = [cat1, cat2, cat3]

for cat in cats:
    cat.walk()

my_pets = Pets(cats)
my_pets.walk()

# Exercise 2 : Dogs
class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f'{self.name} is barking')

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        run_speed1 = self.run_speed() * self.weight
        run_speed2 = other_dog.run_speed() * other_dog.weight

        if run_speed1 > run_speed2:
            print(f'the winner is {self.name}')
        else:
            print(f'the winner is {other_dog.name}')


dog1 =  Dog('Rex',2,12)
dog2 =  Dog('Prada',10,8)
dog3 =  Dog('Coco',5,7)

