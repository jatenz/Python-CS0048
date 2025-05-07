import os

def confirmation():
    input("\n[Press enter to go back...]")

def menu():
    os.system('cls' if os.name =='nt' else 'clear')
    print("Student Grade Calculator")
    print("[1] - Add Score")
    print("[2] - Calculate Average")
    print("[3] - Exit")

subjectNum = 0
totalAverage = 0
totalScore = 0
score = 0

while True:
    menu()
    choice = input("Select choice: ")

    if choice == "1":
        while True:
            print("\n--Add Score--")
            subject = input("Enter Subject: ")
            subjectNum += 1
            if subject == "N":
                subjectNum -= 1
                confirmation()
                break

            score = int(input("Enter Score: "))
            totalScore += score

    elif choice == "2":
        print("\n--Calculate Average--")
        totalAverage = float(totalScore/subjectNum)
        print(f"Average Grade: {totalAverage:.2f}")
        confirmation()

    elif choice == "3":
        print("\nThank you for using my Student Grade Calculator")
        break

    else:
        print("\nInvalid Input.")
        confirmation()
