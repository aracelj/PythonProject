# 4 Figures with loop by Araceli Jakobsson
# User selects figures from a to j and print out the figure


# 4 Figure with loop
print("===== Enter Figures a to j =====")
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
                    s += "#"                                   # moves "#" one position to the right on each new line
                else:
                    s += "."                                   # prints "." in all lines that is not filled with "#"
            print(s)
        break

    elif figure == 'c':
        for y in range(1, 7):                                  # makes 7 lines
            s = ""
            for x in range(1, 9):
                if x >= 3 and x <= 5:                          # prints "#" starting on  3rd-5th column of every line
                    s += "#"
                else:
                    s += "."                                   # prints "." in all lines that is not filled with "#"
            print(s)
        break
    elif figure == 'd':
        for y in range(1, 7):                                  # 7 lines
            s = ""
            if y == 3:                                         # prints "#" all in 3rd row
               for x in range(1, 9):
                   s += "#"
               print(s)
            else:
                for x in range(1, 9):                          # prints "#" every 3rd column
                    if x == 3:
                        s += "#"
                    else:
                        s += "."                               # prints "." in all lines that is not filled with "#"
                print(s)
        break
    elif figure == 'e':
        for y in range(1, 7):                                  # 7 lines
            s = ""
            if y == 3:                                         # prints "#" all in 3rd row
               for x in range(1, 9):
                   s += "#"
               print(s)
            else:
                for x in range(1, 9):                          # prints "#" every 3rd column
                    if x == 5:
                        s += "#"
                    else:
                        s += "."                               # prints "." in all lines that is not filled with "#"
                print(s)
        break


print("End of story!")
    #if figure == 'b':
    #if figure == 'c':
    #if figure == 'd':
    #if figure == 'e':
    #if figure == 'f':
    #if figure == 'g':
    #if figure == 'h':
    #if figure == 'i':
    #if figure == 'j':
#lse:#
      #  print("Wrong selection!")


#amount_input = input("Enter an amount or 'q' to quit:: ")