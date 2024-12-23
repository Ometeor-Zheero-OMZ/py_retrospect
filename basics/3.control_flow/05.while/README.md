#### while
```python
cnt = 0

while cnt < 5:
    cnt += 1
    print(cnt)

print("BLAST OFF!")

"""
1
2
3
4
5
BLAST OFF!
"""
```

#### continue, break
```python
cnt = 0

while cnt < 10:
    cnt += 1

    if cnt == 5:
        continue
    elif cnt == 7:
        break

    print(cnt)

print("2 was skipped, and print out numbers up to 6!")

"""
1
2
3
4
6
2 was skipped, and print out numbers up to 6!
"""
```

#### while else
```python
cnt = 1

while cnt < 6:
    print(f"{cnt} packed.")
    cnt += 1
else:
    print("call it a day!")

"""
1 packed.
2 packed.
3 packed.
4 packed.
5 packed.
call it a day!
"""
```