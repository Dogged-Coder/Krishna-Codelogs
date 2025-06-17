print("Welcome to calculator, Please choose your operation")
choice = int(input("type 1 for addision\nType 2 for subtraction\nType 3 for division\nType 4 for multiplication\n\n"))
if choice>0 and choice <5:
    n1 = float(input("Enter the first no."))
    n2 = float(input("Enter the second no."))
else:
    print("Enter a correct choice nigga :)")
    
match choice :
    case 1:
        print("The sum is :", n1+n2)
    case 2:
        print("The difference is:", n1/n2)
    case 3:
        print("The division is:", n1/n2)
    case 4:
        print("The multiplication is:",n1*n2)
    
