########################
# タプルのアンパッキング #
########################
tup = (10, 20)

x, y = tup
# x = 10 and y = 20
print(f"x = {x} and y = {y}")

###################
# タプルでスワップ #
###################
x = 10
y = 20

# Before swap
# x = 10 and y = 20
print("Before swap")
print(f"x = {x} and y = {y}")
x, y = y, x
# After swap
# x = 20 and y = 10
print("After swap")
print(f"x = {x} and y = {y}")