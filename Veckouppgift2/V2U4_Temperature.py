# Uppgift3 Balder by Araceli Jakobsson
# Version 1 Converts the temperature in celsius to fahrenheit
# Version 2 Ask user whether to use celsius or fahrenheit and converts respectively
# Version 3 If the converted temperature is:
#               below 10°C, display a message "Wear winter jacket."
#                below 20°C, display a message "Pack a bathing clothes."
# Formulas to use: C = (F - 32) / 1.8
#                  F = 1.8 * C + 32


# Version 1 Converts the temperature in celsius to fahrenheit
print("======= Version 1 Converts temperature from celsius to fahrenheit =======")
input_celsius = float(input("Enter temperature in degrees celsius: "))
conversion_celsius_to_fahrenheit = input_celsius * 1.8 + 32
print("It will be", round(conversion_celsius_to_fahrenheit,3),"degrees Fahrenheit.")


# Version 2 Ask user whether to use celsius or fahrenheit and converts respectively
input_temperature = 0
input_celsius = 0
print("======= Version 2 Converts temperature from celsius to fahrenheit or vice versa =======")
input_temperature = int(input("Select conversion from Celsius to Fahnrenheit (1) or Fahrenheit to Celsius (2): "))
if input_temperature == 1:
      input_celsius = float(input("Enter temperature in degrees celsius: "))
      conversion_to_fahrenheit = (input_celsius * 1.8) + 32
      final_conversion = conversion_to_fahrenheit
      input_temperature = "Fahrenheit"

elif input_temperature == 2:
      input_fahrenheit = float(input("Enter temperature in degrees fahrenheit: "))
      conversion_to_celsius = (input_fahrenheit - 32) / 1.8
      final_conversion = conversion_to_celsius
      input_temperature = "Celsius"
      ".")
elif input_temperature != 1 or input_fahrenheit != 2:
    print("Wrong selection, it should be 1 or 2.")

print("It will be", round(final_conversion, 3), "degrees", input_temperature)

