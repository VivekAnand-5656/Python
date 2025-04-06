# Print a multiplication table for a number (e.g., 5):
num = int(input("Enter Table:"))
for val in range(1,11):
    print(f"{num}*{val}=",val*num)