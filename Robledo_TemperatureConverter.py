import os

def confirmation():
    input("\n[Press enter to go back...]")

def menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print("Temperature Converter")
    print("[1] - Convert Celsius to Fahrenheit")
    print("[2] - Convert Fahrenheit to Celsius")
    print("[3] - Exit")

def CtoF():
    os.system('cls' if os.name =='nt' else 'clear')
    print("\n--Celsius to Fahrenheit--")
    value = float(input("Enter temperature in Celsius: "))
    result = (value * 9/5) + 32
    print(f"Celsius: {result:.2f}")
    confirmation()

def FtoC():
    os.system('cls' if os.name =='nt' else 'clear')
    print("\n--Convert Fahrenheit to Celsius--")
    value = float(input("Enter temperature in Fahrenheit: "))
    result = ((value - 32) * 5/9)
    print(f"Fahrenheit: {result:.2f}")
    confirmation()

while True:
    menu()
    choice = input("Select choice: ")
    if choice == "1":
        CtoF()
    elif choice == "2":
        FtoC()
    elif choice == "3":
        print("\n[Thank you for using my Temperature Converter App!]")
        break
    else:
        print("\n[Invalid Input.]")
        confirmation()
