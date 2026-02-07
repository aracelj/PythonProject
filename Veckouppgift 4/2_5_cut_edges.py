# Exercise 2_5 Cut edges function from a module by Araceli Jakobsson
# Call a function and take a list as a parameter and return a new list without the first and last element

#2_5 Calling a function and outputs a new list removing the first and last element of the original list
import my_string_module

cut_edges = [1,2,3,4]
my_output = my_string_module.cut_edges(cut_edges)              #calling cut_edges function from my_string_module to remove the 1st and last element
print(f"Original list: {cut_edges}")
print(f"Current list: {my_output}")

