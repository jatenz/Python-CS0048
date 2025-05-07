import os

def confirmation():
    input("\n[Press enter to go back...]")

def menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print("To-Do List")
    print("[1] - Add Task")
    print("[2] - Remove Task")
    print("[3] - View Task")
    print("[4] - Exit")

taskList = []

while True:
    menu()
    choice = input("Select choice: ")
    if choice == "1":
        print("\n--Add Task--")
        while True:
            task = input("Enter Task to Add: ")
            taskList.append(task)

            if task == "N":
                break
        confirmation()
    elif choice == "2":
        print("\n--Remove Task--")
        selectTask = input("Enter Task to Remove: ")
        taskList.remove(selectTask)
        confirmation()

    elif choice == "3":
        print("\n--View Task--")
        for i in taskList:
            print(i)
        confirmation()

    elif choice == "4":
        print("\nThank You for using my To-Do List App")
        break
    else:
        print("\nInvalid Input.")
        confirmation()
