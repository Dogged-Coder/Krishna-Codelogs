import colorama
from colorama import Fore
colorama.init()

items = int(input("How many items you want to list: "))
a = []
for i in range(items):
    a.append(input(f"Enter the task {i+1}: "))

print(f"\033[1m{Fore.GREEN}TO-DO LIST\033[0m")
for i, task in enumerate(a, 1):
    print(f"{Fore.BLUE}{i}- {Fore.YELLOW}{task}")

update = input("Do you want to update your TO-DO List? y/n: ")
if update.lower() == 'y':
    choice1 = input("Do you want to track completed tasks y/n: ")
    if choice1.lower() == 'y':
        n = int(input("How many tasks have you done? "))
        for _ in range(n):
            rem = int(input("Which task have you done? Give task number one at a time: "))
            if 1 <= rem <= len(a):
                print("Removed task number:", rem)
                a.pop(rem-1)
            else:
                print("Invalid task number.")
    else:
        print("Alright")
    choice2 = input("Do you want to add new tasks y/n: ")
    if choice2.lower() == 'y':
        nn = int(input("How many tasks do you want to add? "))
        for i in range(nn):
            a.append(input(f"Enter the task: {len(a)+1}: "))
    else:
        print("Alright")

print(f"\033[1m{Fore.GREEN}TO-DO LIST\033[0m")
for i, task in enumerate(a, 1):
    print(f"{Fore.BLUE}{i}- {Fore.YELLOW}{task}")