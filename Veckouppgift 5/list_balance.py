def balance_list(list1,list2):
    lista1 = [str(item).replace(","," ").split() for item in list1]
    lista2 = [str(item).replace(","," ").split() for item in list2]
    counter1 = len(lista1)
    counter2 = len(lista2)
    if counter1 > counter2:
            counter_diff = (counter1 - counter2)//2
            if counter_diff != 0:
                for i in range(counter_diff):
                    lista2.append(lista1[-1])
                    lista1.pop()
            else:
                print(f"list1: {lista1} has more elements than List2: {lista2}")

    elif counter1 < counter2:
            counter_diff = (counter2 - counter1) // 2
            if counter_diff != 0:
                for i in range(counter_diff):
                    lista1.append(lista2[-1])
                    lista2.pop()

            else:
                print(f"list2: {lista2} has more elements than List1: {lista1}")
    else:
            return "Balance"

    return len(lista1) == len(lista2)


def balance_list_refactor(list1,list2):
    lista1 = [str(item).replace(","," ").split() for item in list1]
    lista2 = [str(item).replace(","," ").split() for item in list2]
    counter1 = len(lista1)
    counter2 = len(lista2)
    counter_diff = (counter1 - counter2) // 2
    for i in range(counter_diff):
        counter1 = len(lista1)
        counter2 = len(lista2)
        if counter1 > counter2:
                lista2.extend(lista1[-counter_diff])
                lista1.pop()
        elif counter1 < counter2:
                lista1.append(lista2[-counter_diff])
                lista2.pop()

    return len(lista1) == len(lista2)

