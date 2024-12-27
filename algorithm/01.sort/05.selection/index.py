"""
Selection Sort
In computer science, selection sort is an in-place comparison sorting algorithm.
It has a O(n²) time complexity, which makes it inefficient on large lists,
and generally performs worse than the similar insertion sort. 
Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations,
particularly where auxiliary memory is limited.

フロー：
1. 最小値を選択
  - 配列の最初から順に、最小の要素を見つける
2. 最小値を交換
  - 見つけた最小値を現在の位置 (i番目) に移動させる
3. 次の位置に進む
  - 最小値を移動させた後、次の位置 (i+1番目) に移動し、同じ操作を繰り返す
4. 処理完了

時間計算量：
Average: O(n²)
Worst:   O(n²)
Best:    O(n²)

空間計算量：
O(1) 追加のメモリを使用しない

安定性：
不安定
"""
import random
from typing import List

def selection_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(len_nums):
        min_idx = i # 最小値のインデックスを追跡
        for j in range(i + 1, len_nums): # i+1番目からリストの最後までの要素を比較
            if nums[min_idx] > nums[j]: # 左右を比べ、左が大きい場合は最小値を更新
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i] # min_idx で見つけた最小値を現在の位置に交換
        
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(selection_sort(nums))