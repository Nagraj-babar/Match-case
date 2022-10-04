'''Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.'''
a=int(input("Enter a number: "))
match a%2==0:
    case True:
        print("saurabh shukla")
match a<0:
    case True:
        print("prateek jain")
match a>0 and a%2!=0:
    case True:
        print("Aditya Choudhary")        


