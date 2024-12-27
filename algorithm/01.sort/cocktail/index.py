"""
Cocktail Sort
Cocktail shaker sort, also known as bidrectional bubble sort, cocktail sort,
shacker sort (which can also refer to a variant of selection sort), ripple sort,
shuffle sort, or shuttle sort, is an extension of bubble sort.
The algorithm extends bubble sort by operating in two directions.
While it improves on bubble sort by more quickly moving items to the beginning of the list,
it provides only marginal performance improvements.

Like most variants of bubble sort, cocktail shaker sort is used primarily as an educational tool.
More performant algorithms such as quick sort, marge sort, or timsort
are used by the sorting libraries build into popular programming languages such as Python and Java.

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

def cocktail_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    swapped = True
    while swapped:
        swapped = False
        start = 0
        end = len_nums - 1
        for i in range(start, end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i] # 前方向のパス
                swapped = True

        if not swapped:
            break # 交換がなければ終了

        swapped = False
        end -= 1 # 範囲を狭める

        for i in range(end - 1, start - 1, -1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i] # 後方向のパス
                swapped = True

        start += + 1 # 範囲を狭める

    return nums


if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(cocktail_sort(nums))