###########
# 関数定義 #
###########
from typing import Optional

def sqrt(x: int) -> Optional[int]:
    if x <= 0:
        return

    return x ** 2

result: Optional[int] = sqrt(3)
# 9
print(result)

###############################
# Enumとmatchガードを使った関数 #
###############################
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

########################################
# 位置引数・キーワード引数・デフォルト引数 #
########################################

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

#################################################
# デフォルト引数で設定する空のリストは参照渡しになる #
#################################################
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

###############################################################
# 新しいリストを作成する場合はデフォルト引数に None を設定すること #
###############################################################
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

#####################
# 位置引数のタプル化 #
#####################
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

########################
# キーワード引数の辞書化 #
########################
def menu(**kwargs):
    # {'entree': 'beef', 'drink': 'coffee'}
    print(kwargs)

    for k, v in kwargs.items():
        """
        entree beef
        drink coffee
        """
        print(k, v)

menu(entree="beef", drink="coffee")

d = {
    "entree": "pork",
    "drink": "iced coffee",
    "dessert": "melon"
}

menu(**d)