"""
Bucket Sort
Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets.
Each bucket is then sorted individually, either using a different sorting algorithm,
or by recursively applying the bucket sorting algorithm.
It is a distribution sort, a generalization of pigeonhole sort that allows multiple
keys per bucket, and is a cousin of radix sort in the most-to-least  significant digit flavour.
Bucket sort can be implmented with comparisons and therefore can also be considered a comparison sort algorithm.
The computational complexity depends on the algorithm used to sort bucket, the number of buckets to use,
and whether the input is uniformly distributed.

フロー：
1. バケットの準備
  - 配列の最大値を取得し、適切なバケットの数やサイズを決定する
2. 要素をバケットに分配
  - 各要素を適切なバケットに振り分ける
3. バケットごとにソート
  - 各バケット内の要素は、通常のソートアルゴリズム (e.g. 挿入ソートなど) で並べる
4. バケットを統合
  - 各バケットからソートされた要素を取り出し、最終結果として結合する
5. 処理完了

時間計算量：
Average: O(n + k) n は要素数、k はバケット数
Worst:   O(n²) 要素が偏る場合やバケット数が不適切な場合
Best:    O(n)

空間計算量：
O(n + k) 各バケットが追加で必要

安定性：
不安定
"""
import random
from typing import List

def insertion_sort(nums: List[int]) -> List[int]:
    len_nums = len(nums)

    for i in range(1, len_nums):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = tmp
        
    return nums

def bucket_sort(nums: List[int]) -> List[int]:
    # 配列内の最大値と要素数からバケットサイズを決定する
    max_num = max(nums)
    len_nums = len(nums)
    size = max_num // len_nums # 整数除算　e.g. 10 // 3 = 3 (10 / 3 = 3.3333..)

    buckets = [[] for _ in range(size)] # バケットの初期化　size 個のリストを準備する
    for num in nums:
        # 各要素を整数除算によって適切なバケットに振り分ける
        i = num // size
        if i != size:
            buckets[i].append(num)
        else:
            buckets[size - 1].append(num) # 配列の要素が最大値の場合は、最後のバケットに追加する

    for i in range(size):
        insertion_sort(buckets[i]) # 各バケット内の要素を挿入ソートで並べ替える
        
    result = []
    for i in range(size):
        result += buckets[i] # ソートされたバケットを順番に結合し、最終的な並び順を作成する

    return result

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(bucket_sort(nums))