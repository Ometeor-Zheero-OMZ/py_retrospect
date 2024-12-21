### 文字列メソッド

```python
s = "Hi, what's up for today? I'm gonna kick-back and enjoy happy coding up to 8."
```

#### 指定した文字列が先頭に配置されているかどうか判定
```python
# True
print(s.startswith("Hi"))
```

#### 指定した文字列が最後尾に配置されているかどうか判定
```python
# True
print(s.endswith("up to 8."))
```

#### 指定した文字列を探す
```python
# 11 (index of "up" as first occurrence)
print(s.find("up"))
```

#### 指定した文字列が1つ以上ある場合2つ目を探す
```python
# 68 (index of "up" as next occurrence)
print(s.rfind("up"))
```

#### 指定した文字列が登場する個数を勘定
```python
# 2
print(s.count("up"))
```

#### 文字列の先頭を大文字にする
```python
# Hi, what's up for today? i'm gonna kick-back and enjoy happy coding up to 8.
print(s.capitalize())
```

#### スペース区切りで word の先頭を大文字にする
```python
# Hi, What'S Up For Today? I'M Gonna Kick-Back And Enjoy Happy Coding Up To 8.
print(s.title())
```

#### 全て大文字にする
```python
# HI, WHAT'S UP FOR TODAY? I'M GONNA KICK-BACK AND ENJOY HAPPY CODING UP TO 8.
print(s.upper())
```

#### 全て小文字にする
```python
# hi, what's up for today? i'm gonna kick-back and enjoy happy coding up to 8.
print(s.lower())
```

#### 大文字と小文字を入れ替え
```python
# hI, WHAT'S UP FOR TODAY? i'M GONNA KICK-BACK AND ENJOY HAPPY CODING UP TO 8.
print(s.swapcase())
```

#### 指定した文字列同士を入れ替え
```python
# Hi, what's down for today? I'm gonna kick-back and enjoy happy coding down to 8.
print(s.replace("up", "down"))
```