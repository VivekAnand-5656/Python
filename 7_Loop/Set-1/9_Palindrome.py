# Check if a string is a palindrome (same forward and backward).
word = input("Enter String:")
length=len(word)

reve = ""
for char in word:
    reve = char+reve
print(reve)

if(reve==word):
    print("Palindrome !")
else:
    print("Not Palindrome!")