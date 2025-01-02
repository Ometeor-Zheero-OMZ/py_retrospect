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
