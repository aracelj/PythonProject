# Exercise 2_3 List of 4 Films by Araceli Jakobsson
# Make a list of four films as a string. Output the whole list using print function.

# 2_3 Create a List of 4 Films
film = []
i = 1
for i in range(1,5):
     input_film = str(input("Film " + str(i) + ": "))
     film.append(input_film)
print("The Film List:")
print(film)



