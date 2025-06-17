import colorama
from colorama import Fore
colorama.init()

items=int(input("How many items you want to list:"))
a=[]
for i in range(0,items):
    a.append(input(f"Enter the task{i+1} "))

print(f"\033[1m\033[1m\033[1m{Fore.GREEN}TO-DO LIST\033[0m\033[0m\033[0m")
for i in range(0,items):
    print(f"{Fore.BLUE}{i+1}-",f" {Fore.YELLOW}{a[i]}")