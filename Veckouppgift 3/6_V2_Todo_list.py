# 6 Version 2 Todo List by Araceli Jakobsson
# Display a Todo List
# Option 1 See the content of the list
# Option 2 Add new item in the list



# Version2 Todo List

print(" ***** Todo List Extravaganza version 2*****")
print("Choose an option:")
print("1 - Display the Todo List ")
print("2 - Add a new item ")
print("3 - Marked as done ")
print("4 - Display archive ")
print("5 - Exit")

list = []
add_item = []
while True:
    try:
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice! Please enter 1, 2, 3, 4 or 5.")
            continue                                                       # ask again

        if choice == "1":
            list_counter = len(list)
            if list_counter == 0:
                print("This list is empty!)")
            else:
                print(" Todo List: \n", list)

        elif choice == "2":
            add_item = input("Enter an item to add: ")
            list.append(add_item)
            print(f"Ok, added {add_item} in the list.", )
        elif choice == "3"
            print()
            done_item = input("Ent")
            print("Marked as done:", done_item)
        elif choice == "5":
            print("Exit!")
            break

    except ValueError:
        print("Invalid input! Please enter 1, 2 or 3.")

