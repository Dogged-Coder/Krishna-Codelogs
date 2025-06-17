#My first Project to make a rock paper scissors game with computer.

def Game(choice):
    import random
    comp=random.choice(["rock","paper","scissors"])
    userP=0
    compP=0
    if choice==comp:
        print(f"you: {choice} and computer: {comp}")
        print("Draw")
        compP=0
        userP=0
        print(f"Your point: {userP} Computer points: {compP}")
    elif choice=="rock" and comp=="paper":
        print(f"you: {choice} and computer: {comp}")
        print("Computer won")
        compP=compP+1
        print(f"Your point: {userP} Computer points: {compP}")
    elif choice=="paper" and comp=="rock" :
        print(f"you: {choice} and computer: {comp}")
        print("You won")
        userP=userP+1
        print(f"Your point: {userP} Computer points: {compP}")
    elif choice=="scissors" and comp=="rock" :
        print(f"you: {choice} and computer: {comp}")
        print("Computer won")
        compP=compP+1
        print(f"Your point: {userP} Computer points: {compP}")
    elif choice=="rock" and comp=="scissors" :
        print(f"you: {choice} and computer: {comp}")
        print("You won")
        userP=userP+1
        print(f"Your point: {userP} Computer points: {compP}")
    elif choice=="paper" and comp=="scissors" :
        print(f"you: {choice} and computer: {comp}")
        print("Computer won")
        compP=compP+1
        print(f"Your point: {userP} Computer points: {compP}")
    elif choice=="scissors" and comp=="paper" :
        print(f"you: {choice} and computer: {comp}")
        print("You won")
        userP=userP+1
        print(f"Your point: {userP} Computer points: {compP}")
    else:
        print("Wrong choice entered")
        print("Exiting program")
print("Are you ready for the GAME ?\nChoose amongs rock, paper or scissors")
n=int(input("For how many points you want to play?"))
for i in range(0,n):
    print("3....2....1....")
    choice=input("Now choose")
    Game(choice)
