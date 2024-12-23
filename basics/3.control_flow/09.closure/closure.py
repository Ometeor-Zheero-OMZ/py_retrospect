def get_object(a, b):

    def add():
        return a + b
    
    return add

func = get_object(1, 2)
# 3
print(func())

#################
# 状態を保持する #
#################
def outer():
    cnt = 0
    def inner():
        nonlocal cnt
        cnt += 1
        return cnt
    return inner

counter_func = outer()

# 1
print(counter_func())
# other processing 
# 2
print(counter_func())
# and other processing
# 3
print(counter_func())

########################
# 副作用のない関数を返す #
########################
def multiplier(x):
    def multiply_by(y):
        return x * y
    return multiply_by

price = 1200
x = 2
times = multiplier(price)

# 2400
print(times(x))
x = 3
# 3600
print(times(x))


# Oh, the price should be raised!
price = 1400
x = 3
times = multiplier(price)

# 4200
print(times(x))
x = 10
# 14000
print(times(x))
