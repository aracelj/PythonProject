# Exercise 3 Game 21 Version 3 by Araceli Jakobsson
# Version 3 Programs computers card and players card.
# Player has an option to change card or stay and if player's card is greater than computer end of game otherwise it continues.

import random
import my_string_module

print("======== Game 21 Ver.3 ========")
computer = random.randint(1, 13)
print(f"Computer's card: {computer} ")
my_output = my_string_module.my_game3(computer)