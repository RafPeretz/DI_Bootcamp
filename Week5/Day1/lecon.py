# class Dog():
#     def __init__(self,my_color,my_height):
#         self.legs = 4
#         self.color = my_color
#         self.height = my_height
#
#     def introduce(self):
#
#         my_str= print(f'this dog  has {self.legs} legs, is color {self.color} and heigh is {self.height}')
#
#         if not self.name:
#             print('this dog'+ my_str)
#
#         else:
#              print(f'this dog {self.name}' + my_str)
#
#
#
#
#     def add_name(self,name):
#         self.name= name
#
# # dog1 = Dog('Red',1.56)
# # print(dog1)
# # dog1.introduce()
# #
# #
# # dog2 = Dog('Blue',1.33)
# # dog2.introduce()
# #
# # dog2.add_name('Rex')
# # dog1.add_name('Roxanne')
# # dog1.introduce()
# # dog2.introduce()
#
#
# data = [('red',1.56),('blue',0.43)]
#
# my_dogs = [Dog(*val) for val in data]
# my_names = ['Sparky','Rex']
#
# # for dog,name in zip(my_dogs,my_names):
# #     dog.introduce()
# #     dog.add_name(name)
# #     dog.introduce
#
#
# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# first_person = Person("John", 36)
# people = [Person('Sam',18),Person('Jerry',43)]
#
# for person in people:
#   print(person.name)
#
# print(first_person.name)
# print(first_person.age)

# class Dog():
#   # Initializer / Instance Attributes
#   def __init__(self, name_of_the_dog):
#     print("A new dog has been initialized !")
#     print("His name is", name_of_the_dog)
#     self.name = name_of_the_dog
#
#   def bark(self):
#     print("{} barks ! WAF".format(self.name))
#
#   def walk(self,number_of_meter):
#     print(f'{self.name} walked ')
#
class Computer():

  def description(self, name):
    """
    This is a totally useless function
    """
    print("I am a computer, my name is", name)
    # Analyse the line below
    print(self)


mac_computer = Computer()
mac_computer.brand = "Apple"
print(mac_computer.brand)

dell_computer = Computer()

Computer.description(dell_computer, "Mark")
# IS THE SAME AS:
dell_computer.description("Mark")

dog1 = Dog('Rex')
print(dog1.name)
dog1.bark()
