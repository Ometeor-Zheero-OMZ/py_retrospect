#### None
```python
d = {"name": "Jane"}
val = d.get("age")

if val is None:
    # No Element Contained!
    print("No Element Contained!")
```

```python
x = 10
del x

try:
    print(x)
except NameError:
    # NameError: None
    print("NameError: ", None)
```