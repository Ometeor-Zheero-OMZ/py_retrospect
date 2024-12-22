#### キーを取得
```python
d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

# dict_keys(['id', 'work', 'name', 'gender'])
print(d.keys())
```

#### 値を取得
```python
d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

# dict_values(['01', 'Angel Beats!', '立華', 'female'])
print(d.values())
```

#### 辞書を別の辞書で上書き
```python
d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

other_d = { "work": "かぎなど", "death_cause": "unknown" }
d.update(other_d)

# {'id': '01', 'work': 'かぎなど', 'name': '立華', 'gender': 'female', 'death_cause': 'unknown'}
print(d)
```

#### キーを指定して値を取得
```python
d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

# 立華
print(d.get("name"))
```

#### 指定した要素を取り出す
```python
d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

other_d = { "work": "かぎなど", "death_cause": "unknown" }
d.update(other_d)

d.pop("gender")
# del でも可能
# del d["gender"]

# {'id': '01', 'work': 'かぎなど', 'name': '立華', 'death_cause': 'unknown'}
print(d)
```

#### 辞書を空にする
```python
d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

d.clear()

# {}
print(d)
```