# ----------- for loop --------
# Loops are used for sequential traversal. For traversing list,string,tuples etc.
data = [10,50,24,60,80,55,65,95,105]

for val in data:
    print(val)

# Seatch Element
srch = int(input("Enter Element:"))
found=0
for val in data:
    if(val==srch):
        found=1
        print(val," Found")

if(found==0):
    print(srch," Not Found")