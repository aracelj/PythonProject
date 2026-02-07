# Exercise 2_6 Function module by Araceli Jakobsson
# Resolve the error in the code
"""
Original code:
def increase(x):
    return x                               # any code after return statement will not be executed
    x += 1

print(increase(1))
"""
print("====== Original Output ======")
def increase(x):
    return x                              # any code after return statement will not be executed
    x += 1                                # not executed due to prior return statement

print(increase(1))


print("====== Updated Output ======")
def increase(x):
    x += 1                                # 1 + x
    return x                              # returns the value of x

print(increase(1))
