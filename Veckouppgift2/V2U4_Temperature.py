# Uppgift4 Temperature converter by Araceli Jakobsson
# Version 1 Converts the temperature in celsius to fahrenheit
# Version 2 Ask user whether to use celsius or fahrenheit and converts respectively
# Version 3 If the converted temperature is:
#               below 10°C, display a message "Wear winter jacket."
#               at least 20°C, display a message "Pack a bathing clothes."
# Formulas to use: C = (F - 32) / 1.8
#                  F = 1.8 * C + 32


# Version 1 Converts the temperature in celsius to fahrenheit
input_celsius1 = 0
conversion_to_fahrenheit = 0
print("======= Version 1 Converts temperature from celsius to fahrenheit =======")
input_celsius1 = float(input("Enter temperature in degrees celsius: "))
conversion_to_fahrenheit = (1.8 * input_celsius1) + 32
print("It will be", round(conversion_to_fahrenheit,1),"degrees Fahrenheit.")                      # converts from celsius to fahrenheit


# Version 2 Ask user whether to use celsius or fahrenheit and converts respectively
input_selection_temperature = 0
input_celsius2= 0
input_fahrenheit = 0
bring_clothes = 0
print("\n======= Version 2 Converts temperature from celsius to fahrenheit or vice versa =======")
input_selection_temperature = int(input("Celsius to Fahrenheit (1) or Fahrenheit to Celsius (2): (Enter 1 or 2) "))
if input_selection_temperature == 1:                                                              # converts from celsius to fahrenheit if selection 1(celsius to fahrenheit)
      input_celsius2 = float(input("Enter temperature in degrees celsius: "))
      conversion_to_fahrenheit = 1.8 * input_celsius2 + 32
      final_conversion = conversion_to_fahrenheit
      input_temperature = "Fahrenheit"
      print("It will be", round(final_conversion,1), "degrees", input_temperature, ".")
      if conversion_to_fahrenheit < 50:                                                           # checks its below 50°F
           bring_clothes += 1
      elif conversion_to_fahrenheit >= 68:                                                        # checks if at least 68°F
           bring_clothes += 2
      else:
           bring_clothes += 3
elif input_selection_temperature == 2:                                                            # converts from fahrenheit to celsius if selection 2(fahrenheit to celsius)
      input_fahrenheit = float(input("Enter temperature in degrees fahrenheit: "))
      conversion_to_celsius = (input_fahrenheit - 32) / 1.8
      final_conversion = conversion_to_celsius
      input_temperature = "Celsius"
      print("It will be", round(final_conversion, 2), "degrees", input_temperature, ".")
      if conversion_to_celsius < 10:                                                              # checks its below 10°C
          bring_clothes += 1                                                                      # counter to bring winter jacket
      elif conversion_to_celsius >= 20:                                                           # checks if at least below 20°C
          bring_clothes += 2  # checks its below 68 degrees fahrenheit                            # counter to bring swim wear
      else:
          bring_clothes += 3                                                                      # counter for no recommendations
else:                                                                                             # wrong selection between celsius (1) & fahrenheit (2)
      bring_clothes += 0
      print("Wrong selection, it should be 1 or 2.")


# Version 3 To recommend whether to bring winter jacket / swim wear
print ("\n======== Version 3 To recommend whether to bring winter jacket / swim wear ========" )
if bring_clothes == 1:                                                                            # Checks if counter 1 to bring winter jacket
      print("Temperature is under 10°C or under 50°F. Bring winter jacket!")
elif bring_clothes == 2:
      print("Temperature is at least 20°C or 68°F. Bring swim wear!")                             # Checks if counter 2 to bring swim wear
elif bring_clothes == 3:                                                                          # Checks if counter 3 on no recommendations
      print("No suggestions on what clothes to bring!")
else:                                                                                             # Checks if counter 0 for wrong selection on temperature selection
      print("Wrong selection on the temperature conversion.")






