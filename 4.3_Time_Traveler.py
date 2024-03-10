year = int(input("Enter a year: "))
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
century_year = year % 100 == 0
current_year = 2020

if year == current_year:
    print("The provided year is the current year")

elif year > current_year:
    print("The provided year is in the future")

else:
    print("The provided year is the past")