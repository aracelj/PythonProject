# 5 Random Secret Number by Araceli Jakobsson
# Version 1 User enters a humber from 1 to 100 and show if its for low or high and counts how many times the user made guesses.


#Version 1 Guess the Random Secret Number
import random

print("Welcome to the random guessing number!Think of a number from 1 to 100. Can you guess the number?")
secret_number = random.randint(1,100)
attempts = 0
max_attempts= 6
print(secret_number)                                        # guide for the secret number
while attempts < max_attempts:
    input_number = input("Guess the number ( 1-100): ")
    attempts += 1
    try:
        guess_number = int(input_number)
        if (guess_number < secret_number) and (guess_number > 0):                   #checks if lower than secret no.
             print("No, that is too low!")
        elif (guess_number > secret_number) and (guess_number < 101):               #checks if higher than secret no.
             print("No, that is too high!")
        elif guess_number >= 101 or guess_number <=0:                               #checks if guess number is within 1 to 100
             print("Number must be from 1 to 100. Try again!")
        else:
             print(f"Correct!! You guessed it in {attempts} tries.")
             break

    except ValueError:                                                              #checks for error input
        print("Invalid number. Try again!")

else:
    print(f"Game over! You used all {max_attempts} attempts.")
    print(f"The correct number was {secret_number}.")
