# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1(by default) and stops before a specified number.
# range(start?,stop,step?)
for i in range(5):          # range(stop)
    print(i)

print("------")

for i in range(5):          # range(start,stop)
    print(i)
print("------")


for i in range(2,10,2):     # range(start,stop,step)
    print(i)