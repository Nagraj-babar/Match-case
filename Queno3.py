'''Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.'''
a=int(input("Enter a First Digit Number: "))
b=int(input("Enter a secound number: "))
c=int(input("Enter a third number: "))
d=int(input("Enter a first angles: "))
e=int(input("Enter a secound angle: "))
f=int(input("Enter a Third angle: "))
match a==b==c:
    case True:
            print("Lengths of isosceles triangle")
    case False:
            print("Not isosceles triangle") 

'''Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not'''            
match (a**2)+(b**2)==c**2:
    case True:
        print("Right angle Triange")
    case False:
        print("Not Right angle Triangle")

'''Check whether a given set of three numbers are equilateral triangle or not'''
match a==b==c or d==e==f:
    case True:
        print("Three Number is equilateral triangle")
    case False:
        print("Three numbers is not equilateral triangle")
    case _:
        print("Exit")        



