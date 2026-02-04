# Exercise 1g Function  by Araceli Jakobsson

"""
Original code:
def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

To improve the code:
perhaps print the value to determine which input falls as integer or float.

"""

def is_number(x):
    if isinstance(x, int):                          # if x is an integer then it returns True
        print(x, type(x))
        return True

    elif isinstance(x, float):                      # if x is a float then it returns True
        print(x, type(x))
        return True
    return False                                    # if x neither integer or float then it returns False

print(is_number(5.5))
print(is_number(42))