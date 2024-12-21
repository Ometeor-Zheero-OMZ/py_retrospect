### 文字代入

```python
right_side = "ax^2 + b"
# y = ax^2 + b
print(f"y = {right_side}")
```

```python
first_praise = "smart"
second_praise = "gorgeous"
# He is smart, and she is gorgeous
print(f"He is {first_praise}, and she is {second_praise}")
```

```python
idx = "smart"
other_idx = "gorgeous"

# He is smart, and she is gorgeous
print(f"He is {first_praise}, and she is {second_praise}")
```

#### リストから文字を指定
```python
list = ["smart", "gorgeous", "kind", "warm-hearted", "down-to-earth"]

# He is smart, and she is gorgeous
print(f"He is {list[0]}, and she is {list[1]}")

# He is gorgeous, and she is smart
print(f"He is {list[1]}, and she is {list[0]}")
```

#### リストから無作為に文字を指定
```python
list = ["smart", "gorgeous", "kind", "warm-hearted", "down-to-earth"]

rand = random.randrange(0, len(list))
other_rand = random.randrange(0, len(list))

### Randomly selected praises
print(f"He is {list[rand]}, and she is {list[other_rand]}")
```