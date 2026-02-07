# My String module to take a string as a parameter


def string_parameter(name):                                            #2_1 String function
    print(f" {name} is a whiz at programming")                         #printing the string together with the phrase
    return 0

def string_echo(name):                                                 #2_2a Echo function
    print(f"{name}{name}")                                             #echoing the string twice
    return 1

def checker_counter(counter):
    counter_final = 0
    while True:
            counter = input("Enter counter: ")
            if counter.isdigit() == True:                              #accepts only numbers
                counter_final = int(counter)
                break
            else:
                print("Invalid input! Enter a counter number. ")
    return counter_final

def echo_counter(name,counter):                                        #2_2b Echo function with a counter
    echo = ""
    if counter == 0:                                                   #checks if its zero counter
        print("Nothing to echo!")
    else:
        for i in range(counter):
            echo += name
    print(f"{echo}")
    return counter


def my_loop():                                                        #2_3 Loop function
    end = 5
    y = 1
    for x in range(1, 100):
        y *= 2
        if x == end:                                                  #ends at the 5th loop
            break
    print(y)


def last(my_list):                                                    #2_4 last function
    item = my_list[-1]                                                #printing the last element of the list
    return item

def cut_edges(my_list):                                               #2_5 cut_edges function
    item = my_list[1:-1]
    return item

def number_input(ask_user):
  while True:
        try:
            value = float(input (ask_user))                           #validating the input if its a number
            if value == 0:
                print("Value cannot be zero. Try again.")
                continue
            return value
        except ValueError:
            print("Invalid input.Try again.")


def average(x,y):                                                    #2_7 average function
    return (x+y)/2                                                   #returning the average of two numbers

def my_list(pretty_list):                                            #2_8 pretty_list function
    counter = len(pretty_list)
    if counter == 0:                                                 #if list is empty
        print("List is empty")

    else:                                                            #otherwise it will print in enumerated form
        print(f"List entered: {pretty_list}")
        print(f"List has {counter} element:")
        for i in range(counter):
            pretty_print = pretty_list[i]
            print(f"{i+1}. {pretty_print}")
        return

def my_game(random_number):                                          #3_v1 Game 21 version 1 & 2
    total = 0
    #random_number = random_input
    while True:
        user_input = input("Enter a number (or type 'q' to quit): ")

        if user_input.lower() == "q":                                #Stop if user wants to quit early
            break

        try:
            number = float(user_input)                               #Convert it to a number
        except ValueError:
            print("Invalid input, not a number. Try again.")
            continue                                                 #Ignore non-numeric

        if number > random_number:
            print(f"Number {number} is greater than {random_number}. Stopping the game.")
            break

        total += number                                              #Add valid number to total
        print(f"Current sum: {total}")                               #Display running sum
    print(f"Final total: {total}")                                   # Stop if number is equal to number_random


def my_game2(card):                                          #3_v1 Game 21 version 1 & 2
    total = 0
    #random_number = random_input
    while True:
        user_input = input("Enter a number 1-13 (or type 'q' to quit): ")

        if user_input.lower() == "q":  # Stop if user wants to quit early
            break
        try:
            number = float(user_input)                                 #Convert it to a number
            if number > 0 and number < 14:
                number1 = number
        except ValueError:
            print("Invalid input, enter between 1 - 13. Try again.")
            continue                                                 #Ignore non-numeric

        if number > card:
            print(f"Number {number} is greater than {card}. Stopping the game.")
            break

        total += number                                              #Add valid number to total
        print(f"Current sum: {total}")                               #Display running sum
    print(f"Final total: {total}")                                   # Stop if number is equal to number_random


def my_game3(card):                                          #3_v1 Game 21 version 1 & 2
    total = 0
    #random_number = random_input
    while True:
        user_input = input("Enter a number 1-13 (or type 'q' to quit): ")

        if user_input.lower() == "q":  # Stop if user wants to quit early
            break
        try:
            number = float(user_input)                                 #Convert it to a number
            if number > 0 and number < 14:
                number1 = number
        except ValueError:
            print("Invalid input, enter between 1 - 13. Try again.")
            continue                                                 #Ignore non-numeric

        if number > card:
            print(f"Number {number} is greater than {card}. Stopping the game.")
            break

        total += number                                              #Add valid number to total
        print(f"Current sum: {total}")                               #Display running sum
    print(f"Final total: {total}")                                   # Stop if number is equal to number_random




