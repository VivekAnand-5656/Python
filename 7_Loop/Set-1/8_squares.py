# Create a list of squares for numbers 1 to 10.
num = int(input("Enter number:"))
data = []
for val in range(1,num+1):
    add = val*val
    data.append(add)

print(data)
 