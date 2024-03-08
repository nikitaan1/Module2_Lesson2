num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))
num3 = int(input("Enter num3 "))

if num1 == num2 and num1 == num3:
    print("All numbers are equal")

elif num1 == num2: 
    print("Two numbers are equal and the largest is", num3)
elif num1 == num3:
        print("Two numbers are equal and the largest is", num2)
elif num2 == num3:
     print("Two numbers are equal and the largest is", num2)