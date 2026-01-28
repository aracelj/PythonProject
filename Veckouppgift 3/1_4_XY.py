# Exercise 1_4 X & Y Output by Araceli Jakobsson
# What is the output of x and y using breakpoint and debugging
"""
x =0
y = 1
while y < 10:
    if y % 2 == 0:
        x -= y
    else:
        x += y * y
    y +=1

Value of x & y will be:
x   0  1   -1  8  4  29 23  72   64   145
y   1  2   3   4  5  6   7   8    9   10
"""

# 4 Output the value of x and y using breakpoint and debugging
x =0
y = 1
while y < 10:
    if y % 2 == 0:
        x -= y
    else:
        x += y * y
    y += 1