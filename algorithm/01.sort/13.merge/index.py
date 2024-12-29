import random
from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    
    # 分割
    center = len(nums) // 2
    left = nums[:center]
    right = nums[center:]

    # 再帰的ソート
    left = merge_sort(left)
    right = merge_sort(right)

    # マージ処理
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 残りの要素を追加
    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(10)]

    print(merge_sort(nums))