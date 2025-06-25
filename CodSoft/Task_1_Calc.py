
print("Welcome to calculator, Please choose your operation")
while True:
       choice = int(input("type 1 for addition\nType 2 for subtraction\nType 3 for division\nType 4 for multiplication\n\nType 5 for exit"))
       if not 5 :
          try:
            n1 = float(input("Enter the first no."))
            n2 = float(input("Enter the second no."))
          except ValueError:
            print("Enter a number")
        
       match choice :
         case 1:
            print("The sum is :" ,n1,"+",n2,"=",n1+n2)
         case 2:
            print("The difference is:",n1,"-",n2,"=", n1-n2)
         case 3:
            if n1==0:
               print("Can't devide by zero")
            else:
               print("The division is:",n1,"/",n2,"=", n1/n2)
         case 4:
            print("The multiplication is:",n1,"*",n2,"=",n1*n2)
         case 5:
             print("Exiting")
             break
         case _:
            print("Enter a correct operation number")
