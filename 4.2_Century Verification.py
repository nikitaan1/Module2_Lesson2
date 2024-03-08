
year = int(input("Enter a year: "))
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
century_year = year % 100 == 0

if leap_year:
    print("It is a leap year")

elif century_year:
    print("This is a century year")

else:
    print("This is not a leap or century year")