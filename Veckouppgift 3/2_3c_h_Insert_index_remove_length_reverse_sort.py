# Exercise 2_3c Insert another film by Araceli Jakobsson
# 2_3c Add "The two towers" at the beginning of the list(index 0)
# 2_3d Display the index number of "Fellowship of the ring" after adding the "the two towers"
# 2_3e Remove another film. Check if the Fellowship film index change
# 2_3f Take the length of the list
# 2_3g Reverse the list
# 2_3h Sor the list in an ascending alphabetical order

#2_3c Add "The two towers" at the beginning of the list
another_film = []
final_list = []
film = ['Avatar', 'Avengers:Endgame', 'Wonder Woman', 'Titanic', 'Fellowship of the ring']
print("Current Film List: ", film)
another_film = input("Enter another film: ")
film.insert(0,another_film)                         #inserting another film at index 0 of the list
print("Updated Film List: ", film)


#2_3d Display the index number of "Fellowship of the ring" now
print("===================================")
position = film.index("Fellowship of the ring")
print("Fellowship of the ring is on index no: ", position)

#2_3f Take the length of the list
print("===================================")
print("Film List length: ", len(film))

#2_3g Reverse the list
print("===================================")
film.reverse()                                                 #reverse the list
print("Reverse order of the list: ", film)

# 2_3h Sor the list in an ascending alphabetical order
print("===================================")
film.sort()                                                   #sort the list in alphabetical order
print("Sorted List: ", film)
