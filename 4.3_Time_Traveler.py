year = int(input("Enter a year: "))
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
century_year = year % 100 == 0
current_year = 2020

if century_year:
    print("It is a century year")

else:
    print("This is not a leap year")

else current_year == year:
    print("Equal")