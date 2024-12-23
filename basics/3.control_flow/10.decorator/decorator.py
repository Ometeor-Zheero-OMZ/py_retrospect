def print_info(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        print("START")
        result = func(*args, **kwargs)
        print("END")
        return result
    return wrapper

@print_info
def add_num(a, b):
    return a + b

f = add_num(10, 20)
"""
(10, 20) {}
START
END
30
"""
print(f)

###############################
# 自分なりやってみよう（ロガー） #
###############################
from typing import Callable

User = dict[str, str | int]

def logger(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"Elements: {args}")
        print(f"Dict Elements: {kwargs}")

        return func(*args, **kwargs)
    return wrapper

@logger
def create_user(id: int | None, name: str | None, age: int | None, gender: str | None) -> User | None:
    if id is None or name is None or age is None or gender is None:
        return None
    
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    return {"id": id, "name": name, "age": age, "gender": gender}

func = create_user(1, "Alice", 20, "female")
print(func)

"""
Elements: (1, 'Alice', 20, 'female')
Dict Elements: {}
{'id': 1, 'name': 'Alice', 'age': 20, 'gender': 'female'}
"""