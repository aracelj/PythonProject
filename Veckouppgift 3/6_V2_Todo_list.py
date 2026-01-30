# 6 Version 2 Todo List by Araceli Jakobsson
# Display a Todo List
# Option 1 Display the content of the list
# Option 2 Add new item in the list
# Option 3 Marked as done and remove the item from Todo list and save it to the Archive list
# Option 4 Archive list and ask user whether to move the item back to the Todo List or not
# Option 5 Exit the program



# Version2 Todo List

print(" ***** Todo List Extravaganza version 2*****")

counter = 0
archive_counter = 0
list = []
add_item = []
archive_item = []
archive_index = []
archive_list = []
archive_choice = []
while True:
    try:
        choice = input(" ============ Choose an option: ============ "
                       "\n(1) To-do list Content       (4) Archive "
                       "\n(2) Add a new To-do list     (5) Exit "
                       "\n(3) Mark as done "
                       "\nEnter your choice number: ")

        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice! Please enter 1, 2, 3, 4 or 5.")
            continue                                                       # ask again

        if choice == "1":                                                  #content of the list menu
            counter = len(list)
            if counter == 0:
                print("This list is empty!)")
            else:
                print(" To-do List: ")
                for i in range(counter):
                         archive_index = list[i]
                         print(f"{i+1} - {archive_index} ")

        elif choice == "2":                                                #add an item menu
            add_item = input("Enter a new To-do list: ")
            add_item = add_item.capitalize()
            list.append(add_item)                                          #add an item to the Todo list
            print(f"Ok, added {add_item} in the list.", )

        elif choice == "3":                                                #marked as done menu
            counter = len(list)
            if counter != 0:
                print("Choose the To-do task to mark as done: ")
                for i in range(counter):
                         archive_index = list[i]
                         print(f"{i+1} - {archive_index} ")
                archive_choice = input("Enter the list no. to mark as done: ")
                archive_counter = int(archive_choice)
                if (archive_counter > 0) and (archive_counter <= counter): #accepts only within the menu item no.
                    archive_item = list[archive_counter-1]
                    if archive_item in list:
                             archive_list.append(archive_item)             #added to the archive list
                             list.remove(archive_item)                     #removes the item from Todo list
                             print(f"Ok, task \"{archive_item}\" is marked as done.")
                    else:
                             print("Not Found!")
                else:
                    print("Invalid choice! Please enter correct task number.")
            else:
                print("To-do List is empty! Nothing to mark as done.")

        elif choice == "4":                                                #archive menu
            print("Archive List: ")
            counter = len(archive_list)
            if counter !=0:
                    for i in range(counter):
                        archive_index = archive_list[i]
                        print(f"{i + 1} - {archive_index} ")
                    archive_choice = input("Move back the Archived task to Todo List? Yes(y) or No(n): ")
                    if archive_choice == "Y" or archive_choice == "y":      #accepts only Y or y
                        move_choice =input("Which archived number to move to To-do List?: ")
                        archive_counter = int(move_choice)
                        if (archive_counter > 0) and (archive_counter <= counter):    #accepts only within the menu item no.
                            archive_item = archive_list[archive_counter - 1]
                            if archive_item in archive_list:
                                list.append(archive_item)                             #added to the Todo list
                                archive_list.remove(archive_item)                     #removes the item from archive list
                                print(f"Ok, archived \"{archive_item}\" is back in To-do list.")
                            else:
                                print("Not Found!")
                        else:
                            print("Invalid choice! Please enter correct task number.")
                    elif archive_choice == "N" or archive_choice == "n":
                        print("Back to main menu!")

                    else:
                        print("Invalid choice! Please enter y or n .")
                        continue
            else:
                print("Archive list is empty! Nothing to move.")

        elif choice == "5":
            print("Exit!")
            break

    except ValueError:
        print("Invalid input! Please enter 1, 2,3,4 or 5.")

