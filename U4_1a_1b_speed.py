# Uppgift #4  by Araceli Jakobsson
# 1a Outputs the time in hours
# 1b Outputs the time in minutes
# 1c Outputs the time in hour and minutes

#1a outputs the time in hours
speed = int(input ("\nEnter driving speed(km/h): "))
distance = 470
time_hr = distance / speed       #calculates the time in hour
print ("Distance from Stockholm to Gothenburg (km/h): ", distance)
print ("Time to travel from Stockholm to Gothenburg (hours): ", round(time_hr,2))

#1b outputs the time in minutes
time_min = time_hr * 60
print ("Time to travel from Stockholm to Gothenburg is", round(time_hr,2), "hours converted in (minutes): ", int(time_min))

#1c output in hour and minutes
temp_hour = time_min // 60  #take the quotient as the no. of hours
temp_min = time_min % 60    #take the remainder as the no. of minutes
print ("Time to travel from Stockholm to Gothenburg:", int(temp_hour)," hour(s)", int(temp_min), " minute(s)")





