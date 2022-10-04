# Write a program which takes user’s age and display the category of person. Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -Experienced, Age above or equal 60 - Senior Citizen.
a=int(input("Enter Your Age Please: "))
match a<10:
    case True:
        print("Kid")
match 10<a<20:
    case True:
        print("Teen")
match 20<a<40:
    case True:
        print("young")
match 40<a<60:
    case True:
        print("Experienced")
match 60<a or a==60:
    case True:
        print("senior cityzen")

     