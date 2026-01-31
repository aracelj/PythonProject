# Exercise 3_version 2 Receipt Buddy by Araceli Jakobsson
# The program will repeatedly ask for an amount until the user enters quit.
# It will also ask for how many persons are there and splits the payment per person.

# 3_V2 Receipt Buddy
print("===== Welcome to the Receipt Buddy version 2! =====")
amount = 0
amount_sum = 0

while True:
    amount_input = input("Enter an amount or 'q' to quit: ")
    if amount_input.lower() == 'q':                                     # checks if input is not equal to q or Q
        break
    if (amount_input < '0') or (amount_input > '9'):
        print("Invalid input!")
    else:
        amount = float(amount_input)                                    # converts the input to float
        amount_sum += amount                                            # adds the amount

while True:                                                             # while true , it executes
        person_count = input("How many persons are you? ")              # number of person
        try:
            if person_count.isdigit() != True:                          # checks for valid input
                print("Invalid input! Enter a number.")
            else:
                person_count = int(person_count)                        # converts to float
                amount_pay = amount_sum / person_count                  # divides the amount per person
                break
        except ZeroDivisionError:                                       # Handles /0 error
            print("No. of persons cannot be 0.")

print(f"That makes {amount_sum:.2f} kr in total, also, {amount_pay:.2f} kr per person. Welcome back! ")  # computes all the amount
