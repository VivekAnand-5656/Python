# ------Rules In Pyhton --------
# ----Expression Execution----
# String & Numeric values can operate together with * 
a,b=2,3
txt="@"
print(2*txt*3)

# String & String can operate with +
a2,b2="2",3
txt2="@"
print((a2+txt2)*b2)  # Concatenation

# Numeric values can operate with all arithmetic operators
ag,bg=2,3
cg=4
print(ag+bg+cg)

# Arithmetic expression with integer and float will result in float
ac,ad=10,5.2
cc=ac*ad        
print(cc)