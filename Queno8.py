'''Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement'''
a=input("Enter a string: ")
b=input("Enter a string: ")
match a>b:
    case True:
        print(a," come afte ",b)
    case False:
        print(a," came befor ",b)
match a==b:
    case True:
        print("Enterd String is same")            