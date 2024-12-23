t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9)

r = [i for i in t]

# [1, 2, 3, 4, 5]
print(r)

r = [i for i in t if i % 2 == 0]
# [2, 4]
print(r)

r = [i * j for i in t for j in t2]
# [5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 15, 18, 21, 24, 27, 20, 24, 28, 32, 36, 25, 30, 35, 40, 45]
print(r)


list = [True, True, False, True]

r = [is_admin for is_admin in list if is_admin]
# [True, True, True]
print(r)