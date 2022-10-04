# Write a python program to check whether a given string is a multiword string or single word string using match case statement
a=len(input("Enter a String: "))
match a>1:
    case True:
        print("String is a multiword")
    case False:
        print("String is a single word")    