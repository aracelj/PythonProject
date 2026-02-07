# Exercise 5 Game Turtle Graphics by Araceli Jakobsson
# Version 3 Programs ask for the side length of the square and outputs a square as per input side length

"""
examplel code:
import turtle as t

# Upprepa 3 gånger
for x in range(3):
    t.forward(100)
    t.left(120)

# Lyft pennan för att flytta utan att rita
t.penup()
t.forward(200)
t.pendown()
t.dot(10, "red")
t.color("blue")
t.forward(50)

# Låt fönstret stanna kvar tills användaren stänger det
t.mainloop()
"""

import turtle as t
import my_string_module
side = int(input("Enter side length: "))
square_measurement = my_string_module.my_drawing(side)

