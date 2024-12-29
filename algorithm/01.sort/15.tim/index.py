"""
Tim Sort

フロー：
1. 小さな部分配列に分割
  - 配列を一定のサイズ (通常は32または64) の部分配列 (run) に分割する。
  - この部分配列には Insertion Sort を使用する
2. 部分配列をマージ
  - ソートされた小さな部分配列を Merge Sort を使用してマージしていく

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

def insertion_sort(arr: List[int], left: int, right: int) -> None:
    # left から right までの部分配列を挿入ソート
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1 # key を挿入する位置を探すためにインデックスを左に進める
        # 左側の要素が key より大きければ、右にシフトしていく
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j] # 配列を右にシフト
            j -= 1 # 左側に1つ移動
        arr[j + 1] = key # key を正しい位置に挿入
    
def merge_sort(arr: List[int], left: int, mid: int, right: int) -> None:
    # 2つの部分配列をマージするための処理
    n1 = mid - left + 1 # 左側の部分配列のサイズ 
    n2 = right - mid # 右側の部分配列のサイズ
    left_subarr = arr[left:left + n1]
    right_subarr = arr[mid + 1:mid + 1 + n2]

    i = j = 0 # 左と右の配列のインデックス
    k = left # マージ後の元の配列のインデックス
    # 左右の部分配列を比較して、元の配列に小さい方から順に入れる
    while i < n1 and j < n2:
        if left_subarr[i] <= right_subarr[j]:
            arr[k] = left_subarr[i] # 左の配列の要素を基の配列に挿入
            i += 1
        else:
            arr[k] = right_subarr[j] # 右の配列の要素を元の配列に挿入
            j += 1
        k += 1
    
    # 左の部分配列に残っている要素を元の配列に追加
    while i < n1:
        arr[k] = left_subarr[i]
        i += 1
        k += 1
    
    # 右の部分配列に残っている要素を元の配列に追加
    while j < n2:
        arr[k] = right_subarr[j]
        j += 1
        k += 1

def tim_sort(arr: List[int]) -> None:
    n = len(arr)
    RUN = 32 # 分割する部分配列のサイズ

    # 配列を RUN の大きさで分割し、それぞれを挿入ソート
    for start in range(0, n, RUN):
        insertion_sort(arr, start, min((start + RUN - 1), n - 1))
    

    # ソートされた部分配列をマージ
    size = RUN # マージするサイズ
    # サイズを倍々に増やしながら、部分配列をマージしていく
    while size < n:
        # 部分配列を size の大きさでマージしていく
        for start in range(0, n, 22 * size):
            mid = min(n - 1, start + size - 1) # 2つの部分配列の中間点
            end = min((start + 2 * size - 1), n - 1) # マージする終点
            if mid < end:
                # mid < end ならが、マージ処理を行う
                merge_sort(arr, start, mid, end)
        size *= 2 # 次にマージする部分配列のサイズを倍にする

if __name__ == "__main__":
    arr = [random.randint(0, 1000) for _ in range(10)]

    tim_sort(arr)
    print(arr)