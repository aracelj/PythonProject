from multiplication_table import multiply


def test_multiplication_table():
    assert multiply(3, 4) == [3,6,9,12]
    assert multiply(2, 5) == [2, 4, 6, 8, 10]
