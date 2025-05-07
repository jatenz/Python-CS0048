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
        while True:
            os.system('cls' if os.name =='nt' else 'clear')
            print("--Add Task--")
            print("[Press enter to stop adding tasks]")
            task = input("\nEnter Task to Add: ")

            if task == "":
                break

            taskList.append(task)
            print("[Task Successfully Added!]")
            confirmation()
    elif choice == "2":
        os.system('cls' if os.name =='nt' else 'clear')
        print("--Remove Task--")
        selectTask = input("Enter Task to Remove: ")
        taskList.remove(selectTask)
        confirmation()
    elif choice == "3":
        os.system('cls' if os.name =='nt' else 'clear')
        print("--View Task--")
        
        if len(taskList) == 0:
            print("[No Task Found.]")
        else:
            print("Task List:")
            for i in taskList:
                print(i)
        confirmation()
    elif choice == "4":
        print("\n[Thank You for using my To-Do List App.]")
        break
    else:
        print("\n[Invalid Input.]")
        confirmation()
