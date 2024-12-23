def count_up(n):
    cnt = 1
    while cnt <= n:
        yield cnt
        cnt += 1

gen = count_up(5)
for num in gen:
    print(num)

"""
1
2
3
4
5
"""

import time

def sensor_data():
    import random
    while True:
        yield random.randint(1, 100)
        time.sleep(1)

cnt = 0
for data in sensor_data():
    cnt += 1
    print(f"Sensor data: {data}")

    if cnt >= 5:
        break

"""
Sensor data: 21
Sensor data: 61
Sensor data: 92
Sensor data: 28
Sensor data: 84
"""

import asyncio

async def async_gen():
    for i in range(5):
        yield i
        await asyncio.sleep(1)

async def main():
    async for val in async_gen():
        print(val)

asyncio.run(main())
"""
0
1
2
3
4
"""