# Exercise 4 Pokerhand Version 1 by Araceli Jakobsson
# Version 3b Programs that randomize 5 cards with the suit(diamond, club, heart,spade) and value from 2 to ace(2 - 14)
# Program will evaluate what card has the player with whether it is:
# 1 pair, 2 pairs, 3 of a kind, straight, flush, full house, four of a kind, straight flush, fives(no combination found)

import my_string_module
import random

print("===== Pokerhand version 3b =====")
card_counter = 5
my_cards = my_string_module.my_poker(card_counter)
print("Your cards:")
for value, suit in my_cards:                                       #fetching the players random cards
    print(f"  {my_string_module.card_name(value)} of {suit}")

result = my_string_module.evaluate_hand_simple(my_cards)
print(f"You got {result} ")
