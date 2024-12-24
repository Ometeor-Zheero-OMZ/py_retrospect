#### 絶対パス

```python
from utils import pokemon
from helpers import del_pokemon

id = 1
name = "Metagross"
skill = "Psycho Fang"

pokemon = pokemon.get_pokemon(id, name, skill)
# {'id': 1, 'name': 'Metagross', 'skill': 'Psycho Fang'}
print(pokemon)

del_pokemon.delete_pokemon(pokemon)
# {}
print(pokemon)
```

#### 新旧パッケージの読み込み

```python
try:
    from models import pokemon
except ImportError:
    from models.pokemon import Pokemon
```
