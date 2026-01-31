# 4 Figures with loop by Araceli Jakobsson
# User selects figures from a to j and print out the figure
"""
        for y in range(1, 7):
            s = ""
            for x in range(1, 9):
                if x == 1:
                    s += "#"
                else:
                    s += "."
            print(s)
"""

# 4 Figure with loop
print("========== Enter Figures a to j ==========")
figure = ''
figure_input = input("Select figure from a to j or 'q' to quit: ")
figure = figure_input.lower()
while  figure != 'q':
    if figure == 'a':
        for y in range(1, 7):                                  # making 7 lines
            s = ""
            for x in range(1, 9):
                if x == 1:                                     # prints "#" only in 1st column
                    s += "#"
                else:
                    s += "."                                   # prints "." for the rest of the lines
            print(s)
        break

    elif figure == 'b':
        for y in range(1, 7):                                  # makes 7 lines
            s = ""
            for x in range(1, 9):
                if x == y:
                    s += "#"                                   # moves "#" in a \ form
                else:
                    s += "."                                   # prints "." in all lines that is not filled with "#"
            print(s)
        break

    elif figure == 'c':
        for y in range(1, 7):                                  # makes 7 lines
            s = ""
            for x in range(1, 9):
                if x >= 3 and x <= 5:                          # prints "#" from 3-5th column on every row
                    s += "#"
                else:
                    s += "."                                   # prints "." in all lines that is not filled with "#"
            print(s)
        break
    elif figure == 'd':
        for y in range(1, 7):                                  # making 7 lines
            s = ""
            for x in range(1, 9):
                if x == 3 or y == 3:                           # prints "#" in + form
                    s += "#"
                else:
                    s += "."
            print(s)
        break

    elif figure == 'e':
        for y in range(1, 7):                                       # making 7 lines
            s = ""
            for x in range(1, 9):
                if (x == 5) or (x == 6 and y == 1) or (x + y == 7): # prints "#" inverted v form
                    s += "#"
                else:
                    s += "."
            print(s)
        break
    elif figure == 'f':
        for y in range(1, 7):                                       # making 7 lines
            s = ""
            for x in range(1, 9):
                if x == y or (x == 7 -y):                           # prints forming x form
                    s += "#"
                else:
                    s += "."
            print(s)
        break
    elif figure == 'g':
        for y in range(1, 7):                                       # making 7 lines
            s = ""
            for x in range(1, 9):
                if x == 1 or x == 3 or x == 5 or x == 7:            # prints "#" on 1st, 3rd, 5th, 7th column of every row
                    s += "#"
                else:
                    s += "."                                        # prints "." for the rest of the lines
            print(s)
        break
    elif figure == 'h':
        for y in range(1, 7):                                       # making 7 lines
            s = ""
            for x in range(1, 9):
                if x == 1:                                          # prints "." on 1st column
                    s += "."
                elif (x == 2 or x == 7) and (y == 3 or y == 4):     # prints "#" in an |  | form
                    s += "#"
                elif (x >= 2 and x <= 7) and (y == 2 or y == 5):    # prints "#" from 2nd to 6th column on 2nd & 5th row
                    s += "#"
                else:
                    s += "."                                        # prints "." for the rest of the lines
            print(s)
        break

    elif figure == 'i':                                             #printing i option figure
        for y in range(1,7):
            s = ""
            for x in range(1,9):

                if ((x == 2 or x == 5 or x == 8) and (y == 1 or y == 4)) or ((x == 3 or x == 6) and (y == 2 or y == 5)) or ((x == 1 or x == 4 or x == 7) and (y == 3 or y == 6)):
                    s += "#"
                if ((x == 3 or x == 6) and (y == 1 or y == 4)) or ((x == 1 or x == 4 or x == 7) and (y == 2 or y == 5)) or ((x == 2 or x == 4 or x == 8) and (y == 3 or y == 6)):
                    s += "O"
                if ((x == 1 or x == 4 or x == 7) and (y == 1 or y == 4)) or ((x == 2 or x == 5 or x == 8) and (y == 2 or y == 5)) or ((x == 3 or x == 6) and (y == 3 or y == 6)):
                    s += "."
            print(s)
        break

    elif figure == 'j':                                              #printing i option figure
        for y in range(1, 7):
            s = ""
            for x in range(1, 9):
                if (x == 3 or x == 6) and (y >=1 and y <= 3):
                    s += "#"
                elif (x >= 1 or x <= 8) and y == 4:
                    s += "."
                elif (x % 2 == 0) and (y == 5):
                    s += "#"
                elif (x % 2 != 0) and (y == 6):
                    s += "#"
                else:
                    s += "."
            print(s)
        break
    else:
        print("No figure selected!")
        break



