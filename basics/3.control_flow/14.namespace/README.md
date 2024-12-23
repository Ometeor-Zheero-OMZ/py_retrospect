#### 名前空間
```python
file_path = "C:/"

def print_out():
    file_path = "C:/Program Files/bin"
    # C:/Program Files/bin
    print(file_path)

print_out()
# C:/
print(file_path)
```

```python
file_path = "C:/"

def print_out():
    global file_path

    file_path = "C:/Program Files/bin"
    # C:/Program Files/bin
    print(file_path)

print_out()
# C:/Program Files/bin
print(file_path)
```

```python
def print_out():
    # print_out
    print(print_out.__name__)
    # None
    print(print_out.__doc__)

print_out()
```