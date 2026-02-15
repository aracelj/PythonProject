from user_search import autocomplete_list




def test_autocomplete_list():
    assert autocomplete_list("ann", ["Hannah", "Maria", "Ann", "Joseph"]) == True
    assert autocomplete_list("Ann", ["Hannah", "Maria", "Ann", "Joseph"]) == True
    assert autocomplete_list("Onin", ["Hannah", "Maria", "Ann", "Joseph"]) == False