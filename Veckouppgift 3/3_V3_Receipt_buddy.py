# Exercise 3_version 3 Receipt Buddy by Araceli Jakobsson
# The program will repeatedly ask for an amount until the user enters quit.
# When user enter quit, then it will display the sum of all the amounts entered
# User is asked for how many person, tips and display the total amount with tips and per person.

# 3_V3 Receipt Buddy

print("==== Welcome to the Receipt Buddy version 3! =====")
amount = 0
amount_sum = 0
final_sum = 0
tips = 0
additional_tips = 0
total_tips = 0
while True:
    amount_input = input("Enter an amount or 'q' to quit: ")
    if amount_input.lower() == 'q':                                     # checks if input is not equal to q or Q
        break
    if (amount_input < '0') or (amount_input > '9'):                    # checks for input is other than numbers
        print("Invalid input!")
    else:
        amount = float(amount_input)                                    # converts the input to float
        amount_sum += amount                                            # adds the amount

while True:
    person_count = input("How many persons are you? ")                  # number of person
    try:
        if person_count.isdigit() == False:
            print("Invalid. Please enter a whole number.")
        else:
            person_count = int(person_count)
            payment_sum = amount_sum/person_count
            break
    except ValueError:
        print("Invalid number. Please enter a number.")
    except ZeroDivisionError:
        print("No. of persons cannot be 0.")

while True:
    tips = input("How much tips (10% default): ")                        # ask for the tips
    try:
        if tips == '' or tips == ' ':                                    # checks for empty entry
            total_tips = 10
            break
        if tips.isdigit() == True:                                       # takes only number entry
            additional_tips = int(tips)
            total_tips = additional_tips + 10
            break
        else:
            print("Invalid. How much tips (10% default): ")
            break

    except ValueError:
        print("Invalid number. Please enter a number.")

final_sum = amount_sum + ((total_tips/100) * amount_sum)                    # computes for the final sum with tips
amount_pay = final_sum / person_count                                       # computes for the final pay per person
print("Total amount: ", amount_sum, "kr")
print(f"Total Tips (Default 10% + {additional_tips}%): ", total_tips, "%")
print(f"That makes {final_sum:.2f} kr in total plus tips , also {amount_pay:.2f} kr per person. Welcome back! ")






