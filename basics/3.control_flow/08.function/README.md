#### 関数定義
```python
from typing import Optional

def sqrt(x: int) -> Optional[int]:
    if x <= 0:
        return

    return x ** 2

result: Optional[int] = sqrt(3)
# 9
print(result)
```

#### Enumとmatchガードを使う
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BROWN = 3

def pick_coffee(color) -> str:
    match color:
        case Color.RED:
            return "High Brand coffee"
        case Color.GREEN:
            return "Resonable Brand coffee"
        case Color.BROWN:
            return "Cheap Brand coffee"
        case _:
            print("Not be sold")

picked: str = pick_coffee(Color.RED)
# You got a High Brand coffee!
print(f"You got a {picked}!")
```

#### 位置引数・キーワード引数・デフォルト引数
```python
User = dict[str, str | int]
def create_user(name="test_user", age=18, gender="unknown") -> User | None:
    # null チェック
    if name is None or age is None or gender is None:
        raise ValueError("All arguments must be non-null.")
    
    # 整数チェック
    if not isinstance(age, int):
        raise TypeError("Age mut be an integer.")
    
    return {"name": name, "age": age, "gender": gender}

user = create_user("OMZ", 20, "male")
# {'name': 'OMZ', 'age': 20, 'gender': 'male'}
print(user)
```

#### デフォルト引数で設定する空のリストは参照渡しになる
```python
def get_list(x, vec=[]):
    vec.append(x)
    return vec

result = get_list(10, [1, 2])
# [1, 2, 10]
print(result)

result = get_list(10)
# [10]
print(result)

result = get_list(20)
# [10, 20]
print(result)
```

#### 新しいリストを作成する場合はデフォルト引数に None を設定すること
```python
def get_list(x, vec=None):
    if vec is None:
        vec = []
    vec.append(x)
    return vec

result = get_list(10)
# [10]
print(result)

result = get_list(20)
# [20]
print(result)
```

#### 位置引数のタプル化
```python
def say_something(*args):
    # ('name', 'age', 'gender')
    print(args)

    for idx, arg in enumerate(args):
        """
        0 name
        1 age
        2 gender
        """
        print(idx, arg)

say_something("name", "age", "gender")
```

```python
def print_object(id, *args):
    if id != 1:
        return None
    
    print(id)

    for arg in args:
        """
        1
        name
        age
        """
        print(arg)

print_object(1, "name", "age")
```

#### キーワード引数の辞書化
```python
def menu(**kwargs):
    # {'entree': 'beef', 'drink': 'coffee'}
    print(kwargs)

    for k, v in kwargs.items():
        """
        entree beef
        drink coffee
        """
        print(k, v)

"""
entree beef
drink coffee
"""
menu(entree="beef", drink="coffee")

d = {
    "entree": "pork",
    "drink": "iced coffee",
    "dessert": "melon"
}

"""
entree beef
drink coffee
dessert melon
"""

menu(**d)
```

#### 関数内関数
```python
def print_out(a, b):

    def add(c, d):
        return c + d
    
    r = add(a, b)
    # 3
    print(r)

print_out(1, 2)
```

#### 関数の引数と戻り値の型指定
```python
def greet(name: str) -> str:
    return f"Hello, {name}"

# Hello, James
print(greet("James"))
```

#### 変数の型ヒント
```python
age: int = 25

pi: float = 3.14

is_active: bool = True

names: list[str] = ["Alice", "Bob"]

# 25
print(age)
# 3.14
print(pi)
# True
print(is_active)
# ['Alice', 'Bob']
print(names)
```

#### コレクション型のヒント
```python
names: list[str] = ["Alice", "Bob"]

scores: dict[str, int] = {"Alice": 85, "Bob": 90}

tup: tuple[int, int, int] = (1, 2, 3)

num_set: set[int] = {1, 2, 3}

# ['Alice', 'Bob']
print(names)
# {'Alice': 85, 'Bob': 90}
print(scores)
# (1, 2, 3)
print(tup)
# {1, 2, 3}
print(num_set)
```

#### Union型
```python
def process(value: int | float) -> float:
    return value * 1.1

# 23.1
print(process(21))
# 14.190000000000001
print(process(12.9))
```

#### Optional型
```python
def find_user(user_id: int) -> dict[str, int | str | bool] | None:
    if user_id == 1:
        return {"id": 1, "name": "Alice", "admin": False}
    return None

# {'id': 1, 'name': 'Alice', 'admin': False}
print(find_user(1))
# None
print(find_user(2))
```

#### Callable型
```python
from typing import Callable

def operate(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

callback = lambda x, y: x + y
# 5
print(operate(callback, 2, 3))
```

#### 型エイリアス
```python
User = tuple[str, int]

users: list[User] = [("Alice", 25), ("Bob", 30)]

# [('Alice', 25), ('Bob', 30)]
print(users)
```