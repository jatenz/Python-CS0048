import os
import random

def confirmation():
    input("\n[Press enter to go back...]")

randomNum = random.randint(1, 100)
userNum = 0
guess = 0

while True:
    os.system('cls' if os.name =='nt' else 'clear')
    print("Number Guessing Game")
    print("[1] - Play")
    print("[2] - Exit")
    choice = input("Select choice: ")

    if choice == "1":
        print("\n--Guess the Number--")
        while True:
            userNum = int(input("Enter Number: "))
            if userNum < randomNum:
                print("Too Low!")
            if userNum > randomNum:
                print("Too High!")
            if userNum == randomNum:
                print(f"\nCongratulations! You guessed the number in {guess} attempts.")
                confirmation()
                break
    elif choice == "2":
        print("\nThank you for playing my Guessing Number Game.")
        break
    else:
        print("\nInvalid Input")
        confirmation()
        