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
            os.system('cls' if os.name =='nt' else 'clear')
            print("--Add Score--")
            print("[Press enter to stop adding subjects]")
            subject = input("\nEnter Subject: ")

            if subject == "":
                break

            subjectNum += 1
            score = int(input("Enter Score: "))
            print("[Score Successfully Added!]")
            confirmation()
            totalScore += score
    elif choice == "2":
        os.system('cls' if os.name =='nt' else 'clear')
        print("\n--Calculate Average--")

        if subjectNum == 0:
            print("[No Subject Found.]")
            confirmation()
            continue

        totalAverage = float(totalScore/subjectNum)
        print(f"Average Grade: {totalAverage:.2f}")
        confirmation()
    elif choice == "3":
        print("\n[Thank you for using my Student Grade Calculator.]")
        break
    else:
        print("\n[Invalid Input.]")
        confirmation()
