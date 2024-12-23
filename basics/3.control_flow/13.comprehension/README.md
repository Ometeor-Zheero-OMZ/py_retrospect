#### リスト内包表記
```python
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)

r = [i for i in t if i % 2 == 0]
# [2, 4]
print(r)

r = [i * j for i in t for j in t2]
# [5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 15, 18, 21, 24, 27, 20, 24, 28, 32, 36, 25, 30, 35, 40, 45]
print(r)
```

```python
r = [is_admin for is_admin in list if is_admin]
# [True, True, True]
print(r)
```

#### 辞書内包表記
```python
d = ["Mon", "Tue", "Wed"]
f = ["coffee", "milk", "water"]

# 使用する変数: さらに使用する変数 for 受け取り1, 受け取り2 in zip(リスト1, リスト2)
c = {x: y for x, y in zip(d, f)}
# {'Mon': 'coffee', 'Tue': 'milk', 'Wed': 'water'}
print(c)
```

#### 集合内包表記
```python
s = set()

c = {i for i in range(10)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(c)

c = {i for i in range(10) if i % 3 == 0}
# {0, 9, 3, 6}
print(c)
```

#### ジェネレーター内包表記
```python
g = (i for i in range(10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))

"""
0
1
2
3
"""
```