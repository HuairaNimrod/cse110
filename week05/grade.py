#grade calculator

print()
grade_percentage = int(input("enter the grade percentage: "))

if grade_percentage >= 90:
    grade = "A"
    msg = "congrats!!! you passed the class"
elif grade_percentage >= 80:
    grade = "B"
    msg = "congrats!!! you passed the class"
elif grade_percentage >= 70:
    grade = "C"
    msg = "congrats!!! you passed the class"
elif grade_percentage >= 60:
    grade = "D"
    msg = "Keep trying, good luck next time!!"
else:    
    grade = "F"
    msg = "Keep trying, good luck next time!!"

sign_value = grade_percentage%10

if sign_value>=7:
    sign = "+"
elif sign_value<3:
    sign = "-"
else:
    sign =""

print(f"Grade: {grade}{sign}\n{msg}" )
print()