# Exercise 2 Creating modules  by Araceli Jakobsson
#1 Calling a string function
#2a Calling the function and echo a string twice
#2b Calling a function and echo a string with a variable counter to output the string

import my_string_module

#1 Calling the string function
print("====== 1 String Module ====== ")
my_input = input("Enter a string: ")
my_output = my_string_module.string_parameter(my_input)          # calling string_parameter to output a string attaching a phrase"is a whiz at programming"


#2a Calling the echo function
print("====== 2a Echo Module ====== ")
my_input = input("Echo: ")
my_output = my_string_module.string_echo(my_input)               # calling string_echo function to output a string

#2b Calling the echo function with counter
print("====== 2b Echo Module with a counter ====== ")
my_input1 = input("Echo: ")
#my_input2 = input("Counter: ")
my_input2 = ""
my_counter = my_string_module.checker_counter(my_input2)         # calling checker_counter function to accepts only numbers
my_output = my_string_module.echo_counter(my_input1,my_counter)  # calling echo_counter function to output a string with a counter


