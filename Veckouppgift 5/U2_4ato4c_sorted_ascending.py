""" 
4a. Equivalence class = sorted list ex. 1,3,5,100,102
4b Case: It will take a list and sort it in ascending order.
         If the inputted list is not sorted in ascending then returns false otherwise true.
   Requirements:
         1. The function must take a list of numbers
         2. It will return true if its in ascending order otherwise false
         3. The function must handle an empty list and returns None
   Acceptance Criteria:
         1. Accepts a list of ascending order and returns True
         2. Accepts a non-sorted list and returns False.
         3. Accepts an empty list and returns None.
"""

def sorted_ascending(lista):
    if len(lista) == 0:                   #checks for empty list
       return None
    else:
       return lista == sorted(lista)      #sorting in ascending