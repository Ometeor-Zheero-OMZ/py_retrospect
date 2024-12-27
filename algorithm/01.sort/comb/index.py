"""
Comb Sort


フロー：
1. 前方向に進むパス
  - 配列の最初から隣接する要素を比較し、必要に応じて交換する
  - 最大値がリストの末尾に移動する 
2. 後方向に進むパス
  - 配列の最後から隣接する要素を比較し、必要に応じて交換する
  - 最小値がリストの先頭に移動する
3. 範囲を狭めながら繰り返す
  - ソート済み部分を除外して残りの要素に対して同様の処理を繰り返す
4. 早期終了の判定
  - 交換が一度も発生しなければソート完了と判定し、終了する

時間計算量：
Average: O(n²) (二重ループ)
Worst:   O(n²) (逆順の場合)
Best:    O(n) (すでにソート済みなら1回のパスで終了)

空間計算量：
O(1) (追加のメモリを使用しない)
"""
import random
from typing import List

def comb_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    gap = len_nums
    swapped = True
    while gap != 1:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False
        
        for i in range(0, len_nums - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
        
    return nums


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(comb_sort(nums))