
"""
Uppgift1 Price by Araceli Jakobsson
Correct the code
Original code:
        is_member = False
        level1 = 100
        level2 = 300
        discount = 0

        price = input("Välkommen, köp något dyrt? ")
        price = float(price)
        if price > level1:
             print("Gratis! Du har avancerat till nivå 1 och får 10% rabatt.")
             discount = discount + 10
        if price >= level2:
             print("Gratis! Du har avancerat till nivå 2 och får 25% rabatt.")
             discount = discount + 25

        final_price = price (100 - discount) / 100
        print("Efter rabatter blir priset.... " + final_price)
"""

#is_member = True
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: Ange ett pris: ")
price = float(price)
if price > level1 and price <300:                                      #calculates for 10% discount if over 100 but below 300
     print("Gratis! Du har avancerat till nivå 1 och får 10% rabatt.")
     discount = discount + 10
if price >= level2:                                                    #calculates for 25% discount if over or equal to 300
     print("Gratis! Du har avancerat till nivå 2 och får 25% rabatt.")
     discount = discount + 25
#else:
#     print("Ingen rabatt.")
final_price = price * (100 - discount) / 100                           #computing the final price after the discount
print("Efter rabatter blir priset.... " + str(final_price),"Kr")            #setting the final_price variable to string to correct the error
