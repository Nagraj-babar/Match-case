# Write a python script to display the number of days in a given month number.
a=input("Enter a Month: ")
match a:
    case 'jan':
        print("No of days is 31")
    case 'feb':
        print("No of days is 28")
    case 'mar':
        print("No of days is 31")
    case 'apr':
        print("No of days is 30")
    case "may":
        print("No of days is 31")
    case "jun":
        print("No of days is 30")
    case "july":
        print("No of days is 31")
    case "aug":
        print("No of days is 31")
    case "sep":
        print("No of days is 30")
    case "oct":
        print("No of days is 31")
    case "nov":
        print("No of days is 30")
    case "dec":
        print("No of days is 31")
    case _:
        print("You Enter wrong month name")                    


