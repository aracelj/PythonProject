# Exercise 3 Receipt Buddy by Araceli Jakobsson
# The program will repeatedly ask for an amount until the user enters quit.
# When user enter quit, then it will display the sum of all the amounts entered

# 3 Receipt Buddy
print("===== Welcome to the Receipt Buddy! version 1 =====")
amount = 0
amount_sum = 0
while True:
    amount_input = input("Enter an amount or 'q' to quit: ")

    if amount_input.lower() == 'q':                                          # converts input to lowercase
        break                                                                # exits the program
    if (amount_input <'0') or (amount_input > '9'):
        print("Invalid input!")
    else:                                     # checks for whole number
            amount = float(amount_input)                                    # converts the input to float
            amount_sum += amount                                            # adds the amount

print("That makes", amount_sum, "SEK in total. Welcome back! ")  # computes all the amount

