from U2_3ato3c_find_median import find_median
from pytest import approx



def test_find_median():
    assert find_median([1, 102, 3, 100, 5]) == 5
    assert find_median([]) == None
    assert find_median([1, 2, 3, 4]) == approx(2.5)


