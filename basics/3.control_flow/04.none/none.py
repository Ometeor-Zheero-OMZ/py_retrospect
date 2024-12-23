########
# None #
########

d = {"name": "Jane"}
val = d.get("age")

if val is None:
    print("No Element Contained!")

x = 10
del x

try:
    print(x)
except NameError:
    print("NameError: ", None)