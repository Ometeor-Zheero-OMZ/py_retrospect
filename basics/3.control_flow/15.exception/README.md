#### 例外処理
```python
l = [1, 2, 3]
i = 5

try:
    l[i]
except IndexError as e:
    print(f"IndexError: {e}")
except KeyError as e:
    print(f"KeyError :{e}")
except NameError as e:
    print(f"NameError: {e}")
finally:
    print("released pool")

"""
IndexError: list index out of range
released pool
"""
```

```python
l = [1, 2, 3]
i = 2

try:
    l[i]
except IndexError as e:
    print(f"IndexError: {e}")
except KeyError as e:
    print(f"KeyError :{e}")
except NameError as e:
    print(f"NameError: {e}")
else:
    print(f"SUCCESS: {l[i]}")
finally:
    print("released pool")

"""
SUCCESS: 3
released pool
"""
```

#### カスタム例外エラー
```python
class UppercaseError(Exception):
    pass

def check():
    words = ["apple", "ORANGE", "banana"]

    for word in words:
        if word.isupper():
            raise UppercaseError(word)
        
check()

"""
Traceback (most recent call last):
  File "py_retrospect/basics/3.control_flow/15.exception/exception.py", line 52, in <module>
    check()
    ~~~~~^^
  File "py_retrospect/basics/3.control_flow/15.exception/exception.py", line 50, in check
    raise UppercaseError(word)
UppercaseError: ORANGE
"""
```