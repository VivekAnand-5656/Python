# .Write a program to calculate the grade of a student based on their marks using an else-if:
#  ● Marks ≥ 90: Grade A
#  ● Marks ≥ 75: Grade B
#  ● Marks ≥ 50: Grade C
#  ● Marks < 50: Grade F
marks = float(input("Enter Marks: "))
if(marks >= 90):
    print("Grade A!")
elif(marks >= 75):
    print("Grade B!")
elif(marks >= 50):
    print("Grade C!")
elif(marks < 50):
    print("Grade F!")