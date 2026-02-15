
def find_2nd_max(list_number):
    counter = len(list_number)
    if counter == 0:                         #if list is empty
        return 0
    else:
        max_value = max(list_number)         #finding the first max value
        list_number.remove(max_value)        #remove the max value
        return max(list_number)              #returns the 2nd max value



