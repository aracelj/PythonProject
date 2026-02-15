"""
3a
Case: Take the median of a list and if the elements are even, the median will be the average of two median elements
Requirements:
       1. The function must find the median.
       2. It takes a list of numbers
       3. The list of numbers is sorted to find the median.
       4. If the elements of the list is even, it will take the average of two median elements
       5. If the elements is odd then it takes the median of the list.
       6. The function must return a numeric value int or float
       7. The function also identifies if its an empty list.
       8. The function will not modify the original list.
Acceptance Criteria:
       1. Accepts an odd element list, takes the median element and return the value.
       2. Accepts an even element list, takes the average of 2 two median element and returns the value in int or float.
       3. Accepts an empty list and returns None
"""

def find_median(number_list):
    numbers = number_list.copy()                      #copying the list and keep the original list
    numbers.sort()
    if len(numbers) == 0:                               #for empty list
        return None
    elif len(numbers) % 2 == 0:                         #even elements
        number1 = numbers[len(numbers) // 2] - 1        #taking the first middle number
        number2 = numbers[len(numbers) // 2]            #taking the 2nd middle number
        median = (number1 + number2) / 2                #taking the average of 2 middle numbers
        return median
    else:                                               #odd elements
        median = numbers[len(numbers) // 2]
    return median