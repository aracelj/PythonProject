

def find_median(numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) %2 == 0:
        number1 = numbers[len(numbers) // 2] - 1
        number2 = numbers[len(numbers) // 2]
        average = (number1 + number2) / 2
        return average
    else:
        average = numbers[len(numbers) // 2]
    return average