import decimal
import random

#Exercise1
# my_fav_numbers = set()
#
# my_fav_numbers = {1,2,3,4,5}
# my_fav_numbers.add(6)
# my_fav_numbers.add(7)
# my_fav_numbers.remove(7)
#
# print(my_fav_numbers)
#
# friend_fav_numbers = set()
# friend_fav_numbers = {6,44,1,55}
#
# our_fav_numbers = set.union(my_fav_numbers, friend_fav_numbers)
# print(our_fav_numbers)
#
# #Exercise2
# #Tuples are immutable and not supposed to be changed - that is what the list type is for.
# #However, you can replace each tuple using originalTuple + (newElement,), thus creating a new tuple.
# #so NO its not possible
#
# #Exercise3
#
# for i in range(1,21):
#     print(i)
#
# #Exercise4
#
# #float is the type for decimal number that there is point after the number
# x = random.random()
# # Random float number
# for i in range(5):
#     print(random.random())
#
#
# #Exercise5
#
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.remove("Banana")
# basket.pop()
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# count = 0
#
# for fruit in basket:
#    if fruit == "Apples":
#        count+=1
#        break
#
#
# for fruitss in basket:
#     basket.pop()
#
# #Exercise6
#
# name = ''
#
# while(name != 'Rafael'):
#     name = input('What is your name ')
#
# print("We have the same name")
#
#
# #Exercise 7
#
# list = ["Banana", "Apples", "Oranges", "Blueberries"]
#
# for i in range(len(list)):
#
#     if(i%2==0):
#         print(list[i])
#
#
# #Exercise 8
#
# for i in range(1500,2500):
#     if(i%5==0 or i%7==0):
#         print(i)
#
#
# #Exercise 9: Favorite Fruits
#
# favorite_fruits = input('Enter youre favorite fruit plese separe by space ')
# print("\n")
#
# user_list = favorite_fruits.split()
#
# print('list: ', user_list)
#
# inputs_fruit = input('Please enter a fruits')
#
# for index in user_list:
#     if(index==inputs_fruit):
#         print("You chose one of your favorite fruits! Enjoy!")
#     else:
#         print("You chose a new fruit. I hope you enjoy")
#
# #Exercise 10:Who Ordered A Pizza
# sum=10
# topping = ''
# while(topping !=' quit'):
#     topping = input('Please add a topping ifyou dont want topping; Please write quit')
#     print("You will add ", topping,"to your pizaza")
#     sum+=2.5
#
#
# print("you have to pay", sum)
#


#Exercise 11: Cinemax
family_total = 0
input_ages = input('Enter the age of each menber of the family separated by space')
age_list = input_ages.split()

for i in range(len(age_list)):
    # convert each item to int type
    age_list[i] = int(age_list[i])

print(age_list)

for age in age_list:
    if age > 3 and age < 12:
        family_total+=10
    elif age>=12:
        family_total+=15

print(family_total)

#Exercise 12 : Who Is Under 16?

new_list = []
list = ["Sam","Noe","Salome","Ben"]
age = ''

for x in list:
    age = int(input('Hey Please enter youre age'))
    if age>16 and age<21:
        new_list.append(x)
    break

    print(new_list)


#Exercise13

    sandwich_orders = ["thon", "mozarella", "saumon"]
    finished_sandwiches = []
    finished_sandwiches = sandwich_orders.pop(0)
    print(sandwich_orders)
    print(finished_sandwiches)

#Exercise14

    sandwich_orders = ["pastrami", "thon", "pastrami", "tomate", "salade", "pastrami"]
    count = 0
    while "pastrami" in sandwich_orders:
        if ("pastrami" == sandwich_orders[count]):
            sandwich_orders.pop(count)
        count += 1
    print(sandwich_orders)