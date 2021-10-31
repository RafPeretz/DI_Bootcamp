# Exercise 1: Cats
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def oldest_cat(cat_list):
    cat = sorted(cat_list, key=lambda cat: cat.age)[-1]
    return cat


# for cat in cat_list:
#     max([cat.age for cat in cat_list])
#     age = 0
#     for cat in cat_list:
#


def oldest_longer(cat_list):
    age = cat_list[0].age
    current_cat = cat_list[0]
    for cat in cat_list:
        if cat.age > age:
            current_cat = cat
    return current_cat


cat1 = Cat('Rex', 34)
cat2 = Cat('mr bubbles', 12)
cat3 = Cat('meowscules', 80)

data_list = [('Rex', 34), ('mr bubbles', 12), ('meowscules', 80)]

cats = [Cat(*data) for data in data_list]
oldest = oldest_cat(cats)
print(oldest.name, oldest.age)


# Exercise 2 : Dogs
class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f'{self.name} goes woof')

    def jump(self):
        x = self.height * 2
        print(f'{self.name} jump {x} cm high !')


davids_dog = Dog('Rex', 50)
davids_dog.bark()
davids_dog.jump()

sarah_dog = Dog('Teacup', 20)
sarah_dog.bark()
sarah_dog.jump()

if davids_dog.height > sarah_dog.height:
    print(davids_dog.height)

else:
    print(sarah_dog.height)


# Exercise 3 : Who’s The Song Producer?
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for parole in self.lyrics:
            print(parole)


stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

#Exercise 4 : Afternoon At The Zoo

from itertools import groupby

class Zoo:
    def __init__(self,zoo_name,animals,name):
        self.zoo_name = zoo_name
        self.animals = animals
        self.name = name

    def add_animal(self,new_animal):
        self.animals.append(new_animal)

    def get_animals(self):
        for animal in self.animals:
            print(animal)

    def sell_animal(self,animal_sold):
        for animal in self.animals:
            if animal == animal_sold:
                self.animals.remove(animal_sold)

    def sort_animals(self):
        sorted_list = sorted(self.animals)
        [list(g) for k, g in groupby(sorted_list, key=lambda x: x[0])]

    def get_groups(self):
        list = self.sort_animals()
        for elememt in list:
            print(elememt)


ramat_gan_safari  = Zoo('Ramat Gan Zoo', ['Girafe','Panda','Cats'],['Rexi','Willian','Sam'])
ramat_gan_safari.add_animal('Lion')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Girafe')
ramat_gan_safari.get_animals()
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()





