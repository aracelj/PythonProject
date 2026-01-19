# Uppgift2 Balder by Araceli Jakobsson
# User is ask to enter the height and program determines with the following conditions
#    If >= 130 cm, you may go
#    If < 130cm, you may not go

height = float(input("Enter users height in cm: "))
if height >= 130:                               #If user's height is >= 130 cm, prints "You may go."
    print("You may go.")
else:                                           #If user's height is <130 cm, prints "You may not go."
    print("You may not go.")
