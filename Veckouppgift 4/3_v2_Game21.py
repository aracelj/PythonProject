# Exercise 3 Game 21 Version 2 by Araceli Jakobsson
# Version 2 Programs enter randomize number and if its greater than random number then stops the game
# Prints the first number in the series that is bigger than random number

import random
import my_string_module

print("======== Game 21 Ver.2 ========")
random_input = random.randint(1, 13)
my_output = my_string_module.my_game2(random_input)