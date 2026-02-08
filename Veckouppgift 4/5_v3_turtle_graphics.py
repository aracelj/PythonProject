# Exercise 5 Game Turtle Graphics by Araceli Jakobsson
# Version 3 Programs draw a complete circle by editing given code
"""
Original code:
for x in range(7):
    t.forward(40)
    t.right(30)
"""

#Editing the original code to form a complete circle
import turtle as t
i = 12
length = 40
angle = 30

for x in range(i):                    #changing the counter to 12 to complete a full circle
    t.forward(length)
    t.right(angle)
t.mainloop()