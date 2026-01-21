# Uppgift 5 Mini Calculator by Araceli Jakobsson
# 1 User is ask to enter 3 numbers and display the sum
# 2 Determines the highest among the 3 inputted number without using max function
# 3 Give the counts of all the numbers that are the same
# 4 Displays the middle number only if all three numbers are different or all are the same. Otherwise it will not count it as middle no. Display in a table format



# 1 User is ask to enter 3 numbers and display the sum
print("========================== Sum of 3 Numbers =============================")
number_1= float(input("First number: "))
number_2= float(input("Second number: "))
number_3= float(input("Third number: "))
total = number_1 + number_2 + number_3
print("Sum of all 3 numbers: ", round(total,2))

# 2 Determines the highest among the 3 inputted number without using max function
print("\n============================= Maximum Number ============================")
max_number = 0
counter_same = 0
middle_number = 0
alike_2 = 0
alike_3 = 0
alike_2 = "no"
alike_3 = "no"
if number_1 < number_2 and number_1 < number_3:          #checks if number_1 is the lowest number
    max_number = number_2
    middle_number = number_1
    if number_2 < number_3:                              #checks if number_3 > number_2 while number_1 is the lowest number
        max_number = number_3
        middle_number = number_2
    elif number_2 == number_3:                           #checks if number_2 == number_3 while number_1 is the lowest number
        max_number = number_2
        middle_number = "none"
        counter_same += 2
        alike_2 = "yes"
    elif number_2 > number_3:                            #checks if number_2 > number_3 while number_1 is the lowest number
        max_number = number_2
        middle_number = number_3


elif number_2 < number_1 and number_2 < number_3:        #checks if number_2 is the lowest number
    max_number = number_1
    middle_number = number_2
    if number_1 < number_3:                              #checks if number_3 > number_1 while number_2 is the lowest number
        max_number = number_3
        middle_number = number_1

    elif number_1 == number_3:                           #checks if number_1 == number_3 while number_2 is the lowest number
        max_number = number_1
        middle_number = "none"
        counter_same += 2
        alike_2 = "yes"

    elif number_1 > number_3:                            #checks if number_1 > number_3 while number_2 is the lowest number
        max_number = number_1
        middle_number = number_3


elif number_3 < number_1 and number_3 < number_2:        #checks if number_3 is the lowest number
    max_number = number_1
    middle_number = number_3
    if number_1 < number_2:                              #checks if number_2 > number_1 while number_3 is the lowest number
        max_number = number_2
        middle_number = number_1

    elif number_1 == number_2:                           #checks if number_1 == number_2 while number_3 is the lowest number
        max_number = number_1
        middle_number = "none"
        counter_same +=2
        alike_2 = "yes"

    elif number_1 > number_2:                            #checks if number_1 > number_2 while number_3 is the lowest number
        max_number = number_1
        middle_number = number_2

elif number_1 == number_2 and number_1 == number_3:        #checks if all the 3 numbers are equal
    max_number = number_1
    counter_same += 3
    alike_2 = "yes"
    alike_3 = "yes"
    middle_number = number_1

elif number_1 == number_2 and number_1 < number_3:         #checks for 2 numbers 1 & 2 are alike and determines whether the other number is the max number
    max_number = number_3
    counter_same += 2
    alike_2 = "yes"
    alike_3 = "no"
    middle_number = "none"

elif number_2 == number_3 and number_2 < number_1:         #checks for 2 numbers 2 & 3 are alike and determines whether the other number is the max number
    max_number = number_1
    counter_same += 2
    alike_2 = "yes"
    alike_3 = "no"
    middle_number = "none"

elif number_1 == number_3 and number_1 < number_2:         #checks for 2 numbers 1 & 3 are alike and determines whether the other number is the max number
    max_number = number_2
    counter_same += 2
    alike_2 = "yes"
    alike_3 = "no"
    middle_number = "none"

print("The maximum number is", max_number)


# 3 Give the counts of all of the numbers that are the same
print("\n============================= Numbers Alike =============================")
print("Count of numbers alike: ", counter_same)


# 4 Displays the middle number only if all three numbers are different or all are the same numbers in a table format
print("\n=================================== 5.4 Table ===================================")
print(" ________________________________________________________________________________")
print("| 1st No. | 2nd No. | 3rd No. |  Maximum  |  2 Alike?  |  3 Alike?  | Middle No. |")
row = "|" + "  " + str(number_1) + "      " + str(number_2) + "       " + str(number_3) + "        " + str(max_number) + "        " + alike_2 + "           " + alike_3 + "          " + str(middle_number)
row = row.ljust(81) + "|"                                                              #prints "|" on a fixed column position
print(row)
print("|________________________________________________________________________________|")
