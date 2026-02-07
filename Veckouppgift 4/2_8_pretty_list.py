# Exercise 2_8 Function module by Araceli Jakobsson
# Build a function that will print out how many elements in the list and display in enumerated form

import my_string_module

user_input = input ("Enter list elements (separated by spaces or commas): ")
elements = user_input.replace(",", " "). split()                               #replace the entered space or comma with space and seprate it
my_string_module.my_list(elements)
