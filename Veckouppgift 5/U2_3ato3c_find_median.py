

def find_median(numbers):
    numbers.sort()
    if len(numbers) == 0:
        return None
    elif len(numbers) % 2 == 0:
        number1 = numbers[len(numbers) // 2] - 1
        number2 = numbers[len(numbers) // 2]
        median = (number1 + number2) / 2
        return median
    else:
        median = numbers[len(numbers) // 2]
    return median