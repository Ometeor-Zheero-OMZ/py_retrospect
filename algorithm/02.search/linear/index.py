"""
Linear Search
In computer science, linear search or sequential search is a method for finding an element within a list.
It sequentially checks each element of the list until a match is found or the whole list has been searched.

"""
from typing import List, NewType

IndexNum = NewType('IndexNum', int)

def linear_search(nums: List[int], val: int) -> IndexNum:
    for i in range(len(nums)):
        if nums[i] == val:
            return i

    return -1

if __name__ == "__main__":
    nums = [0, 1, 5, 7, 9, 11, 15, 20, 24]

    print(f"Index of elements in list is: nums[{linear_search(nums, 0)}]")