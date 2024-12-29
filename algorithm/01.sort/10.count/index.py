"""
Counting Sort
In computer science, counting sort is an algorithm for sorting a collection of objects
according to keys that are small positive intergers; that is, it is an integer sorting algorithm.
It operates by counting the number of objects that possess distinct key values,
and applying prefix sum on those counts to determine the positions of each key value in the output sequence.
Its running time is linear in the number of items and the difference between the maximum key value and the minimum key value,
so it is only suitable for direct use in situations where the variation in keys is not significantly greater than the number 
of items. It is often used as a subroutine in radix sort, another sorting algorithm, which can handle larger keys more efficiently.

フロー：
1. カウント配列の作成
  - 尿力リスト内の各値の出現回数をカウントする
2. 累積和を計算
  - 各要素の位置を決定するために、カウント配列の累積和を計算する
3. 出力リストの構築
  - 入力リストを逆順に走査し、各値をカウント配列のインデックスに基づいて適切な位置に配列する

時間計算量：
Average: O(n + k) kは要素の最大値
Worst:   O(n + k) kは要素の最大値
Best:    O(n + k) kは要素の最大値

空間計算量：
O(n + k)

安定性：
安定
"""

import random
from typing import List

def counting_sort(nums: List[int]) -> List[int]:
    max_num = max(nums) # 最大値を取得
    cnt = [0] * (max_num + 1) # 最大値までの範囲に対応するカウント配列を作成する
    result = [0] * len(nums)

    for num in nums:
        cnt[num] += 1
    
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1] # 累積和を計算

    i = len(nums) - 1
    while i >= 0:
        idx = nums[i] # 逆順に処理
        result[cnt[idx] - 1] = nums[i] # カウント配列を参照し、結果配列の正しい位置に要素を配置
        cnt[idx] -= 1 # 要素を配置した後はカウントを1つ減らす
        i -= 1
    return result

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(counting_sort(nums))