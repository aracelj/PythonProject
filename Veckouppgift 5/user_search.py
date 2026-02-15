"""

Task: To create a function that searches for a user input name inside the master list.

Requirements:
    1. The function must have a list of names called master list
    2. The function must accept a string that will be the name to search
    3. The function must search the master list for the exact name entered but matches lowercase or uppwercase
    4. If the name is found in the master list, return True.
    5. If the name is not found in the master ist, return False.
    6. The function must not change the original master list.

Acceptance Criteria:
    1. User enters a name to search.
    2. The system searches the name in master list.
    3. The search is an exact match required but accepts lowercase or uppercase ex. "Ann" matches "ann"
    4. If the name exists in the master list, the function returns True.
    5. If the name does not exists in the master list, the function returns False.
    6. The original master list remains unchanged.
"""
  

def autocomplete_list(user_input, master_list):
    name_input = user_input.strip().lower()
    master = [name.lower() for name in master_list]

    for item in master:
        if name_input == item:
            return True

    return False

