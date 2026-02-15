"""

Task: To create a function that searches for a user input name inside the master list.

Requirements:
    1. The function must have a list of names called master list
    2. The function must accept a string that will be the name to search
    3. The function must search the master list for the exact name entered but matches lowercase or uppercase
    4. The function must handle empty strings as input.
    5. If the name is found in the master list, returns True.
    6. If the name is not found in the master ist, returns False.
    7. The function must not change the original master list.

Acceptance Criteria:
    1. Accepts a user name to search.
    2. The system searches the name in master list.
    3. The search is an exact match required but accepts lowercase or uppercase ex. "Ann" matches "ann"
    4. If the name exists in the master list, the function returns True.
    5. If the name does not exists in the master list, the function returns False.
    6. If the user name input is empty, the function returns None.
    7. The original master list remains unchanged.
"""
  

def autocomplete_list(user_input, master_list):
    name_input = user_input.strip().lower()                  #removes spaces within the input and converts to lowercase
    master = [name.lower() for name in master_list]          #converts the master_list to lowercase
    if len(name_input) == 0:
        return None
    else:
        for item in master:
            if name_input == item:                           #checks if it match and returns True
                return True

    return False                                             #if it does not match, returns false

