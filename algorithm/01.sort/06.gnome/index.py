"""
Selection Sort
In computer science, selection sort is an in-place comparison sorting algorithm.
It has a O(n²) time complexity, which makes it inefficient on large lists,
and generally performs worse than the similar insertion sort. 
Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations,
particularly where auxiliary memory is limited.

フロー：
1. 現在位置から比較と移動を行う
  - 配列の最初から順番に要素をチェックする
  - 現在の要素と1つ前の要素を比較する
2. 条件によって前後に移動する
  - 要素が正しい順序にある場合、次の要素に進む
  - 要素が順序通りでない場合、前に戻り要素を交換する
3. 範囲を狭めながら繰り返す
  - 配列の先頭に戻った場合は再び前に進み、正しい位置に要素を入れ替える動作を繰り返す
4. 処理完了

時間計算量：
Average: O(n²)
Worst:   O(n²)
Best:    O(n)

空間計算量：
O(1) 追加のメモリを使用しない

安定性：
安定
"""
import random
from typing import List

def gnome_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    idx = 0
    while idx < len_nums:
        if idx == 0:
            idx += 1
        if nums[idx] >= nums[idx - 1]:
            idx += 1
        else:
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
            idx -= 1
        
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(gnome_sort(nums))