## ハッシュテーブル

```python
from typing import Any
import hashlib

class HashTable:
    def __init__(self, size=10) -> None:
        self.size = size
        # [[], [], [], [], [], [], [], [], [], []]
        self.table = [ [] for _ in range(size) ]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, k, v) -> None:
        idx = self.hash(k)

        # 同じキーがある場合、値を更新する
        for data in self.table[idx]:
            if data[0] == k:
                data[1] = v
                return
        else:
            self.table[idx].append([k, v])

    def print(self) -> None:
        for idx in range(self.size):
            print(idx, end=' ')
            for data in self.table[idx]:
                print("-->", end=' ')
                print(data, end=' ')

            print()

    def get(self, key) -> Any:
        idx = self.hash(key)

        for data in self.table[idx]:
            if data[0] == key:
                return data[1]

if __name__ == "__main__":
    ht = HashTable()

    ht.add("router", "IODATA")
    # [[], [], [], [], [], [], [['router', 'IODATA']], [], [], []]
    print(ht.table)
    ht.add("router", "NTT")
    # [[], [], [], [], [], [], [['router', 'NTT']], [], [], []]
    print(ht.table)

    ht.add("mouse", "Logicool")
    # [[], [], [], [], [], [], [['router', 'NTT'], ['mouse', 'Logicool']], [], [], []]
    print(ht.table)

    ht.add("GPU", "NVIDIA")
    # [[['GPU', 'NVIDIA']], [], [], [], [], [], [['router', 'NTT'], ['mouse', 'Logicool']], [], [], []]
    print(ht.table)

    ht.print()

    # NVIDIA
    print(ht.get("GPU"))
    # None
    print(ht.get("memory"))
```

### 指定した数値になる組み合わせを探す

```python
from typing import List, Tuple, Optional

def get_pair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()

    for num in nums:
        val = target - num
        if val in cache:
            return val, num

        cache.add(num)

def get_pair_half_sum(nums: List[int]) -> Optional[Tuple[int, int]]:
    sum_nums = sum(nums)

    half_sum, remainder = divmod(sum_nums, 2)
    if remainder != 0:
        return

    cache = set()
    for num in nums:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num

if __name__ == "__main__":
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    # (2, 10)
    print(get_pair(l, t))

    l = [11, 2, 5, 9, 10, 3]
    # (11, 9)
    print(get_pair_half_sum(l))
```
