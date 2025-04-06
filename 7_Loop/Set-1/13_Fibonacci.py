# Print Fibonacci series up to n terms.
num = int(input("Enter Number:"))

store=0
a=0
b=1
print(a)
print(b)
for val in range(1,num+1):
    store=a+b
    print(store)
    a=b
    b=store