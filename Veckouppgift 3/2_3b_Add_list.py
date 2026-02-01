# Exercise 2_3b Add another film Araceli Jakobsson
# Add "Fellowship of the ring" at the end of the list

#2_3b Add another film "Fellowship of the ring" at the end of the list
film = ['Avatar', 'Avengers:Endgame', 'Wonder Woman', 'Titanic']
print("Current Film List: ", film)
another_film = str(input("Enter another film: "))
film.append(another_film)                                #adding another film at the last of the list
print("Updated Film List: ", film)
