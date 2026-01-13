# Uppgift #4  by Araceli Jakobsson
# Outputs the time travelled from Stockholm to Gothenburg in hours, minutes
# Outputs the hypotenuse of a triangle
# Outputs the date of the day and the next 7 days.

#1a outputs the time in hours
speed = int(input ("\nEnter driving speed(km/h): "))
distance = 470
time_hr = distance / speed       #calculates the time in hour
print ("Distance from Stockholm to Gothenburg (km/h): ", distance)
print ("Time to travel from Stockholm to Gothenburg (hours): ", round(time_hr,2))

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
  next_day = date.today() + timedelta(days=i+1)    # fetching the next day dates
  print (next_day)
  i +=1

