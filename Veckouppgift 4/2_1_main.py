# Exercise 2 Creating modules  by Araceli Jakobsson

import my_string_module

#1 Calling the string function
print("====== 1 String Module ====== ")
my_input = input("Enter a string: ")
my_output = my_string_module.string_parameter(my_input)


#2a Calling the echo function
print("====== 2a Echo Module ====== ")
my_input = input("Echo: ")
my_output = my_string_module.string_echo(my_input)

#2b Calling the echo function with counter
print("====== 2b Echo Module with a counter ====== ")
my_input1 = input("Echo: ")
#my_input2 = input("Counter: ")
my_input2 = ""
my_counter = my_string_module.checker_counter(my_input2)
my_output = my_string_module.echo_counter(my_input1,my_counter)


