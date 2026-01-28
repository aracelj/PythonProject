# Exercise 2_2 Sum of all elements in the list by Araceli Jakobsson
# Sum of all elements in [1, -2, 3, -2, 4, -3]


# Sum of all elements in a given list
answer = 0
list1 = [1, -2, 3, -2, 4, -3]
counter = len(list1)
for i in range (counter):
    answer += list1[i]
print("The sum of all elements in the list ", list1, " is : ", answer)