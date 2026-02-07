# Exercise 2_4 Last function from a module by Araceli Jakobsson
#Call a function and take a list as a parameter and return last element of the list

#2_4 Function to output the last element of the list
import my_string_module

last = [1,2,3]
my_output = my_string_module.last(last)                   #calling last function from my_string_module
print(f"Last element of the list: {my_output}")