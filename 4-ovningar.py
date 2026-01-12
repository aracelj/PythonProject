#1a Output the time travelled from Stockholm to Gothenburg
#   User enters the speed in km/h

speed = int(input ("Enter driving speed(km/h): "))
distance = 470
time_hr = distance / speed
print ("Distance from Stockholm to Gothenburg(km/h): ", distance)
print ("Time to travel from Stockholm to Gothenburg(hour): ", int(time_hr))

#1b outputs the time in minutes
time_min = time_hr * 60
print ("Time to travel from Stockholm to Gothenburg(minutes): ", int(time_min))

#1c output in hour and minutes
temp_hour = time_min // 60
temp_min = time_min % 60
print ("Time to travel from Stockholm to Gothenburg:", int(temp_hour)," hour", int(temp_min), " minutes")

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

