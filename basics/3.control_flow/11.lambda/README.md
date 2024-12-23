#### ラムダ
```python
l = ["Mon", "Tue", "Wed", "Ths", "Fri", "Sat", "Sun"]

def change_words(words, func):
    for word in words:
        print(func(word))

"""
Mon
Tue
Wed
Ths
Fri
Sat
Sun
"""
change_words(l, lambda word: word.capitalize())
"""
mon
tue
wed
ths
fri
sat
sun
"""
change_words(l, lambda word: word.lower())
```

#### 一時的な関数 
```python
add = lambda x, y: x + y
# 7
print(add(3, 4))
```

#### 関数の引数として渡す関数
```python
nums = [1, 2, 3, 4]
doubled_nums = list(map(lambda x: x * 2, nums))
# [2, 4, 6, 8]
print(doubled_nums)
```

#### 文字列の長さでソート
```python
names = ["Alice", "Bob", "Charlie"]
names.sort(key=lambda name: len(name))
# ['Bob', 'Alice', 'Charlie']
print(names)
```

#### 条件分岐を使った計算
```python
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
# Even
print(is_even(4))
# Odd
print(is_even(5))
```

#### reduceを使う
```python
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
# 24
print(product)
```