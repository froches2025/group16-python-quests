user_grade = int(input("Enter the current score of the student out of 100: "))
if user_grade >= 90:
    print("Student grade is A")
elif user_grade >= 80 and user_grade <= 89:
    print("Student grade is B")
elif user_grade >= 70 and user_grade <= 79:
    print("Student grade is C")
else:
    print("Needs for improvement")
