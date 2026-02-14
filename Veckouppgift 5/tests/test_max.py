from U1_4_max import find_max__green, find_max__refactor




def test_find_max__green():
    assert find_max__green([1, 102, 3, 100, 3]) == 102
    assert find_max__green([]) == 0

def test_find_max__refactor():
    assert find_max__refactor([1, 102, 3, 100, 3]) == 102
    assert find_max__refactor([]) == 0

