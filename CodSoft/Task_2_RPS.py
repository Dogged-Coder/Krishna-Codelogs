
import random

def Game(choice, userP, compP):
    comp = random.choice(["rock", "paper", "scissors"])
    if choice == comp:
        print(f"you: {choice} and computer: {comp}")
        print("Draw")
    elif choice == "rock" and comp == "paper":
        print(f"you: {choice} and computer: {comp}")
        print("Computer won")
        compP += 1
    elif choice == "paper" and comp == "rock":
        print(f"you: {choice} and computer: {comp}")
        print("You won")
        userP += 1
    elif choice == "scissors" and comp == "rock":
        print(f"you: {choice} and computer: {comp}")
        print("Computer won")
        compP += 1
    elif choice == "rock" and comp == "scissors":
        print(f"you: {choice} and computer: {comp}")
        print("You won")
        userP += 1
    elif choice == "paper" and comp == "scissors":
        print(f"you: {choice} and computer: {comp}")
        print("Computer won")
        compP += 1
    elif choice == "scissors" and comp == "paper":
        print(f"you: {choice} and computer: {comp}")
        print("You won")
        userP += 1
    else:
        print("Wrong choice entered")
        print("Exiting program")
    print(f"Your point: {userP} Computer points: {compP}")
    return userP, compP

while True:
    print("Are you ready for the GAME ?\nChoose among rock, paper or scissors")
    n = int(input("For how many points you want to play? "))
    userP = 0
    compP = 0
    for i in range(n):
        print("3....2....1....")
        choice = input("Now choose: ").lower()
        userP, compP = Game(choice, userP, compP)
    print(f"Final Score - You: {userP} Computer: {compP}")
    again = input("Do you want to play again? y/n: ")
    if again.lower() == 'y':
        continue
    else:
        print("Have a good day")
        break