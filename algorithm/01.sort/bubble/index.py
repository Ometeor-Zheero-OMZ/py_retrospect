"""
Bubble Sort
sometimes referred to as sinking sort, is a simple sorting algorithm 
that repeatedly steps through the input list element by element,
comparing the current element with the one after it,
swapping their values if needed.
These passes through the list are repeated until no swaps have to be performed during a pass,
meaning that the list has become fully sorted.
The algorithm, which is a comparison sort, is named for the way the larger elements "bubble" up to the top of the list.

フロー：
1. 配列の最初から順番に、隣接する要素を比較する
2. 大きい要素が後ろに移動するように、必要なら要素を交換する
3. 1回のパスが終わると、最大の要素がリストの末尾に移動している
4. 残りの要素に対して同様の処理を繰り返す

時間計算量：
Average: O(n²) (二重ループ)
Worst:   O(n²) (逆順の場合)
Best:    O(n) (すでにソート済みなら1回のパスで終了)

空間計算量：
O(1) (追加のメモリをほとんど使用しない)
"""
import random
from typing import List

def bubble_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(len_nums):                               # 各パスを繰り返す
        swapped = False
        for j in range(len_nums - 1 - i):                   # 未ソート部分を比較
            if nums[j] > nums[j + 1]:                         # 左の要素が右より大きければ
                nums[j], nums[j + 1] = nums[j + 1], nums[j] # 交換
                swapper = True
        if not swapped:
            break
    return nums
    """
    `len_nums - 1 -i`
    各パス毎に最後の要素はすでに確定しているので、未ソート部分だけを確認
    Pythonのタプル展開を使って、2つの値を交換
    途中でソートが完了している場合、それ以降の処理は不要のため、swappedで毎回チェック
    """

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(bubble_sort(nums))