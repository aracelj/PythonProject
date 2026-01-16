# Uppgift #4_3a  by Araceli Jakobsson
# 3a Outputs the date of the day
# 3b Outputs the date of the next 7 days

#3a Outputs the date of the day
from datetime import date
print("\nToday's date: :", date.today())


#3b Outputs the date of the next 7 days
from datetime import date, timedelta
print("\nThe dates for the next 7 days:")
i = 1
for i in range (7):
  next_day = date.today() + timedelta(days=i+1)    # fetching the next 7 day dates
  print (next_day)
  i +=1