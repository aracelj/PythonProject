# Uppgift #4  b_basey Araceli Jakob_basesson
#2 Outputs the hypotenuse of a triangle using pythagorean theorem c² = a² + b_base²

import math
b_base = float(input("\nEnter measurement of the base of a triangle: "))
a_height  = float(input("Enter measurement of the height of a triangle: "))
hypotenuse = math.sqrt(b_base**2 + a_height**2)  # computes the hypotenuse using the pythagorean theorem c² = a² + b_base²
print ("The hypotenuse of a triangle using the pythagorean theorem:", round(hypotenuse,2))