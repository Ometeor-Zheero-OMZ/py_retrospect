import random 
from typing import List

def heapify(nums: List[int], n: int, i: int) -> None:
    largest = i # ルートノード
    left = 2 * i + 1 # 左の子ノード
    right = 2 * i + 2 # 右の子ノード

    # 左の子ノードがルートより大きい場合
    if left < n and nums[left] > nums[largest]:
        largest = left
    
    # 右の子ノードが現在の最大値より大きい場合
    if right < n and nums[right] > nums[largest]:
        largest = right
    

    # 最大値がルートでない場合、交換して再帰的にヒープ可
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

def heap_sort(nums: List[int]) -> List[int]:
    n = len(nums)

    # 配列を最大ヒープに変換
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)
    
    # ヒープから要素を取り出してソート
    for i in range(n - 1, 0, -1):
        # ルート (最大値) を末尾に移動
        nums[0], nums[i] = nums[i], nums[0]
        # ヒープサイズを1減らし、再度ヒープ可
        heapify(nums, i, 0)
    
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]
    
    print(heap_sort(nums))