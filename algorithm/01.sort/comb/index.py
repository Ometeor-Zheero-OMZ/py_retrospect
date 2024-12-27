"""
Comb Sort
Comb sort is a relatively simpl sorting algorithm originally designed by Wlodzimierz Dobosiewixz and Artur Borowy in 1980,
later rediscovered (and given the name "Combsort") by Stephen Lacey and Richard Box in 1991. Comb sort improves on
bubble sort in the same way that Shellsort improves on insertion sort,
in that they both allow elements that start far away from their intended position to move more than one space per swap.

フロー：
1. 初期設定
  - 配列の長さを初期ギャップとして設定する
2. ギャップの縮小
  - ギャップを1.3倍に縮小しながら繰り返す
3. 比較と交換
  - キャップ分だけ離れた要素を比較し、必要に応じて交換する
4. 終端判定

時間計算量：
Average: O(n log n) ギャップの縮小により効率化されている
Worst:   O(n²)      ギャップが小さくなったとき、バブルソートを同様の動きになる
Best:    O(n)       すでにソートされている場合は高速終了

空間計算量：
O(1) 追加のメモリを使用しないインプレースアルゴリズム
"""
import random
from typing import List

def comb_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    gap = len_nums # 配列サイズで初期化
    swapped = True 
    while gap != 1:
        gap = int(gap / 1.3) # ギャップを1.3倍に縮小　1.3は経験的に最適とされる値のこと
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