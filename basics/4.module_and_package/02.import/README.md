#### import の仕方

```python
import utils.pokemon
```

```python
from utils import pokemon
```

```python
from utils import pokemon as poke

id = 1
name = "Metagross"
skill = "Psycho Fang"

pokemon = poke.get_pokemon(id, name, skill)
print(pokemon)
```
