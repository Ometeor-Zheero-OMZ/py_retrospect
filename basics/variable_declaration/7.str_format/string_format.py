import random

###############
# old version #
###############
# y = ax + b
print("y = {}".format("ax^2 + b"))

# y = 7x + 3
print("y = {}{}^2 + {}".format('7', 'x', '3'))

# He is smart, and she is gorgeous
print("He is {0}, and she is {1}".format("smart", "gorgeous"))

###########################################
# latest version "f-string" (Python 3.6+) #
###########################################
right_side = "ax^2 + b"
# y = ax^2 + b
print(f"y = {right_side}")


a, x, b = 7, 'x', 3
# y = 7x^2 + 3
print(f"y = {a}{x}^2 + {b}")

first_praise = "smart"
second_praise = "gorgeous"
# He is smart, and she is gorgeous
print(f"He is {first_praise}, and she is {second_praise}")

idx = "smart"
other_idx = "gorgeous"

# He is smart, and she is gorgeous
print(f"He is {first_praise}, and she is {second_praise}")

list = ["smart", "gorgeous", "kind", "warm-hearted", "down-to-earth"]

# He is smart, and she is gorgeous
print(f"He is {list[0]}, and she is {list[1]}")

# He is gorgeous, and she is smart
print(f"He is {list[1]}, and she is {list[0]}")

rand = random.randrange(0, len(list))
other_rand = random.randrange(0, len(list))

### Randomly selected praises
print(f"He is {list[rand]}, and she is {list[other_rand]}")

