# Exercise 2_3c Insert another film_list by Araceli Jakobsson
# 2_3c Add "The two towers" at the beginning of the list(index 0)
# 2_3d Display the index number of "Fellowship of the ring" after adding the "the two towers"
# 2_3e Remove another film_list. Check if the Fellowship film_list index change
# 2_3f Take the length of the list
# 2_3g Reverse the list
# 2_3h Sort the list in an ascending alphabetical order

#2_3c Add "The two towers" at the beginning of the list
another_film_list = []
remove_film_list = []
film_list = ['Avatar', 'Avengers:Endgame', 'Wonder Woman', 'Titanic', 'Fellowship Of The Ring']
print("Current film List: ", film_list)
another_film_list = input("Enter another film: ")
another_film_list = another_film_list.title()                              #converting the film_list string into a title format
film_list.insert(0,another_film_list)                                      #inserting another film_list at index 0 of the list
print("Updated film List: ", film_list)


#2_3d Display the index number of "Fellowship of the ring" now
print("===================================")
position = film_list.index("Fellowship Of The Ring")                  #fetching the position of the film_list using index function
print("Fellowship Of The Ring is on index no: ", position)


#2_3e Remove another film_list in the list
print("===================================")
remove_film_list = input("Enter the film you wish to remove: ")
remove_film_list = remove_film_list.title()                                #converting the film_list into a title format
film_list.remove(remove_film_list)                                         #removing the film_list from the list
print("Updated film List: ", film_list)


#2_3f Take the length of the list
print("===================================")
print("film List length: ", len(film_list))                           #fetching the length of the list

#2_3g Reverse the list
print("===================================")
film_list.reverse()                                                   #reverse the list
print("Reverse order of the list: ", film_list)

# 2_3h Sort the list in an ascending alphabetical order
print("===================================")
film_list.sort()                                                      #sort the list in alphabetical order
print("Sorted List: ", film_list)
