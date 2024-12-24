from models import pokemon

Pokemon = pokemon.Pokemon

def get_pokemon(id: int|None, name: str|None, skill: str|None) -> Pokemon|None:
    return { "id": id, "name": name, "skill": skill }
