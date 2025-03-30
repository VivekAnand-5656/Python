# -------- Conditional Statements
# Single line if / Ternary Operator

# ------- Type-1 to write Ternary Operator ------
food = input("Enter Food : ")
eat = "Yes" if food == "Peda" else "No"
print(eat)

# ------- Type-2 to write Ternary Operator ------
food2 = input("Enter Food : ")
print("Sweet") if food2 == "cake" or food2 == "jalebi" else print("Not Sweet")

# ----------Type 2 Ternary Operator ---- its not more usable...
# Clever if / Ternary Operator 
age = int(input("Enter age:- "))
vote = ("yes","no") [age <= 18]
print(vote)

sal = float(input("Enter salary:- "))
tax = sal*(0.1,0.2) [sal<=50000]
print(tax)