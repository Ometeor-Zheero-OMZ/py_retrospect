#### 指定した要素を空にする
```python
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s[3:6] = []

# ['a', 'b', 'c', 'g']
print(s)
```

#### 最後尾に要素を追加
```python
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s.append('z')

# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'z']
print(s)
```

#### 指定した位置に要素を追加
```python
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s.insert(0, "zero")

# ['zero', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
print(s)
```

#### 最後尾の要素を取り出す
```python
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
tmp = s.pop()

# ['a', 'b', 'c', 'd', 'e', 'f']
print(s)
# g
print(tmp)
```

#### 指定した位置の要素を取り出す
```python
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
tmp = s.pop(3)

# ['a', 'b', 'c', 'e', 'f', 'g']
print(s)
# d
print(tmp)
```

#### 要素を削除
```python
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del s[3]

# ['a', 'b', 'c', 'e', 'f', 'g']
print(s)
```

#### リストを削除
```python
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
del s

# NameError: name 's' is not defined
print(s)
```

#### リストの先頭から指定した要素を探して取り出す
```python
s = [1, 2, 1, 3, 2, 4, 3, 5, 4, 6]
tmp = s.remove(2)

# [1, 1, 3, 2, 4, 3, 5, 4, 6]
print(s)
# None (removeは返り値がない)
print(tmp)

s.remove(2)
# [1, 1, 3, 4, 3, 5, 4, 6]
print(s)

s.remove(2)
# ValueError: list.remove(x): x not in list
print(s)
```


#### リストの結合
````python
x = [1, 2, 3]
y = [4, 5, 6]

# [1, 2, 3, 4, 5, 6]
print(x + y)

x.extend(y)
# [1, 2, 3, 4, 5, 6]
print(x)
```