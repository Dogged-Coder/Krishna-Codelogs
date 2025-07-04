print("Welcome to calculator, Please choose your operation")

while True:
    try:
        choice = int(input("\nType 1 for addition\nType 2 for subtraction\nType 3 for division\nType 4 for multiplication\nType 5 to exit\n\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number for operation choice!")
        continue

    if choice in [1, 2, 3, 4]:
        try:
            n1 = float(input("Enter the first number: "))
            n2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers!")
            continue

        match choice:
            case 1:
                print(f"The sum is: {n1} + {n2} = {n1 + n2}")
            case 2:
                print(f"The difference is: {n1} - {n2} = {n1 - n2}")
            case 3:
                if n2 == 0:
                    print("Can't divide by zero!")
                else:
                    print(f"The division is: {n1} / {n2} = {n1 / n2}")
            case 4:
                print(f"The multiplication is: {n1} * {n2} = {n1 * n2}")
    elif choice == 5:
        print("Exiting calculator.")
        break
    else:
        print("Invalid choice! Please select a number between 1 to 5.")
