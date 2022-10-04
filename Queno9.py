'''Write a python script to check whether a given year is
a. Non century leap year not/400
b. Century leap year /400 /100 +1 
c. Non century non leap year 
d. Century non leap year'''
a=int(input('Enter a year: '))
b=(a/100)+1
match a%400==0:
    case True:
        print(b,"Century Leap year")
    case False:
        print("Non century leap year")
          
