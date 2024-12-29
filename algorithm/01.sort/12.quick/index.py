"""
Radix Sort
In computer science, radix sort is a non-comparative sorting algorithm.
It avoids comparison by creating and distributing elements into buckets according to their radix.
For elements with more than one significant digit, this bucketing process is repeated for each digit,
while preserving the ordering of the prior step, until all digits have been considered.
For this reason, radix sort has also been called bucket sort and digital sort.

フロー：
1. 最下位桁から順にソート
  - 一の位、十の位、百の位と桁ごとにソートを行う
2. 桁を繰り上げて繰り返す
  - 各桁のソートが完了したら次の桁に移動し、繰り返す
3. 最上位まで処理
  - 最大値の桁数文だけ処理を続ける

時間計算量：
Average: O(n log n)
Best:    O(n log n)
Worst:   O(n²) すでにソート済みまたは逆順のデータの場合

空間計算量：
O(log n)

安定性：
不安定
"""

import random
from typing import List

def partition(nums: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = nums[high] # ピボットをサイドの位置に設定
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    # ピボットを適切な位置に配置
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1  # ピボットの最終位置を返す


def quick_sort(nums: List[int]) -> List[int]:
    def _quick_sort(nums: List[int], low: int, high: int) -> None:
        if low < high:
            # ピボットの位置を取得
            partition_idx = partition(nums, low, high)
            # 左右のサブリストを再帰的にソート
            _quick_sort(nums, low, partition_idx - 1)
            _quick_sort(nums, partition_idx + 1, high)

    # ソート処理を開始
    _quick_sort(nums, 0, len(nums) - 1)
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(quick_sort(nums))