### 文字列スライス
```python
title = 'python'

# p
print(title[0])

# y
print(title[1])

# n
print(title[-1])
```

#### スライスする範囲を指定
```python
title = 'python'

# py
print(title[0:2])
```

#### 先頭の要素から二番目の要素まで
```python
title = 'python'

# py
print(title[:2])
```

#### 2番目の要素から5番目の要素まで
```python
title = 'python'

# tho
print(title[2:5])
```

#### 途中から最後の要素まで
```python
title = 'python'

# thon
print(title[2:])
```

#### スライスで指定した文字を入れ替え
```python
title = 'python'
title = "Mike " + 'T' + title[1] + 's' + title[4:]

# Mike Tyson
print(title)
```