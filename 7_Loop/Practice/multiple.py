# Print the multiplication table of a number n.
num = int(input("Enter Number :"))
 
multi = 1
i = 1
while i<=10:
    multi=num*i
    print(f"{num} * {i} = ",multi)
    i+=1
