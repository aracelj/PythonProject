# Exercise 1d Function  by Araceli Jakobsson

"""
Original code:
def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))          # x = 10 + y = 15 so fun2(25)
print(a)


Output will be:
125

"""

def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))          # x = 10 + y = 15 so fun2(25) and pass the value to the function fun2
print(a)