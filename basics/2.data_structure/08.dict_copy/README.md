#### 辞書のコピー
```python
d = {
    "id": "01",
    "work": "Angel Beats!",
    "name": "立華",
    "gender": "female"
}

copied_d = d.copy()
copied_d["birth"] = "Feb 25"

# {'id': '01', 'work': 'Angel Beats!', 'name': '立華', 'gender': 'female', 'birth': 'Feb 25'}
print(copied_d)
```