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
計数ソート: O(n + k)    kは桁数の範囲
基数ソート: O(d(n + k)) dは最大桁数
Worst:     d桁すべてを処理

空間計算量：
O(n + k)

安定性：
安定
"""

import random
from typing import List

def counting_sort(nums: List[int], place: int) -> List[int]:
    cnt = [0] * 10
    result = [0] * len(nums)

    # 桁の抽出
    for num in nums:
        idx = int(num / place) % 10
        cnt[idx] += 1
    
    # 累積和の計算
    for i in range(1, 10):
        cnt[i] += cnt[i - 1]

    i = len(nums) - 1
    while i >= 0:
        idx = int(nums[i] / place) % 10
        result[cnt[idx] - 1] = nums[i]
        cnt[idx] -= 1
        i -= 1
    return result

def radix_sort(nums: List[int]) -> List[int]:
    max_num = max(nums)
    place = 1
    while max_num > place: # 最大値まで処理
        nums = counting_sort(nums, place)
        place *= 10 # 桁ごとのソート
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(radix_sort(nums))