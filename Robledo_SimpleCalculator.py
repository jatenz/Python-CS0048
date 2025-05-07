import os

def confirmation():
    input("\n[Press enter to go back...]")
    
def menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print("Python Simple Calculator")
    print("[1] - Add")
    print("[2] - Subtract")
    print("[3] - Multiply")
    print("[4] - Divide")
    print("[5] - Exit")

def addition():
    os.system('cls' if os.name =='nt' else 'clear')
    print("--Addition--")
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    result = num1 + num2
    print("Result:", result)
    confirmation()
def subtraction():
    os.system('cls' if os.name =='nt' else 'clear')
    print("--Subtraction--")
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    result = num1 - num2
    print("Result:", result)
    confirmation()
def multiplication():
    os.system('cls' if os.name =='nt' else 'clear')
    print("--Multiplication--")
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))
    result = num1 * num2
    print("Result:", result)
    confirmation()
def division():
    os.system('cls' if os.name =='nt' else 'clear')
    print("--Division--")
    num1 = int(input("Enter 1st Number: "))
    num2 = int(input("Enter 2nd Number: "))

    if num2 == 0:
        print("[Error: Division by zero is not allowed.]")
        confirmation()
        return
    
    result = num1 / num2
    print("Result:", result)
    confirmation()

while True:
    menu()
    choice = input("Select choice: ")

    if choice == "1":
        addition()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiplication()
    elif choice == "4":
        division()
    elif choice == "5":
        print("\n[Thank you for using my Simple Calculator App!]")
        break
    else:
        print("\n[Invalid Input.]")
        confirmation()