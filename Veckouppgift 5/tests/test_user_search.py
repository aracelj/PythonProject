from user_search import autocomplete_list

"""
def test_autocomplete_list__red():
   assert autocomplete_list("ann", ("Hannah", "Maria", "Ann", "Joseph")) == True
   but gives an error since by default it is case sensitive and the master list must be converted to lowercase
"""


def test_autocomplete_list():
    assert autocomplete_list("ann", ["Hannah", "Maria", "Ann", "Joseph"]) == True
    assert autocomplete_list("Ann", ["Hannah", "Maria", "Ann", "Joseph"]) == True
    assert autocomplete_list("ANN", ["Hannah", "Maria", "Ann", "Joseph"]) == True
    assert autocomplete_list("Onin", ["Hannah", "Maria", "Ann", "Joseph"]) == False
    assert autocomplete_list("", ["Hannah", "Maria", "Ann", "Joseph"]) == None