# Uppgift 1. This simple python program prints a message to the screen
# Hello World
# This program was made by Araceli Jakobsson #

print ("Hello World \nThis program was made by Araceli Jakobsson")

#end Uppgift1

"""
Uppgift #2 
Räkna ut hur mycket som blir kvar, efter att man betalat en biljett
Pengarna som blir över ska dela med en vän
ursprung kod och ändrar till rätt koder
     x = 100  # biljettpris
     y = 200  # pengar på fickan
     print("Det blir " + (y - x) " kronor över.")
     z = y - x / 2
     print("Varje person får " + z)
"""

biljet = 100  # biljettpris
kontant = 200  # pengar på fickan
print ("\nBiljet: 100 \nKontant:200 kronor")
print ("Det blir" ,(kontant - biljet),  "kronor över.")
change = (kontant - biljet )/ 2
print("Varje person får", change,"kronor")

#end Uppgift2


#Uppgift #3
# The program will do the following calculations of time in hours, minutes
# Total cost of the jacket after the rebates

#1a ask for a whole number
tal1 = int(input("\nEnter a whole number: "))

#1b ask for another whole number and sum it up.
tal2 = int(input("Enter another whole number:"))
Total = tal1 + tal2
print ("Total for the two numbers: ",Total)

# 2a Calculates total cost to pay for the jacket which cost 2000 kronor with 75% rebates
jacket_cost = 2000
rebates = 75
final_cost = int(jacket_cost -(jacket_cost*(rebates)/100))  #calculates the final cost after the fixed rebates
print ("\nJacket original price: 2000 kronor \nRebates: 75%")
print ("Total jacket cost after the", rebates, "% rebates is:", final_cost, "kronor.")

#2b Enter the rebates percentage and give the total cost after the rebates
rebates_input = int(input("Enter the rebates percentage: "))
rebates_cost = int(jacket_cost*(rebates_input/100))            #calculates for the rebates cost
final_cost_percentage = int(jacket_cost - rebates_cost)        #calculates the final cost after the applied rebates
print (rebates_input, "% rebates: ", rebates_cost, "kronor")
print ("Total cost of the jacket after the rebates is: ", final_cost_percentage, "kronor.")

#end Uppgift3



#Uppgift #4
# Outputs the time travelled from Stockholm to Gothenburg in hours, minutes
# Outputs the hypotenuse of a triangle
# Outputs the date of the day and the next 7 days.

#1a outputs the time in hour
speed = int(input ("\nEnter driving speed(km/h): "))
distance = 470
time_hr = distance / speed
print ("Distance from Stockholm to Gothenburg (km/h): ", distance)
print ("Time to travel from Stockholm to Gothenburg (hours): ", round(time_hr,2)) #take only the whole number of the time

#1b outputs the time in minutes
time_min = time_hr * 60
print ("Time to travel from Stockholm to Gothenburg", round(time_hr,2), "hours converted in (minutes): ", int(time_min))

#1c output in hour and minutes
temp_hour = time_min // 60  #take the quotient as the no. of hours
temp_min = time_min % 60    #take the remainder as the no. of minutes
print ("Time to travel from Stockholm to Gothenburg:", int(temp_hour)," hour(s)", int(temp_min), " minute(s)")

#2 Outputs the hypotenuse of a triangle.
import math
base = int(input("\nEnter measurement of the base of a triangle: "))
altitude  = int(input("Enter measurement of altitude of a triangle: "))
hypotenuse = math.sqrt(base**2 + altitude**2)  # computing for the hypotenuse
print ("The hypotenuse of a triangle:", int(hypotenuse))

#3a Outputs the date of the day
from datetime import date
print("\nToday's date: :", date.today())


#3b Outputs the date of the next 7 days
from datetime import date, timedelta
print("\nThe dates for the next 7 days:")
i = 1
for i in range (7):
  next_day = date.today() + timedelta(days=i+1) # fetching the next day dates
  print (next_day)
  i +=1

#end Uppgift4