#### 特殊メソッド (Magic Method)

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Vec(Generic[T]):
    _version: str = "0.6.2"

    def __init__(self):
        self.elems: list[T] = []

    def push(self, elem: T) -> None:
        self.elems.append(elem)

    def remove(self, idx: int) -> None:
        if 0 <= idx < len(self.elems):
            del self.elems[idx]
        else:
            raise IndexError("Index out of range.")

    @classmethod
    def version_info(cls):
        print(f"{cls.__name__} is now {cls._version}")

    @staticmethod
    def is_empty(elems: list[T]) -> bool:
        return len(elems) == 0

    # アドレスの代わりに文字列を返す
    def __str__(self):
        return "Vec is a dynamic list allows you for any elements inserted into"

    # サイズを図ることができる
    def __len__(self):
        return len(self.elems)

v = Vec()

# True
print(v.is_empty([]))

v.push('c')
v.push('h')
v.push('u')
v.push('n')
v.push('k')
# ['c', 'h', 'u', 'n', 'k']
print(v.elems)

# False
print(v.is_empty(v.elems))

v.remove(2)
# ['c', 'h', 'n', 'k']
print(v.elems)

# Vec is now 0.6.2
v.version_info()

# 4
print(len(v))

# Vec is a dynamic list allows you for any elements inserted into
print(v)
```
