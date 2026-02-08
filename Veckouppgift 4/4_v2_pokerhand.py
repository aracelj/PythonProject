# Exercise 4 Pokerhand Version 2 by Araceli Jakobsson
# Version 2 Programs that randomize a card (2-14) and suit(Diamonds, Clubs, Spades, Hearts)
# Outputs if there two cards with the same value

import my_string_module
import random

card_counter = 2
version = 2
my_cards = my_string_module.my_poker(card_counter)                  #fetching the players random cards
print("You cards: ")
for value, suit in my_cards:
    print(f"  {value} of {suit}")                #calling the function card_name in the module

result = my_string_module.my_poker_evaluation2(my_cards,version)            #check if two cards is the same
print(f"Hand Evaluation: {result}")
