############################
# 関数の引数と戻り値の型指定 #
############################
def greet(name: str) -> str:
    return f"Hello, {name}"

# Hello, James
print(greet("James"))

#################
# 変数の型ヒント #
#################
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

########################
# コレクション型のヒント #
########################
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

###########
# Union型 #
###########
def process(value: int | float) -> float:
    return value * 1.1

# 23.1
print(process(21))
# 14.190000000000001
print(process(12.9))

##############
# Optional型 #
##############
def find_user(user_id: int) -> dict[str, int | str | bool] | None:
    if user_id == 1:
        return {"id": 1, "name": "Alice", "admin": False}
    return None

# {'id': 1, 'name': 'Alice', 'admin': False}
print(find_user(1))
# None
print(find_user(2))

##############
# Callable型 #
##############
from typing import Callable

def operate(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

callback = lambda x, y: x + y
# 5
print(operate(callback, 2, 3))

###############
# 型エイリアス #
###############
User = tuple[str, int]

users: list[User] = [("Alice", 25), ("Bob", 30)]

# [('Alice', 25), ('Bob', 30)]
print(users)