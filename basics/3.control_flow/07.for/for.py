#######
# for #
#######
list = [1, 2, 3, 4, 5]

for i in list:
    print(i)

"""
1
2
3
4
5
"""
#########
# range #
#########
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
else:
    print("終了だしん！")

"""
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...
98
Fizz
Buzz
終了だしん！
"""

print("聴いてください")
for _ in range(10):
    print("打")
else:
    print("(間奏)")

"""
聴いてください
打
打
打
打
打
打
打
打
打
打
(間奏)
"""

#############
# enumerate #
#############
list = ["お寿司", "お肉", "おっふ", "おうどん"]
for i, elem in enumerate(list):
    print(i, elem)

"""
0 お寿司
1 お肉
2 おっふ
3 おうどん
"""

#############################################
# In Rust
# for (i, elem) in list.iter().enumerate() {
#     println("{} {}", i, elem);
# }
#############################################

#######
# zip #
#######
days = ["Monday", "Tuesday", "Wednesday", "Thusday", "Friday"]
foods = ["sushi", "chickn with cheese", "porched eggs"]
refreshments = ["cappuccino", "strawberry flavored water", "tea"]

for day, food, refreshment in zip(days, foods, refreshments):
    print(day, food, refreshment)

"""
Monday sushi cappuccino
Tuesday chickn with cheese strawberry flavored water
Wednesday porched eggs tea
"""
#############
# ペアを作る #
#############
students = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

for name, score in zip(students, scores):
    print(f"{name} scored {score}")

"""
Alice scored 85
Bob scored 90
Charlie scored 78
"""

#############
# 辞書を作る #
#############
keys = ["name", "age", "city"]
values = ["Alice", 25, "Netherland"]

info = dict(zip(keys, values))
print(info)

"""
{'name': 'Alice', 'age': 25, 'city': 'Netherland'}
"""

#################################
# インデックスを使用してペアを作る #
#################################
questions = ["1 + 1 = ?", "2 + 2 = ?", "3 + 3 = ?"]
answers = [2, 4, 6]

for idx, (q, a) in enumerate(zip(questions, answers), 1):
    print(f"Q{idx}: {q} Answer: {a}")

"""
Q1: 1 + 1 = ? Answer: 2
Q2: 2 + 2 = ? Answer: 4
Q3: 3 + 3 = ? Answer: 6
"""

d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)

"""
x : 100
y : 200
"""