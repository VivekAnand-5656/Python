# Reverse a string using a for loop.
word = input("Enter String:")
length = len(word)

for char in word:
    print(word[length-1]) 
    length-=1