
year = int(input("Enter a year: "))
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if leap_year:
    print("It is a leap year")

else:
    print("This is not a leap year")
