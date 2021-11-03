import json
from faker import Faker

fake = Faker()

with open('file.json', 'r') as f:
    family = json.load(f)

print('janes children:')

for child in family['children']:
    child['favorite_color'] = fake.color()
    for key, value in child.items():
        print(f'my {key} is {value}')


with open('file.json', 'w') as f:
    json.dump(family, f, indent=2)

