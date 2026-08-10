# How to connect to an API using Python
# DownLoad request module --> pip install requests

import requests
# requests Python ki library hai jo HTTP requests bhejne ke kaam aati hai.
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url) #API ko request bhejta hai.
    # print(response) #<Response [200]> You will get the status code.
    
    if response.status_code==200:
        pokemon_data=response.json() #response.json() is JSON data ko Python object, usually dictionary, me convert karta hai.
        # print(pokemon_data) #will give full api in json format
        return pokemon_data
    else:
        print(f"SomeThing Went Wrong {response.status_code}")

pokemon_name = input("Enter the pokemon name about which you want to know: ")
pokemon_info = get_pokemon_info(pokemon_name)
if pokemon_info :
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id:{pokemon_info["id"]}")
    print(f"Height:{pokemon_info["height"]}")
    print(f"Weight:{pokemon_info["weight"]}")

