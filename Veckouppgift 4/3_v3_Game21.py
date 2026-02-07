# Exercise 3 Game 21 Version 3 by Araceli Jakobsson
# Version 3 Programs ask if wants to get another card (random number) or to stays
# Prints the first number in the series that is bigger than card

import random
import my_string_module

print("======== Game 21 Ver.3 ========")
random_input = random.randint(1, 13)
print(f"Random no.: {random_input} ")
my_output = my_string_module.my_game2(random_input)