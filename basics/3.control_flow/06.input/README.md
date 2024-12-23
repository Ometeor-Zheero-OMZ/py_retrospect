#### input
```python
is_ok = True

while is_ok:
    word = input("Enter `ok` to finish:\n")
    if word == 'ok':
        break
    print("please enter `ok`")

"""
Enter `ok` to finish:
s
please enter `ok`
Enter `ok` to finish:
ok
"""
```

```python
is_ok = False

while not is_ok:
    try:
        word = input("Enter a number to addition:\n")
        num = int(word)
        if isinstance(num, int):
            num += 1
            print(f"num = {num}")
            break
    except ValueError:
        print("Please enter a number\n")
"""
Enter a number to addition:
s
Please enter a number

Enter a number to addition:
1
num = 2
"""
```