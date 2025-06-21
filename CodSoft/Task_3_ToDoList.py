import colorama
from colorama import Fore
colorama.init()

items=int(input("How many items you want to list:"))
a=[]
for i in range(0,items):
    a.append(input(f"Enter the task{i+1} "))

print(f"\033[1m{Fore.GREEN}TO-DO LIST\033[0m")
for i in range(0,items):
    print(f"{Fore.BLUE}{i+1}-",f" {Fore.YELLOW}{a[i]}")

update=input(print("Do you want to update your TO-DO List? y/n"))
if update.lower()=='y':
   choice1 =input("Do you want to track completed tasks y/n")
   if choice1.lower()=='y':
       n=int(input("How many task have you done?"))
       for i in range (n):
          rem=int(input("Which task you have done? Give task number one at a time"))
          a.pop(rem-1)
          print("Removed task number :",rem)
   else:
       print("Alright")
   choice2 =input("Do you want to add new task y/n")
   if choice2.lower()=='y':
        nn=int(input("How many task you want to add?"))
        for i in range(nn):
            a.append(input(f"Enter the task:{len(a)+1}"))
   else:
       print("Alright")

print(f"\033[1m{Fore.GREEN}TO-DO LIST\033[0m")
for i in range(items+nn):
    print(f"{Fore.BLUE}{i+1}-",f" {Fore.YELLOW}{a[i]}")
