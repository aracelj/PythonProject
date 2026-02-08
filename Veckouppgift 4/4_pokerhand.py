# Exercise 4 Pokerhand by Araceli Jakobsson
# Version 1 Programs that randomize 5 cards with the suit(diamond, club, heart,spade) and value from 2 to ace(2 - 14)
# Program will evaluate what card the player has

import my_string_module
import random
card_counter = 5
my_cards = my_string_module.my_poker(card_counter)
print("Your cards:")
for value, suit in my_cards:                                       #fetching the players random cards
    print(my_string_module.card_name(value), "of", suit)

result = my_string_module.evaluate_hand_simple(my_cards)
print(f"You got {result} ")

