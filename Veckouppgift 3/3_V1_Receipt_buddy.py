# Exercise 3 Receipt Buddy by Araceli Jakobsson
# The program will repeatedly ask for an amount until the user enters quit.
# When user enter quit, then it will display the sum of all the amounts entered

# 3 Receipt Buddy
print("==== Welcome to the Receipt Buddy! =====")
amount = 0
amount_sum = 0
amount_input = input("Enter an amount or 'q' to quit:: ")
while amount_input.lower() != 'q':                                  # checks if input is not equal to q or Q
    amount = float(amount_input)                                    # converts the input to float
    amount_sum += amount                                            # adds the amount
    amount_input = input("Enter an amount or 'q' to quit: ")

print("That makes", amount_sum," SEK in total. Welcome back! ")     #computes all the amount

