# Develop a program to categorize a person's Body Mass Index  (BMI) using else-if:
#  ● BMI < 18.5: Underweight
#  ● BMI 18.5- 24.9: Normal
#  ● BMI 25- 29.9: Overweight
#  ● BMI >= 30: Obese

BMI = float(input("Enter BMI: "))
if(BMI < 18.5):
    print("Underweight")
elif(BMI > 18.5 or BMI < 24.9):
    print("Normal")
elif(BMI > 25 or BMI < 29.9):
    print("Overweight")
elif(BMI >= 30):
    print("Obese")