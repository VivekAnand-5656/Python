# Find and replace "is" with "was" in "This is a simple test.".
words = input("Enter words:")
search = input("Enter search word:")
repl = input("Enter replacing word:")
print("Final:",words.replace(search,repl))