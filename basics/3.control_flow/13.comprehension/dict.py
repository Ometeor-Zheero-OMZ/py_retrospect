d = ["Mon", "Tue", "Wed"]
f = ["coffee", "milk", "water"]

# 使用する変数: さらに使用する変数 for 受け取り1, 受け取り2 in zip(リスト1, リスト2)
c = {x: y for x, y in zip(d, f)}
# {'Mon': 'coffee', 'Tue': 'milk', 'Wed': 'water'}
print(c)