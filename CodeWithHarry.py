#Name Good afternoon
'''name= str(input("What is your name:"))
print( " Yourn name is:",name )
print("Good afternoon")'''


#Letter template
'''print("Fill info for letter:")
print("Dear <|NAME|> \n You are selected! \n <|DATE|>")
name = str(input("Ur name:"))
date = str(input("Date dd/mm/yy"))
print("Dear\n",name +"  You are selected! \n",date)'''


#to detect double space
'''string = str(input("Enter the string:"))
for i in range(len(string)-1) :
  if string[i]==" " and string[i+1]==' ' :
     print(i , "\n")   
'''

#to print 7 fruits in a list
'''list=input("Enter any 7 fruits:").split()
print(list)'''


#by append
'''list=[]
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    list.append(fruit)
print(list)'''
    

#accept and sort students marks
'''list=[]
for i in range(5):
    marks = int(input("Enter marks :"))
    list.append(marks)
    list.sort()
print(list)'''


#Acctept values and print only the unique one
'''n=int(input("enter the number of values:"))
set=set()
for i in range(n):
 s = int(input(f"Enter the value: {i}  ",))
 set.add(s)
print(set)'''


#To enter favourite languages by 4 friends
'''fav={}
for i in range(4):
    name = input("Enter your name:")
    lang= input("Enter your favourite language:")
    fav[name]=lang
print(fav)'''

#Greatest of 4 number by user
'''a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
d = int(input("Enter the fourth number"))
if a>b and a>c and a>d:
    print("The greatest number is:", a)
elif b>a and b>c and b>d:
    print("The greatest number is:", b)
elif c>a and c>b and c>d:
    print("The greatest number is:", c)
else:
    print("The greatest number is:", d)
'''

#to detect spam messages
'''msg=input ("Enter the message:")
if "make a lot of money" in msg or "buy now" in msg or "click this" in msg:
    print("This is a spam message")
else:
    print("This is not a spam message")
    '''

#To find the meaning of words in Hindi
'''dict={"pani":"water", "chawal":"rice", "roti":"bread", "sabji":"vegetable"}
choice=input(f"Enter the word in Hindi: {dict.keys()}")
print("The meaning of", choice, "is", dict.get(choice,"not found"))'''


#to find if a given name is present in a list
'''n=int(input("Enter the number of list:"))
name=[]
for i in range(n):
  a=input("enter the names:")
  name.append(a)
print(name)
check=input("ENter name to check")
if check in name:
 print("Name found at index",name.index(check))
else:
  print("Name not found :)")'''

#to generate table of 7
'''
i=1
while i<11:
    print(f"7 X {i} = {7*i}")
    i = i+1

for i in range(1,11):
    print(f"7 X {i} = {7*i}") '''

#   to check if a number is prime
'''a=0
no=int(input("Enter the number"))
for i in range(2,no):
    if no%i==0:
        a=a+1
if a>0:
 print("Number is not a prime number.")
elif a==0:
   print("number is a prime number")'''

#pattern : *         for n =3
#         ***
#        *****
'''n=int(input("Enter the value of n:"))
for i in range(n+1):
  print(" "*(n-i),"*"*((2*i)-1)," "*(n-i))
  '''

#pattern  ***   for n =3
#         * *
#         ***
'''n = int(input("Enter the value of n:"))
for i in range (1,n+1):
    if i==1 or i==n :
        print ("*"*n)
    else :
        print("*"+" "*(n-2)+"*")'''

#to print factorial by def function
'''def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the number:"))
print(f"The factorial of number is:{factorial(n)}")'''

#to print greatest of 3 number using def
'''def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
a,b,c=int(input("Enter the 1st numbers:")),int(input("Enter the 2nd numbers:")),int(input("Enter the 3rd numbers:"))
print(f"the greastest number is : {greatest(a,b,c)}")
'''

#to print sum of n natral no. with recrussion
'''
add=0
def sum(n):
    if n==1:
     return 1
    else:
       add=n+sum(n-1)
       return add
n=int(input("Enter the value of n:"))
print(f"The sum of n natural numbers is: {sum(n)}")
'''

#pattern by recrussion- ***
#                       **
#                       *     for n=3
'''def pat(n):
    for i in range(n,0,-1):
        print("*"*i)
    return " Done  :D"
n=int(input("Entervvalue of n:"))
pat(n)'''

import mediapipe as mp
print("🎉 MediaPipe is working, lets bend some air!")