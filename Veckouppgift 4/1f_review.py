# Exercise 1f Function  by Araceli Jakobsson

"""
Original code:
def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)

Output will be:

"""

def foo(i):
    return 2*i*i                        # 2 * 3 * 3

def goo(x, y):
    return x(y)                         # x(3)

a = goo(foo, 3);                        # a = return value (18) from foo function
print(a)


