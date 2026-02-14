
def find_max__not_empty(list_number2):
    counter = len(list_number2)
    max_number = list_number2[0]
    for i in range(1,counter):
        number = list_number2[i]
        if max_number > number:
            max_number = max_number
        elif max_number == number:
            max_number = number
        else:
            max_number = number
    return max_number

def find_max__green(list_number):
    counter = len(list_number)
    if counter == 0:
        return 0
    else:
        return find_max__not_empty(list_number)


def find_max__not_empty_refactor(list_number2):
    max_number = max(list_number2)
    return max_number

def find_max__refactor(list_number):
    counter = len(list_number)
    if counter == 0:
        return 0
    else:
        return find_max__not_empty_refactor(list_number)







