# ---------- Break & Continue --------------

# Break
data = [10,50,26,35,89,52,86,64,98,256,250]
length = len(data)
srch = int(input("Enter Search Number:"))
i=0
while i<length:
    if(data[i]==srch):
        break
    print(data[i])
    i+=1

# Continue
newsrch = int(input("Enter Search:"))
j=0
while j<length:
    if(data[j]==newsrch):
        j+=1
        continue
    print(data[j])
    j+=1