import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a32637f7a246cbbf84703155c071e81b'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}


body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "261424",
    "name" : "lukas",
    "photo_id": 2
}

body_pokeball = {
    "pokemon_id": "261424"
}

\

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)

print(response_create.text)

\

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)  

print(response_change.text)

\

response_pokeball = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)

print(response_pokeball.text)

