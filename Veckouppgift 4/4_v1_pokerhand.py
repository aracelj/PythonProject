# Exercise 4 Pokerhand Version 1 by Araceli Jakobsson
# Version 1 Programs that randomize 5 cards with the suit(diamond, club, heart,spade) and value from 2 to ace(2 - 14)

import my_string_module
import random

hand = my_string_module.my_poker()

print("Your cards:")
for value, suit in hand:
    print(my_string_module.card_name(value), "of", suit)

result = my_string_module.my_poker_evaluation(hand)
print("\nHand evaluation:", result)
