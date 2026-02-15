from U1_5_max_2nd import find_2nd_max

def test_find_max_2nd():
    assert find_2nd_max([1, 102, 3, 100, 3]) == 100
    assert find_2nd_max([]) == 0