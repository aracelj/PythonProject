# Exercise 1_5 Move the line by Araceli Jakobsson
# Change the code to move a step to the right
"""
What is the output of the code:
for y in range(1, 7):
    s = ""
    for x in range(1, 9):

        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

 Original Output:
#.......
 .#......
 ..#.....
 ...#....
 ....#...
 .....#..

"""

#5 Change the code to move a step to the right
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y + 1:
            s += "#"
        else:
            s += "."
    print(s)