import os

def confirmation():
    input("\n[Press enter to go back...]")

def menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print("Temperature Converter")
    print("[1] - Convert Celsius to Fahrenheit")
    print("[2] - Convert Fahrenheit to Celsius")
    print("[3] - Exit")

def CtoF(value):
    return (value * 9/5) + 32

def FtoC(value):
    return ((value - 32) * 5/9)

userNum = 0

while True:
    menu()
    choice = input("Select choice: ")
    if choice == "1":
        print("\n--Celsius to Fahrenheit--")
        userNum = float(input("Enter temperature in Celsius: "))
        result = float(CtoF(userNum))
        print(f"Celsius: {result:.2f}")
        confirmation()
    elif choice == "2":
        print("\n--Convert Fahrenheit to Celsius--")
        userNum = float(input("Enter temperature in Fahrenheit: "))
        result = float(FtoC(userNum))
        print(f"Fahrenheit: {result:.2f}")
        confirmation()
    elif choice == "3":
        print("\nThank you for using my Temperature Converter App")
        break
    else:
        print("\nInvalid Input.")
        confirmation()
