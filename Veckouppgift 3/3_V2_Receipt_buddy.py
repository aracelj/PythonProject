# Exercise 3_version 2 Receipt Buddy by Araceli Jakobsson
# The program will repeatedly ask for an amount until the user enters quit.
# When user enter quit, then it will display the sum of all the amounts entered

# 3_V2 Receipt Buddy
print("==== Welcome to the Receipt Buddy version 2! =====")
amount = 0
amount_sum = 0
amount_input = input("Enter an amount or 'q' to quit:: ")
while amount_input.lower() != 'q':                                  # checks if input is not equal to q or Q
    amount = float(amount_input)                                    # converts the input to float
    amount_sum += amount                                            # adds the amount
    amount_input = input("Enter an amount or 'q' to quit: ")

person_count = float(input("How many persons are you? "))           # number of person
amount_pay = amount_sum / person_count                              #divides the amount per person
print("That makes", amount_sum," kr in total, also", amount_pay, "kr per person. Welcome back! ")     #computes all the amount