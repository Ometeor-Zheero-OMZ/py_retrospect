#### コンストラクタ

```python
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

person = Person("test_user")
user1 = person.get_name()

person.set_name("Jimmy")
user2 = person.get_name()

# test_user
print(user1)
# Jimmy
print(user2)
```
