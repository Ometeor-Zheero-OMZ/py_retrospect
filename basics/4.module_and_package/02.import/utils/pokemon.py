Pokemon = dict[str, str|int|bool]

def get_pokemon(id: int|None, name: str|None, skill: str|None) -> Pokemon|None:
    return { "id": id, "name": name, "skill": skill }
