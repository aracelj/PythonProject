"""
Uppgift #2 by Araceli Jakobsson
Räkna ut hur mycket som blir kvar, efter att man betalat en biljett
Pengarna som blir över ska dela med en vän
ursprung kod och ändrar till rätt koder
     x = 100  # biljettpris
     y = 200  # pengar på fickan
     print("Det blir " + (y - x) " kronor över.")
     z = y - x / 2
     print("Varje person får " + z)
"""

biljetpris = 100  # biljettpris
kontant = 200  # pengar på fickan
print ("\nBiljetpris:", biljetpris,"kronor \nKontant:", kontant,"kronor")
print ("Det blir" ,(kontant - biljetpris),  "kronor över.")
change = (kontant - biljetpris)/ 2
print("Varje person får", int(change),"kronor.")

