# Search for a number x in this tuple using loop
data = (10,54,65,85,94,65,86,80)
srch = int(input("Enter Search:"))
found = 0
for val in data:
    if(val==srch):
        found = 1
        print("Found Number")

if(found==0):
    print("Not Found")