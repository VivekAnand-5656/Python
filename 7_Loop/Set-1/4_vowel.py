# Count the number of vowels in a string.
string = input("Enter String:")
count =0
for char in string:
    if(char=="a" or char=="A" or char=="e" or char=="E" or char=="i" or char=="I" or char=="o" or char=="O" or char=="u" or char=="U"):
        count+=1

print("Vowels = ",count)