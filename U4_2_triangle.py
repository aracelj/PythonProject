# Uppgift #4  by Araceli Jakobsson
#2 Outputs the hypotenuse of a triangle using pythagorean theorem c² = a² + b²

import math
base = float(input("\nEnter measurement of the base of a triangle: "))
altitude  = float(input("Enter measurement of the height of a triangle: "))
hypotenuse = math.sqrt(base**2 + altitude**2)  # computes the hypotenuse using the pythagorean theorem c² = a² + b²
print ("The hypotenuse of a triangle using the pythagorean theorem:", round(hypotenuse,2))