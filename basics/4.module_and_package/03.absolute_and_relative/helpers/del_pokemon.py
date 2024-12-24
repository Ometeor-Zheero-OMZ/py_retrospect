from models import pokemon

Pokemon = pokemon.Pokemon

def delete_pokemon(pokemon: Pokemon|None):
    pokemon.clear()