# My String module to take a string as a parameter

import random
import time
import turtle as t
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

def cut_edges(my_list):                                              #2_5 cut_edges function
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

def my_game(random_number):                                          #3_v1 Game 21 version 1
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
    print(f"Final total: {total}")                                   # Stop if number is over 21

def my_game2(card):                                                  #Game21 Version 2

    total = 0
    while True:
        number2 = random.randint(1,13)                               #Generating 2nd random number
        print(f"Generated random number: {number2}")
        if number2 > card:                                           #Stops generating the 2nd if its greater than card number
            print(f"Number {number2} is greater than the card number {card}. Stopping the game.")
            break
        else:
            total += number2
            print(f"Current sum: {total}")                           #Display running sum
        time.sleep(5)
    print(f"Final total: {total}")                                   #Stops the game and display final sum

def my_game3(card):                                                  #3_v1 Game 21 version 3
    total = 0
    while True:
        number2 = random.randint(1,13)                               #Generating 2nd random number
        print(f"Player's card: {number2}")
        change_card = input("Change card? y (yes) or n (no): ")
        if change_card.lower() == "y":
            number2 = random.randint(1, 13)
        else:
            if number2 > card:                                       #Stops generating the 2nd if its greater than card number
                print(f"Player's card is {number2} greater than the computer's card {card}. Player wins!")
                break
            else:
                print(f"Player lost a game!")
        time.sleep(3)

def my_poker(card_counter):                                                      #4 Pokerhand suits
    suits = ["Hearts","Clubs","Spades","Diamonds"]
    cards = []
    for suit in suits:
        for value in range(2,15):
            cards.append((value, suit))                              # stored as tuple as [value: 'suit' ..] creating 52 combinations
    return random.sample(cards,card_counter)

def my_poker_evaluation(cards,version):  # 4 Pokerhand evaluation
    values = []
    suits = []
    for value, suit in cards:
        values.append(value)
        suits.append(suit)

    i = 0

    poker_version = 3
    if values[i] == values[i + 1]:
        value = values[i]
        message = "You have 2 cards of same value."
        if poker_version == version:
           return (message, value, suits)
        else:
           return message
    else:
        return "No pair found."



def card_name(value):
    names = {11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}
    return names.get(value, str(value))                              # returns the string value if value does not exist in names




def evaluate_hand_simple(cards):
    values = []
    suits = []
    for value, suit in cards:
        values.append(value)
        suits.append(suit)

    values.sort()

    # Count card values
    counts = {}
    for value, suit in cards:
        counts[value] = counts.get(value, 0) + 1

    # Detect pairs, three, four
    pairs = []
    three = None
    four = None
    for value, count in counts.items():
        if count == 4:
            four = value
        elif count == 3:
            three = value
        elif count == 2:
            pairs.append(value)

# Detect flush
    is_flush = len(set(suits)) == 1

    # Detect straight
    is_straight = all(values[i] - values[i-1] == 1 for i in range(1, len(values)))

    # Ace-low straight (A-2-3-4-5)
    if set(values) == {14, 2, 3, 4, 5}:
        is_straight = True
        values = [1, 2, 3, 4, 5]

    # Check hands in order of strength
    if is_straight and is_flush:
        return f"Straight Flush: {card_name(values[-1])}"
    if four:
        return f"Four of a Kind with value: {card_name(four)}s"
    if three and pairs:
        return f"Full House: {card_name(three)}s over {card_name(pairs[0])}s"
    if is_flush:
        return "Flush"
    if is_straight:
        return f"Straight: {card_name(values[-1])}"
    if three:
        return f"Three of a Kind with value: {card_name(three)}s"
    if len(pairs) == 2:
        return f"Two Pairs with value: {card_name(max(pairs))}s and {card_name(min(pairs))}s"
    if len(pairs) == 1:
        return f"One Pair with value: {card_name(pairs[0])}s"

    # Fives if no other hand
    return f"Fives"



def my_drawing(sides):                                     # Turtle Graphics ver1
    import turtle as t

    for x in range(4):
        t.forward(sides)                                   #move the turtle forward by side value
        t.right(90)                                        #turn the turtle 90 degrees

    t.mainloop()                                           # keeping the draw board open until exited

