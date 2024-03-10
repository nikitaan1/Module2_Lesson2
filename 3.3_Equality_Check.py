student_grade = input("What is the grade of the student? ")
extracurricular_activities = input("Is the student part of an extracurricular activity? ")

if student_grade == "A":
    if extracurricular_activities == "Sport":
        print("The Student Will Get 20% Discount")
    else:
        print("The Student Will Get 10% Discount")

elif student_grade == "B":
    if extracurricular_activities == "Drama":
        print("The Student Will Get 15%")
    else:
        print("The Students Will Not Recieve A Discount")
        
        


