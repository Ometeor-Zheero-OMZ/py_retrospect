s = set()

c = {i for i in range(10)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(c)

c = {i for i in range(10) if i % 3 == 0}
# {0, 9, 3, 6}
print(c)