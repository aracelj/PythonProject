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
tips_fin = 0.0
tips_percentage = 0.0
amount_input = input("Enter an amount or 'q' to quit:: ")
while amount_input.lower() != 'q':                                  # checks if input is not equal to q or Q
    amount = float(amount_input)                                    # converts the input to float
    amount_sum += amount                                            # adds the amount
    amount_input = input("Enter an amount or 'q' to quit: ")

person_count = float(input("How many persons are you? "))           # number of person
tips = input("How much tips (10% default): ")

if tips == "":                                                      # checks for tips if blank
    tips_percentage = 10
else:                                                               # if tips if not blank
    tips_percentage = float(tips)
    if tips_percentage < 10:                                        # if tips is less than 10
        tips_percentage = 10

final_sum = amount_sum + ((tips_percentage/100) * amount_sum)       # computes for the final sum with tips
amount_pay = final_sum / person_count                               # computes for the final pay per person
print("Total amount: ", amount_sum, "kr")
print("Tips applied :", tips_percentage, "%")#divides the amount per person
print(f"That makes {final_sum:.2f} kr in total plus tips , also {amount_pay:.2f} kr per person. Welcome back! ")