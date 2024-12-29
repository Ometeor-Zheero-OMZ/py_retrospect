"""
Binary Search
In computer science, binary search, also known as half-interval search,
logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array.
Binary search compares the target value to the middle element of the array.
If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half,
again taking the middle element to compare to the target value, and repeating this until the target value is found.
If the search ends with the remaining half being empty, the target is not in the array.

"""
from typing import List, NewType

IndexNum = NewType('IndexNum', int)

def binary_serch(nums: List[int], val: int) -> IndexNum:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]

    print(f"Index of elements in list is: nums[{binary_serch(nums, 15)}]")