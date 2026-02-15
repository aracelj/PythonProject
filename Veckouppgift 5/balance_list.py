"""
Case: The function takes two list and balance the two list accordingly, that is moving some of elements to the next list that has elements.
Requirements:
    1. The function takes two input list
    2. It moves the element to the list that has the least elements and make it equal as much as possible.
    3. It handles an empty list.
    4. It modifies the list to return the updated lists.
Acceptance Criteria:
    1. Accepts two input lists
    2. It should balance the number of elements in the two lists as much as possible.
    3. If it has equal no. of elements, it returns True.
    4. After balancing, if the no. of elements is still not equal, then it returns False
    5. After balancing, if the no. of elements is still equal, then it returns True
    6. It should handle for two empty list, then it returns None.
"""
def balance_list__green(list1,list2):
    lista1 = [str(item).replace(","," ").split() for item in list1]     #copying to another list name,converting to string, replacing,"," to space and removing it
    lista2 = [str(item).replace(","," ").split() for item in list2]     #copying to another list name,converting to string, replacing,"," to space and removing it
    counter1 = len(lista1)
    counter2 = len(lista2)
    counter_diff = abs(counter1 - counter2) // 2
    if counter1 == 0 and counter2 == 0:                                 #checking if two lists are empty
        return None
    if counter1 > counter2:                                             #checks if list1 has more elements than list2
        for i in range(counter_diff):
            lista2.append(lista1[-1])                                   #appending the end element of list1 to list2
            lista1.pop()                                                #removing the last element of list1
    elif counter1 < counter2:                                           #checks if list2 has more elements than list1
        for i in range(counter_diff):
            lista1.append(lista2[-1])                                   #appending the end element of list2 to list1
            lista2.pop()                                                #removing the last element of list2

    return len(lista1) == len(lista2)


def balance_list__refactor(list1,list2):
    lista1 = [str(item).replace(","," ").split() for item in list1]
    lista2 = [str(item).replace(","," ").split() for item in list2]
    counter1 = len(lista1)
    counter2 = len(lista2)
    counter_diff = abs(counter1 - counter2) // 2
    if counter2 == 0 and counter2 ==0:
        return None
    if counter1 > counter2:
        for i in range(counter_diff):
            lista2.append(lista1.pop())
    elif counter1 < counter2:
        for i in range(counter_diff):
            lista1.append(lista2.pop())
    return len(lista1) == len(lista2)



