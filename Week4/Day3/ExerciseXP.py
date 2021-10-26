#Exercise 1 : Convert Lists Into Dictionaries

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

num_dict ={keys[0]:values[0],
           keys[1]:values[1],
           keys[2]:values[2]

           }

print(num_dict)

#Exercise 2 : Cinemax #2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
family_total= 0
for member in family:
    if family[member] > 3 and family[member] < 12:
        family_total+=10
        print(f"{member} has to pay 10$")
    elif family[member]>=12:
        family_total+=15
        print(f"{member} have to pay 15$")


print(f"family total cost will be {family_total} $")

#Exercise 3: Zara

brand = {
'name': 'Zara' ,
'creation_date': 1975 ,
'creator_name': 'Amancio Ortega Gaona' ,
'type_of_clothes': ['men', 'women', 'children', 'home' ],
'international_competitors': ['Gap', 'H&M', 'Benetton'] ,
'number_stores': 7000 ,
'major_color':
{ 'France': 'blue',
    'Spain': 'red',
    'US': ['pink', 'green']
}
}
print(brand)

brand["number_stores"] = 2
print(brand)

print(' \n Zara client are fashion lover that love good quality for cheap')

brand['country_creation '] = 'Spain'
print(brand)

for key in brand:
     if(key=='international_competitors'):
         brand[key].append('Desigual')


print(brand)

brand.pop('creation_date')
print('\n',brand)

print('\n',brand['international_competitors'][-1])

print('\n',brand['major_color']['US'])

print('\n',len(brand.keys()))

for key in brand:
    print(key)

more_on_zara = {
    'name':'Zara',
    'number_stores': 10000
}

brand.update(more_on_zara)

print(brand)

#Exercise 4 : Disney Characters

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

disney_users_A = {}

for index,values in enumerate(users):
    disney_users_A[values] = index

print(disney_users_A)

disney_users_B = {}

for index,values in enumerate(users):
    disney_users_B[index] = values

print(disney_users_B)

disney_users_C = {}

for index,values in enumerate(users):
    disney_users_C[values] = index

sorted_keys = disney_users_C.items()
new_values = sorted(sorted_keys)
print(new_values)

