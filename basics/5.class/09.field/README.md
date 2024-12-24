#### クラス変数（フィールド）

```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.species}: called {self.name}")

person1 = Person("Jim")
# Homo sapiens: called Jim
person1.print_info()

person2 = Person("Henry")
# Homo sapiens: called Henry
person2.print_info()
```

#### ジェネリクスを使用して作ろう

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Vec(Generic[T]):
    _version = "0.6.2"

    def __init__(self):
        self.elems: list[T] = []

    def push(self, elem: T) -> None:
        self.elems.append(elem)

    def remove(self, idx: int) -> None:
        if 0 <= idx < len(self.elems):
            del self.elems[idx]
        else:
            raise IndexError("Index out of range.")

    def version_info(self):
        print(f"The version {self._version} now.")

v = Vec()
v.push('c')
v.push('h')
v.push('u')
v.push('n')
v.push('k')
# ['c', 'h', 'u', 'n', 'k']
print(v.elems)

v.remove(2)
# ['c', 'h', 'n', 'k']
print(v.elems)

# The version 0.6.2 now.
v.version_info()
```
