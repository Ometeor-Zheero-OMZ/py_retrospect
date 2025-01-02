from typing import List, Tuple, Optional

def get_pair(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    # 数字を一時的に保持する (数字はユニークで保持される)
    cache = set()

    for num in nums:
        # target を満たすために必要な値を計算
        val = target - num
        # 必要な値がすでにセットに含まれている場合はペアを返す
        if val in cache:
            return val, num

        # 現在の数字をセットに追加
        cache.add(num)

def get_pair_half_sum(nums: List[int]) -> Optional[Tuple[int, int]]:
    sum_nums = sum(nums)

    # 合計値と余りを計算
    half_sum, remainder = divmod(sum_nums, 2)
    # 合計値が奇数の場合はペアが存在しないため処理を終了
    if remainder != 0:
        return

    cache = set()
    for num in nums:
        # 現在の数字をセットに追加
        cache.add(num)
        # ペアを探すために必要な値を計算
        val = half_sum - num
        # 必要な値がセット内にあればペアを返す
        if val in cache:
            # return val, num
            # 小さい順に並べて返す
            return tuple(sorted([val, num]))

if __name__ == "__main__":
    l = [11, 2, 5, 9, 10, 3]
    t = 12
    # (2, 10)
    print(get_pair(l, t))

    l = [11, 2, 5, 9, 10, 3]
    # (11, 9)
    print(get_pair_half_sum(l))