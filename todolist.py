#Jay QH
#To Do List
#make a functional to-do list that you can edit


#init
undone = ["Lemon", "Chicken", "Broccoli", "Coffee", "Rice"]
done = []
#functions

def list():
    while True:
        option = (input("Would you like to: 1. Add an item to the to do list, 2. Mark an item as done, 3. Remove an item or clear the list, or 4. Exit the program?: "))
        if option == "1":
            new = input("What would you like to add to the list?: ")
            undone.append(new)
            print(undone)
            print(done)
        elif option == "2":
            finished = input("What item did you knock off the list?: ")
            undone.remove(finished)
            print(undone)
            done.append(finished)
            print(done)
        elif option == "3":
            remove = input("What item would you like to remove? If you want to clear the list please type all.: ")
            if remove == "all":
                undone.clear()
            else:
                undone.remove(remove)
        elif option == "4":
            break

#main
list()
