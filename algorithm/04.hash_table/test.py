from find_pair import get_pair, get_pair_half_sum

def test_get_pair():
    # 正常系: ターゲットを満たすペアが存在する場合
    assert get_pair([11, 2, 5, 9, 10, 3], 12) == (2, 10)
    assert get_pair([1, 4, 6, 8], 10) == (4, 6)
    assert get_pair([5, 1, 2, 7], 8) == (1, 7)

    # 異常系: ターゲットを満たすペアが存在しない場合
    assert get_pair([1, 2, 3], 10) is None
    assert get_pair([], 5) is None
    assert get_pair([3], 3) is None

def test_get_pair_half_sum():
    # 正常系: 合計の半分を満たすペアが存在する場合
    assert get_pair_half_sum([11, 2, 5, 9, 10, 3]) == (9, 11)
    assert get_pair_half_sum([4, 6, 8, 2]) == (4, 6)

    # 異常系: 合計の半分を満たすペアが存在しない場合
    assert get_pair_half_sum([1, 3, 5]) is None
    assert get_pair_half_sum([7]) is None
    assert get_pair_half_sum([]) is None

    # 合計が奇数の場合はペアが存在しない
    assert get_pair_half_sum([1, 2, 4]) is None

"""
================================================= test session starts ==================================================
platform linux -- Python 3.13.0, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/omz/prog_dir/py_dir/py_retrospect/algorithm/04.hash_table
collected 2 items

test.py ..                                                                                                       [100%]

================================================== 2 passed in 0.00s ===================================================
"""