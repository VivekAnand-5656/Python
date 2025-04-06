# Search for a number x in this tuple using loop

tpl = (1,4,9,16,25,36,49,64,81,100)
length = len(tpl)

srch = int(input("Enter searching:"))
found = 0
i=0
while i<length:
    if(tpl[i]==srch):
        found=1
        print("Found = ",tpl[i])
    
    i+=1

if(found==0):
    print("Not Found")