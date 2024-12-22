#### 指定した要素のインデックスを取得
```python
l = [1, 2, 3, 4, 5, 1, 2, 3]

# 2
print(l.index(3))
```

#### 指定した位置から指定した要素のインデックスを取得
```python
l = [1, 2, 3, 4, 5, 1, 2, 3]

# 7
print(l.index(3, 3))
```

#### 指定した要素の数を勘定
```python
l = [1, 2, 3, 4, 5, 1, 2, 3]

# 2
print(l.count(3))
```

#### ソート
```python
l = [1, 2, 3, 4, 5, 1, 2, 3]
l.sort()

# [1, 1, 2, 2, 3, 3, 4, 5]
print(l)
```

#### 逆向きソート
```python
l = [1, 2, 3, 4, 5, 1, 2, 3]
l.sort(reverse=True)

# [5, 4, 3, 3, 2, 2, 1, 1]
print(l)
```

#### 逆向き
```python
l = [1, 2, 3, 4, 5, 1, 2, 3]
l.reverse()

# [3, 2, 1, 5, 4, 3, 2, 1]
print(l)
```

#### 文字列の分割
```python
s = "Segmentation fault occurred. Please fix it."
to_split = s.split(' ')

# ['Segmentation', 'fault', 'occurred.', 'Please', 'fix', 'it.']
print(to_split)
```

#### 分割した文字列を再結合
```python
s = "Segmentation fault occurred. Please fix it."
to_split = s.split(' ')

x = ' '.join(to_split)
# Segmentation fault occurred. Please fix it.
print(x)
```