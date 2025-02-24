import requests

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data

def print_pokemon_info(pokemon_data):
    name = pokemon_data['name']
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    print(f"Name: {name}")
    print("Abilities:")
    for ability in abilities:
        print(f"- {ability}")

def calculate_average_weight(pokemon_data_list):
    total_weight = 0
    for pokemon_data in pokemon_data_list:
        total_weight += pokemon_data['weight']
    average_weight = total_weight / len(pokemon_data_list)
    return average_weight

# Example usage
pokemon_data_list = [{'name': 'Pikachu', 'weight': 60}, {'name': 'Bulbasaur', 'weight': 69}]
average_weight = calculate_average_weight(pokemon_data_list)
print(average_weight)