def my_drawing2(length,counter):                           # Turtle Graphics ver1
    import turtle as t
    t.speed(2)
    distance = 20
    width = t.window_width()//2
    height = t.window_height()//2
    t.penup()
    t.goto(-width + 10, height - 10)                      #set the pen at the upper left corner
    t.pendown()

    for i in range(counter):
            for x in range(4):                            #draw the 4 sides of the square
                t.forward(length)                         #length of the square
                t.right(90)                               #turn the turtle 90 degrees
            t.penup()
            t.forward(length + distance)
            if t.xcor() + length > width:                 #check if it exceeds the turtle window screen
                t.setx(-width + 10)
                t.sety(t.ycor() - length - 20)
            t.pendown()
    t.mainloop()                                          #keeping the draw board open until exited

# Move to starting point
def position_P():
    t.penup()                                         # moving the cursor without drawing
    t.goto(-260, -40)                                 # start left below center line
    t.pendown()                                       # start drawing
# ---------- Draw P ----------
def draw_P():
    t.left(90)
    t.forward(85)                                     # vertical line
    t.right(90)
    t.circle(-25, 180)                                # top curve of P

# ---------- Move to Y position ----------
def position_Y(distance):
    t.penup()
    t.goto(t.xcor() + 50 + distance, t.ycor() - 5)   # alignment of arm
    t.setheading(90)                                 # face right
    t.pendown()

# ---------- Draw Y ----------
def draw_Y():
    t.right(20)
    t.forward(57)                               # left arm

    t.backward(57)
    t.left(40)
    t.forward(57)                               # right arm

    t.backward(57)
    t.right(20)
    t.forward(-32)                              # stem

# ---------- Move to T position ----------
def position_T(distance):
    t.penup()
    t.goto(t.xcor() + 30 + distance, t.ycor() + 85)          # alignment of horizontal
    t.setheading(0)                                          # face right
    t.pendown()

# ---------- Draw T ----------
def draw_T():
    t.forward(50)                                            # horizontal line
    t.penup()
    t.goto(t.xcor() - 25, t.ycor())                          # alignment in the middle of the horizontal line
    t.setheading(270)
    t.pendown()

    t.forward(85)                                            # vertical line

# ---------- Move to H position ----------
def position_H(distance):
    t.penup()
    t.goto(t.xcor() + 30 + distance, t.ycor())               # alignment of vertical line
    t.setheading(0)                                          # face right
    t.pendown()

# ---------- Draw H ----------
def draw_H():
    t.left(90)
    t.forward(85)                                            # vertical line

    t.penup()
    t.goto(t.xcor() + 40, t.ycor() - 85)                     # alignment other vertical line
    t.setheading(0)
    t.pendown()
    t.left(90)
    t.forward(85)                                            # vertical line

    t.penup()
    t.goto(t.xcor(), t.ycor() - 40)                          # middle of vertical line
    t.pendown()
    t.setheading(180)
    t. forward(40)                                           # horizontal line
# ---------- Move to O position ----------
def position_O(distance):
    t.penup()
    t.goto(t.xcor() + 45 + distance, t.ycor())               # alignment
    t.setheading(270)                                        # face right
    t.pendown()
# ---------- Draw to O
def draw_O():
    radius = 45
    t.circle(radius)                                         # circle

# ---------- Move to N position ----------
def position_N(distance):
    t.penup()
    t.goto(t.xcor() + 95 + distance, t.ycor() + 42)          # alignment
    t.setheading(270)                                        # face down
    t.pendown()
# ---------- Draw to N
def draw_N():
    t. forward(90)                                           # vertical line

    t.penup()
    t.goto(t.xcor() + 40, t.ycor() + 90)                     # alignment
    t.setheading(270)                                        # face down
    t.pendown()
    t.forward(90)                                            # vertical line

    t.penup()
    t.goto(t.xcor(), t.ycor())                               # alignment
    t.setheading(0)                                          # face right
    t.pendown()
    t.left(113)
    t.forward(98)                                            # diagonal line










