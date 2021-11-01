# Exercise 1 : Family
class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **kwargs):
        self.members.append(kwargs)

    def is_18(self, name):

        self.name_check = name
        for key in self.members:
            if self.name_check == key["name"]:
                if i['age'] >= 18:
                    return True
            else:
                return False

    def print_member(self):
        print(self.members)


family = Family([
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False},
], "Peretz")

#Exercise 2 : TheIncredibles Family

class TheIncredibles(family):

    def use_power(self):
        print("hey")

