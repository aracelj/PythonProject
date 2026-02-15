# 1b equivalence class: (9/5) C + 32

#1c Test file
def celsius_fahrenheit(degree):
    if degree < -273.15:                 #for value less than -273.15 and returns None
        return None
    return degree * 9 /5 + 32            #converting celsius to fahrenheit