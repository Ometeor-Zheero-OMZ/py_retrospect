"""
Shellsort
Shellsort, also known as Shell sort or Shell's method, is an in-place comparison sort.
It can be seen as either a generalization of sorting by exchange (bubble sort) or sorting by insertino (insertion sort).
The method starts by sorting pairs of elements far apart from each other, then progressively reducing the gap between elements to be compared.
By starting with far-apart elements, it can move some out-of-place elements into the position faster than a simple nearest-neighbor exchange.
Donald Shell published the first version of this sort in 1959.
The running time of SHellsort is heavily dependent on the gap sequence it uses.
For many practical variants, determining their time complexity remains an open problem.

フロー：
1. ギャップの設定
  - 最初に、リストの長さを基に gap を決定する。gap は通常、リストの長さを2で割った値から始まり、次第に小さくする
2. ギャップを使ったソート
  - ギャップを使って、間隔を開けた位置の要素同士を比較する
  - ギャップを徐々に小さくし、ギャップが1になるまで繰り返す

時間計算量：
Average: O(n log n)
Worst:   O(n²)
Best:    O(n log n)

空間計算量：
O(1) 


安定性：
安定
"""

import random
from typing import List

def shell_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    gap = len_nums // 2 # ギャップの初期設定
    while gap > 0:
        for i in range(gap, len_nums):
            tmp = nums[i] # 現在の要素を保持
            j = i # 現在の挿入位置を追跡
            while j >= gap and nums[j - gap] > tmp: # j がギャップ分だけ移動しながら、隣接する要素を比較する
                nums[j] = nums[j - gap] # シフト
                j -= gap
            nums[j] = tmp
        gap //= 2

    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(shell_sort(nums))