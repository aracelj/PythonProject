# Exercise 2_1c Sum from 1 to 100 using While Loop by Araceli Jakobsson
# Sum of all numbers from 1 to 100 using while loop

#1c Sum of numbers 1 to 100 using while loop
answer = 0
i = 1
while i != 101:                                                       # loop stops when i is 101
    answer += i                                                       # adding 1+2.....+100 = 5050
    i += 1
print("The Sum of all numbers from 1 to 100 is: " + str(answer))