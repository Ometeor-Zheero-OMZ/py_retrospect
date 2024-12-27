"""
Bogo Sort
In computer science, bogosort (also known as permutation sort and stupid sort)
is a sorting algorithm based on the generate and test paradigm.
The function successively generates permutations of its input until it finds one that is sorted.
It is not considered useful for sorting, but may be used for educational purposes,
to contrast it with more efficient algorithms.

Average: O((n + 1)!)
Best: O(n)
Worst: Unbounded
Stable? No
"""

import random
from typing import List

def in_order(nums: List[int]) -> bool:
    # for i in range(len(nums)-1):
    #     if nums[i] > nums[i+1]:
    #         return False
    # return True

    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

def bogo_sort(nums: List[int]) -> List[int]:
    while not in_order(nums):
        random.shuffle(nums)
    return nums

if __name__ == "__main__":
    # nums = [1, 5, 3, 2, 6, 3]
    nums = [random.randint(0, 100) for _ in range(10)]

    print(bogo_sort(nums))