s = "Hi, what's up for today? I'm gonna kick-back and enjoy happy coding up to 8."

# True
print(s.startswith("Hi"))

# True
print(s.endswith("up to 8."))

# 11 (index of "up" as first occurrence)
print(s.find("up"))

# 68 (index of "up" as next occurrence)
print(s.rfind("up"))

# 2
print(s.count("up"))

# Hi, what's up for today? i'm gonna kick-back and enjoy happy coding up to 8.
print(s.capitalize())

# Hi, What'S Up For Today? I'M Gonna Kick-Back And Enjoy Happy Coding Up To 8.
print(s.title())

# HI, WHAT'S UP FOR TODAY? I'M GONNA KICK-BACK AND ENJOY HAPPY CODING UP TO 8.
print(s.upper())

# hi, what's up for today? i'm gonna kick-back and enjoy happy coding up to 8.
print(s.lower())

# hI, WHAT'S UP FOR TODAY? i'M GONNA KICK-BACK AND ENJOY HAPPY CODING UP TO 8.
print(s.swapcase())

# Hi, what's down for today? I'm gonna kick-back and enjoy happy coding down to 8.
print(s.replace("up", "down"))