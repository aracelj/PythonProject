from balance_list import balance_list__green, balance_list__refactor

"""
TDD_red
def test_balance_list_red():
    result = balance_list__green([1, 2, 3, 4, 5, 6, 7, 8], ["hi", "banana", 1])
    assert result == True      #returns an error as the the return should be False
"""
def test_balance_list_red():
    assert balance_list__green([1, 2, 3, 4, 5, 6, 7, 8], ["hi", "banana", 1]) == False


def test_balance_list_green():
    assert balance_list__green([1,2,3,4,5,6,7,8], ["hi","banana", 1, 2]) == True
    assert balance_list__green([], ["hi", "banana", 1]) == False
    assert balance_list__refactor([], []) == None

def test_balance_list__refactor():
    assert balance_list__refactor([1,2,3,4,5,6,7,8], ["hi","banana", 1, 2]) == True
    assert balance_list__refactor([], ["hi", "banana", 1]) == False
    assert balance_list__refactor([], []) == None


