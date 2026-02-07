# Exercise 5 Game Turtle Graphics by Araceli Jakobsson
# Version 4 Programs draw the word "PYTHON" using turtle module

import my_string_module
import turtle as t

screen = t.Screen()
screen.setup(width=600, height=600)
t.speed(3)
t.width(5)
distance = 10

my_string_module.position_P()
my_string_module.draw_P()
my_string_module.position_Y(distance)
my_string_module.draw_Y()
my_string_module.position_T(distance)
my_string_module.draw_T()
my_string_module.position_H(distance)
my_string_module.draw_H()
my_string_module.position_O(distance)
my_string_module.draw_O()
my_string_module.position_N(distance)
my_string_module.draw_N()


t.mainloop()