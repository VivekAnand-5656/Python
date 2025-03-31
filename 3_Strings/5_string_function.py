# -------- String Functions -----------
# 1 : str.endswith()         || returns True if string ends with substr
str = "i am study python from apna college"      
print("Check End : ",str.endswith("lege"))

# 2 : str.startwith()        || Check if string starts with a specific substring
print("Check Star : ",str.startswith("i am"))

# 3 : str.capitalize()       || Capatilizes 1st charachter of the strings
print("Capatileze First char : " ,str.capitalize())                          # it's not change in original string
str = str.capitalize()                           # now it's change in original strings
print("Capatilize Frst char : ",str)  

# 4 : str.title()            || Capitalizes the first letter of each word 
print("Each word : ",str.title())

# 5 : str.upper()            || Converts all characters to uppercase
print("Convert Upper : ", str.upper())

# 6 : str.lower()            || Converts all characters to lowercase
print("LowerCase : ",str.lower())

# 7 : str.replace(old,new)   || Replaces all occurences of old to new
print("Relpace word to another word : ",str.replace("python","Javascript"))

# 8 : str.find(word)         || returns 1st index of occurrer
print("Find First indx : ",str.find("apna"))                          # Find 1st index position of word 

# 9 : str.count("am")        || counts the occurence of substr
print("Count Occur : ",str.count("am"))                           # count how many times word writes in string

# 10 : str.swapcase()         || Swaps uppercase to lowercase and vice versa
print("Swap : ",str.swapcase())                                   # Swapt uppercase to lowercase and lowercase to uppercase

# 11 : str.strip()            || Removes leading and trailing whitespace
ttr = " hello "
print("Remove White space:",ttr.strip())

# 12 : str.lstrip()           || Removes leading (left) whitespace
print("left whitespace:",ttr.lstrip())

# 13 : str.rstrip()           || Removes trailing (right) whitespace
print("right whitespace:",ttr.rstrip())

# 14 : str.split(seperator)   || Splits string into a list
str2 = "ac,bc,cd"
print("str into list:",str2.split(","))                          # when find (,) the split string into list 

# 15 : str.join(iterable)     || Join elements of an iterable with a string
print("Joins iterable:","-".join(str2))

# 16 : str.isalpha()          || Returns True if all characters are alphabetic
check = "aayan"
print("alphabet:",check.isalpha())

# 17 : str.isdigit()          || Returns True if all characters are digits
nu = "458964"
print("Digit:",nu.isdigit())

# 18 : str.isalnum()          || Returns True if all characters are alphanumeric
chr="vivek1245"
print("Alphanumeric:",chr.isalnum())

# 19 : str.istitle()          || Returns True if the string is in title case
word="Vivek Anand"
print("Is Title:",word.istitle())

# 20 : str.isspace()          || Returns True if the strings contains only spaces
print("Space:",str.isspace())