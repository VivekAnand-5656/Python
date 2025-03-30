# Develop a program to categorize a person's Body Mass Index  (BMI) using else-if:
#  ● Units <= 100: ₹5 per unit
#  ● Units <= 300: ₹7 per unit
#  ● Units > 300: ₹10 per unit

units = int(input("Enter Unit:"))
if(units <= 100):
    print("Total : ₹",units*5)
elif(units <= 300):
    print("Total : ₹",units*7)
elif(units > 300):
    print("Total : ₹",units*10)