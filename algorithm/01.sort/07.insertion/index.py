"""
Insertion Sort
Insertion sort is a simple algorithm that builds the final sorted array (or list)
one item at a time by comparisons. It is much less efficient on large lists that more 
advanced algorithms such as quick sort, heap sort, or mergsort. 
However, insertion sort provides several advantages.

フロー：
1. ソート済み部分を確率
  - 最初の要素はすでにソートされているとみなし、2番目の要素から処理を開始する
2. 挿入位置を探索
  - 現在の要素を一時保存し、ソート済み部分を逆方向に比較しながら適切な挿入位置を探す
3. 要素をシフトして挿入
  - 挿入位置より大きい要素を1つ右に移動し、空いた場所に一時保存した要素を挿入する
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

def insertion_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)

    for i in range(1, len_nums): # 2番目の要素から処理を開始し、順番にすべての要素を挿入する
        tmp = nums[i] # 現在の要素を一時保存する
        j = i - 1     # 直前の要素インデックスを j として保持する
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j] # 現在の要素より大きい値を1つ右にシフトする
            j -= 1                # 挿入位置を探すために j を1つずつ減らす

        nums[j + 1] = tmp # 空いた位置に一時保存した要素を挿入する
        
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(insertion_sort(nums))