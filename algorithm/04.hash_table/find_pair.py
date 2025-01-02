from typing import List, Tuple, Optional

def get_pair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    cache = set()

    for num in nums:
        val = target - num
        if val in cache:
            return val, num

        cache.add(num)

def get_pair_half_sum(nums: List[int]) -> Optional[Tuple[int, int]]:
    sum_nums = sum(nums)

    half_sum, remainder = divmod(sum_nums, 2)
    if remainder != 0:
        return

    cache = set()
    for num in nums:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num

if __name__ == "__main__":
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    # (2, 10)
    print(get_pair(l, t))

    l = [11, 2, 5, 9, 10, 3]
    # (11, 9)
    print(get_pair_half_sum(l))