# 5 Random Secret Number by Araceli Jakobsson
# User enters a humber from 1 to 100 and determines if its correct, low, high or just 5 steps away from the correct number


#Version 2 Guess the Random Secret Number

import random

print("Welcome to the random guessing number!Think of a number from 1 to 100. Can you guess the number?")
secret_number = random.randint(1,100)
attempts = 0
guess_number = 0
max_attempts= 10
print(secret_number)                                        # guide for the secret number
while attempts < max_attempts:
        input_number = input("Guess the number ( 1-100): ")
        attempts += 1
        try:
                guess_number = int(input_number)
                if (guess_number < secret_number) and (guess_number > 0):
                         if abs(secret_number - guess_number) <= 5:                         #checks if guess number is 5 steps closer to the correct no.
                             print("No, that number is too close to the correct number.")
                         else:                                                              #checks if lower than secret no.
                             print("No, that is too low!")
                elif (guess_number > secret_number) and (guess_number < 101):               #checks if guess number is 5 steps closer to the correct no.
                         if abs(secret_number - guess_number) <= 5:
                             print("No, that number is too close to the correct number.")
                         else:                                                              #checks if higher than secret no.
                             print("No, that is too high!")
                elif guess_number >= 101 or guess_number <= 0:                              #checks if guess number is within 1 to 100
                         print("Number must be from 1 to 100. Try again!")
                else: #guess_number == secret_number:
                         print(f"Correct!! You guessed it in {attempts} tries.")
                         break

        except ValueError:                                                                  #checks for error input
            print("Invalid number. Try again!")

else:
    print(f"Game over! You used all {max_attempts} attempts.")
    print(f"The correct number was {secret_number}.")



