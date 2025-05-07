import os
import random

def confirmation():
    input("\n[Press enter to go back...]")

while True:
    os.system('cls' if os.name =='nt' else 'clear')
    print("Number Guessing Game")
    print("[1] - Play")
    print("[2] - Exit")
    choice = input("Select choice: ")

    if choice == "1":
        randomNum = random.randint(1, 100)
        guess = 0

        while True:
            os.system('cls' if os.name =='nt' else 'clear')
            print("\n--Guess the Number--")
            userNum = int(input("Enter Number (1-100): "))
            
            if userNum >= 1 and userNum <= 100:
                guess += 1
                if userNum < randomNum:
                    print("[Too Low!]")
                if userNum > randomNum:
                    print("[Too High!]")
                if userNum == randomNum:
                    print(f"Congratulations! You guessed the number in {guess} attempts.")
                    confirmation()
                    break
            else:
                print("[Invalid Input: Number must be between 1 and 100.]")
            confirmation()
    elif choice == "2":
        print("\n[Thank you for playing my Guessing Number Game.]")
        break
    else:
        print("\n[Invalid Input.]")
        confirmation()
        