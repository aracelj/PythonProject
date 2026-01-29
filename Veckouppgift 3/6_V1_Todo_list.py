# 6 Version 1 Todo List by Araceli Jakobsson
# Display a Todo List
# Option 1 See the content of the list
# Option 2 Add new item in the list


# Version 1 Todo List

print(" ***** Todo List Extravaganza version 1 *****")
print("Choose an option:")
print("1 - Todo List Content ")
print("2 - Add a new item ")
print("3 - Exit ")

list = []
add_item = []
while True:
    try:
        choice = input("Enter your choice (1/2/3): ")

        if choice not in ("1","2","3"):
            print("Invalid choice! Please enter 1, 2 or 3.")
            continue                                                    #ask again

        if choice == "1":                                               #todo list content
            list_counter = len(list)
            if list_counter == 0:                                       #checks if list is empty
                print("This list is empty!")
            else:
                print(" Todo List: \n", list)

        elif choice == "2":                                             #add an item
            add_item = input("Enter an item to add: ")
            list.append(add_item)
            print(f"Ok, added {add_item} in the list.", )

        elif choice == "3":                                             #exit the program
            print("Exit!")
            break

    except ValueError:                                                  #handles the invalid input
        print("Invalid input! Please enter 1, 2 or 3.")

