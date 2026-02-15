from multiply_table import multiplication_table__green, multiplication_table__refactor

"""
def test_multiplication_table__red():
    assert multiplication_table__green(3, 4) == [3,6,9,12] = Error since the n and limit input were not converted to integers
    
"""


def test_multiplication_table():
    assert multiplication_table__green(3, 4) == [3,6,9,12]
    assert multiplication_table__green(3, 0) == []
    assert multiplication_table__refactor(2, 5) == [2, 4, 6, 8, 10]
