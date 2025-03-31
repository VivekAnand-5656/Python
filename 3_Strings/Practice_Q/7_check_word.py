# Check if the word "Python" is present in the string "I am learning Python.". 
sen = input("Enter sentence1:")
check = input("Enter Checking word:")
index = sen.find(check)
if check in sen:
    print(check,f"Found at {index}")
else:
    print("Not Present!")