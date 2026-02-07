# Exercise 2_7 Function module by Araceli Jakobsson
# Build a function named average and outputs the average of the two numbers entered

import my_string_module

x = my_string_module.number_input("Enter value of x: ")        # calls the function number_input allowing only number input, no zero for x
y = my_string_module.number_input("Enter value of y: ")        # calls the function number_input allowing only number input, no zero for y
my_average = my_string_module.average(x,y)                     # taking the average of x & y
print(f"({x} + {y}) /2, which will be {my_average}")
