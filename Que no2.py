# Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
a=eval(input("Enter a Number: "))
b=eval(input("Enter a Number "))
c=input("what do you want to do: ")
match c:
    case 'Addition':
        print(a+b)
    case 'Subtraction':
        print(a-b)
    case 'Multiplication':
        print(a*b)
    case "Division":
        print(a/b)
    case _:
        print("Something went wrong")



