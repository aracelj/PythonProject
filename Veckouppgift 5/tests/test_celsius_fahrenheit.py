

from U2_1a_celsius_fahrenheit import celsius_fahrenheit




def test_celsius_fahrenheit():
    assert celsius_fahrenheit(0) == 32
    assert celsius_fahrenheit(100) == 212
    assert celsius_fahrenheit(-273.2) == None
