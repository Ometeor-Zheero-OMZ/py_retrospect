is_admin = True

if is_admin:
    print("Authenticated")
else:
    print("Unauthenticated")

a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
len = len(a)

if len < 3:
    print("Too low")
elif len < 6:
    print("good")
else:
    print("Too high")