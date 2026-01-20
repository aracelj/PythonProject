# Uppgift4 Temperature converter by Araceli Jakobsson
# Version 1 Converts the temperature in celsius to fahrenheit
# Version 2 Ask user whether to use celsius or fahrenheit and converts respectively
# Version 3 If the converted temperature is:
#               below 10°C, display a message "Wear winter jacket."
#                below 20°C, display a message "Pack a bathing clothes."
# Formulas to use: C = (F - 32) / 1.8
#                  F = 1.8 * C + 32


# Version 1 Converts the temperature in celsius to fahrenheit
input_celsius1 = 0
conversion_to_fahrenheit = 0
print("======= Version 1 Converts temperature from celsius to fahrenheit =======")
input_celsius1 = float(input("Enter temperature in degrees celsius: "))
conversion_to_fahrenheit = 1.8 * input_celsius1 + 32
print("It will be", round(conversion_to_fahrenheit,1),"degrees Fahrenheit.")                      # converts from celsius to fahrenheit


# Version 2 Ask user whether to use celsius or fahrenheit and converts respectively
input_selection_temperature = 0
input_celsius2= 0
print("\n======= Version 2 Converts temperature from celsius to fahrenheit or vice versa =======")
input_selection_temperature = int(input("Celsius to Fahnrenheit (1) or Fahrenheit to Celsius (2): (Enter 1 or 2) "))
if input_selection_temperature == 1:                                                              # converts from celsius to fahrenheit if selection 1(celsius to fahrenheit)
      input_celsius2 = float(input("Enter temperature in degrees celsius: "))
      conversion_to_fahrenheit = 1.8 * input_celsius2 + 32
      final_conversion = conversion_to_fahrenheit
      input_temperature = "Fahrenheit"
      print("It will be", round(final_conversion,1), "degrees", input_temperature, ".")

elif input_selection_temperature == 2:                                                           # converts from fahrenheit to celsius if selection 2(fahrenheit to celsius)
      input_fahrenheit = float(input("Enter temperature in degrees fahrenheit: "))
      conversion_to_celsius = (input_fahrenheit - 32) / 1.8
      final_conversion = conversion_to_celsius
      input_temperature = "Celsius"
      print("It will be", round(final_conversion, 2), "degrees", input_temperature, ".")

else:                                                                                            # wrong selection between celsius (1) & fahrenheit (2)
      print("Wrong selection, it should be 1 or 2.")






