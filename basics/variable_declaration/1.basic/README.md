## basic.py

### 出力
#### 数値
```python
num = 1

# 1
print(num)
```

#### 文字列
```python
name = "国崎 往人"

# 国崎 往人
print(name)
```

#### 型表示
```python
num = 1
name = "国崎 往人"
is_owner = True

# 1 <class 'int'>
print(num, type(num))

# 国崎 往人 <class 'str'>
print(name, type(name))

# True <class 'bool'>
print(is_owner, type(is_owner))
```

## type_cast.py

```python
name = '23'
num = int(name)

# 23 <class 'int'>
print(num, type(num))
```

### 変換
#### 整数
```python
# 1
print(int(1.74))

# 12
print(int("12"))
```

#### 単精度浮動小数点数
```python
# 3.0
print(float(3))

# 3.14
print(float("3.14"))
```

#### 複素数
```python
# (1+2j)
print(complex(1, 2))

#(3+4j)
print(complex("3+4j"))
```

#### 文字列
```python
# "23"
print(str(23))

# "3.14"
print(str(3.14))
```

#### リスト
```python
parenthesis = (1, 2, 3)
curly_bracket = {1, 2, 3}

# [1, 2, 3]
print(list(parenthesis))

# [1, 2, 3]
print(list(curly_bracket))
```

#### タプル
```python
parenthesis = (1, 2, 3)
curly_bracket = {1, 2, 3}

# (1, 2, 3)
print(tuple(parenthesis))

# (1, 2, 3)
print(tuple(curly_bracket))
```

#### 集合
```python
bracket = [1, 2, 3]
str = "01001000 01000101 01001100 01010000"

# {1, 2, 3}
print(set(bracket))
# {' ', '1', '0'}
print(set(str))
```

#### ブーリアン
```python
# True
print(bool(1))

# False
print(bool(0))

# True
print(bool([]))

# False
print(bool([1, 2]))
```

#### バイト
```python
s = "リトルバスターズ！"
unicode = "utf-8"

# b'\xe3\x83\xaa\xe3\x83\x88\xe3\x83\xab\xe3\x83\x90\xe3\x82\xb9\xe3\x82\xbf\xe3\x83\xbc\xe3\x82\xba\xef\xbc\x81'
print(bytes(s, unicode))

# bytearray(b'\xe3\x83\xaa\xe3\x83\x88\xe3\x83\xab\xe3\x83\x90\xe3\x82\xb9\xe3\x82\xbf\xe3\x83\xbc\xe3\x82\xba\xef\xbc\x81')
print(bytearray(s, unicode))
```