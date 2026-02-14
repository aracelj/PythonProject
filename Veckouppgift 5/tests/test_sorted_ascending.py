from U2_4ato4c_sorted_ascending import sorted_ascending




def test_sorted_ascending():
    assert sorted_ascending([1, 102, 3, 100, 5]) == False
    assert sorted_ascending([1, 2, 3, 4, 6]) == True