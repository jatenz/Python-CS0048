import os

firstNum = 0
secondNum = 0
result = 0 

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

def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2

while True:
    menu()
    choice = input("Select choice: ")

    if choice == "1":
        print("\n--Addition--")
        firstNum = int(input("Enter 1st Number: "))
        secondNum = int(input("Enter 2nd Number: "))
        result = int(addition(firstNum, secondNum))
        print("Result:", result)
        confirmation()
    elif choice == "2":
        print("\n--Subtraction--")
        firstNum = int(input("Enter 1st Number: "))
        secondNum = int(input("Enter 2nd Number: "))
        result = int(subtraction(firstNum, secondNum))
        print("Result:", result)
        confirmation()
    elif choice == "3":
        print("\n--Multiplication--")
        firstNum = int(input("Enter 1st Number: "))
        secondNum = int(input("Enter 2nd Number: "))
        result = int(multiplication(firstNum, secondNum))
        print("Result:", result)
        confirmation()
    elif choice == "4":
        print("\n--Division--")
        firstNum = int(input("Enter 1st Number: "))
        secondNum = int(input("Enter 2nd Number: "))
        if secondNum != "0":
            result = int(division(firstNum, secondNum))
            print("Result:", result)
            confirmation()
        else:
            print("Cannot Divide by Zero")
            confirmation()

    elif choice == "5":
        print("Thank you for using my Simple Calculator App")
        break
    else:
        print("\nInvalid Input.")
        confirmation()