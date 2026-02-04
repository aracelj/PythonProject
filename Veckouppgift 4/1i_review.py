# Exercise 1i Function  by Araceli Jakobsson

"""
Original code:
def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

1. To find and return the smallest number in a list
2. The results for the following list:
   1st list result: -11
   2nd list: 0 as it is empty
   3rd list: 0 as the list contains 1 element and will directly print out the counter 0 as it does not qualify to execute the if condition.

"""

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])

# developing the code
print("\n======== Updated Output ========  ")
def find_min(numbers):
    if len(numbers) == 0:                                 # checks if list is empty
        print("The list is empty!")
        return None
    counter = numbers[0]
    for item in numbers:
        if item < counter:                                # take the value of counter as smallest
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])
find_min([])
find_min([100])