# import utils.pokemon
# from utils import pokemon
from utils import pokemon as poke

id = 1
name = "Metagross"
skill = "Psycho Fang"

pokemon = poke.get_pokemon(id, name, skill)
print(pokemon)