import time

def print_delay():
    s = "Once upon a time\nA little boy lived in a village\nwhere the fishermen hunted tons of fish:\n"
    fish = ["tuna", "salmon", "cod", "mackerel", "trout"]

    fish.sort(key=lambda fish: len(fish))

    for c in s:
        print(c, end='', flush=True)
        time.sleep(0.07)
    
    for f in fish:
        print(f, end=", ", flush=True)
        time.sleep(1)
    print("and so on!")

print_delay()