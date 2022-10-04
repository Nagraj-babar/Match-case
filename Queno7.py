# Write a python program to check whether a given number is positive, negative or zero using match case statement
a=int(input("Enter a number: "))
match a>0:
    case True:
        print("Number is Positive")
match a<0:        
    case True:
        print("Number is Negative")
match a==0:
    case True:
        print("Number is zero")            