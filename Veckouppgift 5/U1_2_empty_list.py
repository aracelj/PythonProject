#2 Test cases by Araceli Jakobsson
""""
Original code:
# Returnerar summan av alla tal i listan
def sum_list(list):
    return None

def test_empty_list():
    expected = # ???
    actual = # ???
    assert actual == expected

def test_number_list():
# TODO: testa med listor som har ett, två respektive fem element.
Passert sum_list([5]) == 5
Passert # ???
Passert # ???
"""
import pytest


def sum_list(lista):
    total = 0
    for item in lista:
        total += item
    return total

def test_empty_list():
    expected = 134
    actual = sum_list([1,3,100,20,10])
    assert actual == expected


def test_number_list():
# TODO: testa med listor som har ett, två respektive fem element.
    assert sum_list([5]) == 5
    assert sum_list([1,2]) == 3
    assert sum_list([1,2,3,4,5]) == 15

