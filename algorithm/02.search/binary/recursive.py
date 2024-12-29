"""
Binary Search


"""
from typing import List, NewType

IndexNum = NewType('IndexNum', int)

def binary_search(nums: List[int], val: int) -> IndexNum:
    def _binary_search(nums: List[int], val: int, left: IndexNum, right: IndexNum) -> IndexNum:
        if left > right:
            return -1
        
        mid = (left + right) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            return _binary_search(nums, val, mid + 1, right)
        else:
            return _binary_search(nums, val, left, mid - 1)

    return _binary_search(nums, val, 0, len(nums) - 1)

if __name__ == "__main__":
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]

    print(f"Index of elements in list is: nums[{binary_search(nums, 15)}]")