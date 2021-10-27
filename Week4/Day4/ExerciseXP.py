#Exercises XP #1
def display_message():
    print("Hello in this course I am learning how to code python.")

display_message()

#Exercise 2: What’s Your Favorite Book ?

def favorite_book():
    print("One of One of my favorite books is Alice in Wonderland")

favorite_book()

#Exercise 3 : Some Geography
def describe_city(city,country):
    print(f'{city} is in {country}')

describe_city('Marseille','France')

#Exercise 4 : Random

import random
random.random()

def throw_number(num):
    generate_number = random.randint(1,100)
    if num == generate_number:
        print('Sucess')

    else:
        print('Fail')

throw_number(1)

#Exercise 5 : Let’s Create Some Personalized Shirts !

def make_shirt(size ,text):
    size=['L','M','any size']
    text = ['I love python','Hey','Yo']

    print(f'the size of the t-shirt is {size} the text is "{text}".')

make_shirt('','')

#Exercise 6 : Magicians …
magicians_list = ["Voldemort" ,"Dumbledor","SiriusBlack"]

def show_magicians():
    for value in magicians_list:
        print(value)

show_magicians()

def show_magicians():
    for index, item in enumerate(magicians_list):
        item = item + ' The great'
        magicians_list[index] = item
        print(magicians_list)

show_magicians()