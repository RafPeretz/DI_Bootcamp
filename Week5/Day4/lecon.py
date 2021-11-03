import random

import requests

category_response = requests.get('https://api.chucknorris.io/jokes/categories')
if category_response.status_code == 200:
    categories = category_response.json()

category = categories[0]
params = {'category': category}
joke_response = requests.get(f'https://api.chucknorris.io/jokes/random', params=params)
if joke_response.status_code == 200:
    print(joke_response.json())