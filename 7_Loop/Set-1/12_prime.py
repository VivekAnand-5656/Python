# Write a program to find all prime numbers between 1 and 50
num1 = int(input("Enter Num1:"))
num2 = int(input("Enter Num2:"))
count=0
j=2
for val in range(num1,num2+1):
    count=0
    for i in range(j,val):
        if(val%j==0):
            break
    else:
        print(val)