# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades,
# return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	    A
# 80-89	    B
# 70-79	    C
# 60-69	    D
# 0-59	    F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

# debugged/altered by James Jack 2/6/21

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grade = [exam_one, exam_two, exam_three]

avg = sum(grade) / len(grade)
if avg >= 90:
    letter_grade = "A"
elif 80 <= avg < 90:
    letter_grade = "B"
elif 69 < avg < 80:
    letter_grade = "C"
elif 69 >= avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grade:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
