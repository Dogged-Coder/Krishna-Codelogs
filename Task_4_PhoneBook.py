import colorama
from colorama import Fore
colorama.init()
entries=int(input("How many number of entries?"))
name=[]
phone=[]
email=[]
add=[]
for i in range(entries):
   name.append(input(f"Enter the name {i+1}"))
   phone.append(int(input(f"Enter the phone number of {name[i]}")))
   email.append(input("Enter the email address of this person:"))
   add.append(input("Enter the address of this person:"))


def phonebook():
    print(f"\033[1m{Fore.BLUE}__________________PHONE___BOOK______________\033[0m")
    print(f"{Fore.RED}     NAME           ||PHONE NUMBER||            Email           ||   Address")
    print(f"{Fore.BLACK}___________________________________________________________")
    for i in range(len(name)):  # Use len(name) instead of entries
        print(f"{Fore.BLACK}{i+1}...", f"{Fore.GREEN}{name[i].ljust(20)}📞", f"{Fore.YELLOW}{phone[i]}📬{email[i].ljust(20)}🏡{add[i]}")
phonebook()

check = input("Do you want to check a particular contact? y/n: ")
if check.lower() == 'y':
    which = input("Which name do you want to check for? ")
    found = False
    for i, n in enumerate(name):
        if n.lower() == which.lower():
            print(f"{Fore.RED}     NAME           ||PHONE NUMBER||            Email           ||   Address")
            print(f"{Fore.BLACK}{i+1}...", f"{Fore.GREEN}{name[i].ljust(20)}📞", f"{Fore.YELLOW}{phone[i]}📬{email[i].ljust(20)}🏡{add[i]}")
            found = True
            break
    if not found:
        print("Wrong name entered")
else:
    print("Alright")



upd = input("Do you want to update any contact? y/n: ")
if upd.lower() == 'y':
    whic = input("Which person's contact do you want to update? (name): ")
    found = False
    for i, n in enumerate(name):
        if n.lower() == whic.lower():
            new = int(input("Tell the new number: "))
            phone[i] = new
            print(f"{Fore.RED}     NAME           ||PHONE NUMBER||            Email           ||   Address")
            print(f"{Fore.BLACK}{i+1}...", f"{Fore.GREEN}{name[i].ljust(20)}📞", f"{Fore.YELLOW}{phone[i]}📬{email[i].ljust(20)}🏡{add[i]}")
            found = True
            break
    if not found:
        print("Wrong name entered")
else:
    print("Alright")



delete = input("Do you want to delete any contact? y/n: ")
if delete.lower() == 'y':
    whom = input("Which person's contact do you want to delete? (name): ")
    found = False
    for i, n in enumerate(name):
        if n.lower() == whom.lower():
            name.pop(i)
            phone.pop(i)
            email.pop(i)
            add.pop(i)
            print("Contact deleted.")
            found = True
            break
    if not found:
        print("Wrong name entered")
else:
    print("Alright")

phonebook()
