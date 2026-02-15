from list_balance import balance_list, balance_list_refactor


def test_balance_list_red():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list2 = ["hi", "banana", 1]
    result = balance_list(list1, list2)
    assert result == False


def test_balance_list_green1():
    list1 = [1,2,3,4,5,6,7,8]
    list2 = ["hi","banana", 1, 2]
    result = balance_list(list1, list2)
    assert result == True


def test_balance_list_green2():
    list1 = [1,2,3,4]
    list2 = ["hi","banana", 1, 2]
    result = balance_list(list1, list2)
    assert result == "Balance"


def test_balance_list_refactor():
    list1 = [1,2,3,4,5,6,7,8]
    list2 = ["hi","banana", 1, 2]
    result = balance_list_refactor(list1, list2)
    assert result == True
