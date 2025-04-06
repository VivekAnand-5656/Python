# Loop through a list and remove all even numbers.
num = int(input("Enter size of list:"))
data = []

for val in range(1,num+1,1):
    st = int(input(f"Enter{val}:"))
    data.append(st)
print(data)

for val in data[:]:
    if val%2==0:
        data.remove(val)
print("After remove:", data)