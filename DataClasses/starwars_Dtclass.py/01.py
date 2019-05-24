import requests

response = requests.get('https://swapi.co/api/films/1/')
dictionary = response.json()
