"""
Case: The function will give the multiplication table with parameters of a number and limits.
Requirements:
      1. Take 2 inputs, 1 for the table number, another as the limits of the multiple
      2. The function must return the multiplication table for n from 1 up to limit.
      4. It must return the table as a list of numbers.
      5. It must handle positive integers for both n and limit.
      6. It must handle limit = 0 and returns an empty list
Acceptance Criteria:
      1. Accepts two integer numbers, and returns the multiplication table according to its limits.
      2. Accepts limits = 0, returns an empty list
      3. The return value must be in a list of numbers, not a string""

"""

def multiplication_table__green(n, limit):
    output = []
    n = int(n)                               #converts to integer
    limit = int(limit)                       #converts to integer
    if limit == 0:
        return output
    for i in range(1, limit + 1):            #multiplying the number with its limit
        result = n * i
        output.append(result)                #save the result at the end of the list
    return output


def multiplication_table__refactor(n, limit):
    output = []
    n = int(n)                               #converts to integer
    limit = int(limit)                       #converts to integer
    for i in range(1, limit + 1):            #multiplying the number with its limit
        output.append(n * i)                 #save the result at the end of the list
    return output


