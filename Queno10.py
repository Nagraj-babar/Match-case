'''Write a program to display day name on the basis of users liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday'''
a=input("What is your favorite colour: ")
match 'yellow'in a:
    case True:
        print("Monday")   
match "blue" in a:
    case True:
        print("Tuesday")
match 'orange'in a:
    case True:
        print("Wednesday")
match 'white' in a:
    case True:
        print("Thursday")
match 'black'in a:
    case True:
        print("Friday")
match 'red' in a:
    case True:
        print("Saturday")
    case _:
        print("sunday")           
           

