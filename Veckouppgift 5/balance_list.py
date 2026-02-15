
def balance_list(list1,list2):
    lista1 = [str(item).replace(","," ").split() for item in list1]
    lista2 = [str(item).replace(","," ").split() for item in list2]
    counter1 = len(lista1)
    counter2 = len(lista2)
    if counter1 > counter2:
        counter_diff = (counter1 - counter2)//2
        for i in range(counter_diff):
            lista2.append(lista1[-1])
            lista1.pop()
    elif counter1 < counter2:
        counter_diff = (counter2 - counter1) // 2
        for i in range(counter_diff):
            lista1.append(lista2[-1])
            lista2.pop()
    else:
        counter_diff = 0
    return len(lista1) == len(lista2)


#archive_list.append(archive_item)  # added to the archive list
#list.remove(archive_item)