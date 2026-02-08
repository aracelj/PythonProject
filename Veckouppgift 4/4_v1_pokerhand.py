# Exercise 4 Pokerhand Version 1 by Araceli Jakobsson
# Version 1 Programs that randomize a card that will return the rank(2-14) and suit(Diamonds, Clubs, Spades, Hearts)

import my_string_module
import random
card_counter = 1
my_cards = my_string_module.my_poker(card_counter)                  #fetching the players random cards
print(f"Your card: {my_cards} ")
