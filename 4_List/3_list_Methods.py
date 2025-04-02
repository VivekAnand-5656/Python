# -------- List Methods -----------
list = [45,85,96,20,25]
print("Orignal:",list)
# 1 : .append(value)            || adds one element at the end
list.append(100)
print("Appended:",list)

# 2 : .sort()                   || sorts in ascending order
list.sort()
print("Sorting:",list)

# 3 : .sort(reverse=True)       || sorts in descending order
list.sort(reverse=True)
print("Dscending:",list)

# 4 : .reverse()                || reverses list
newlist = [45,88,21,30,40]
newlist.reverse()
print("Reverse:",newlist)

# 5 : .insert(index,el)         || insert element at index
newlist.insert(2,100)
print("Insert by index:",newlist)

# 6 : .remove(value)            || remover first occurrence of element
newlist.remove(100)
print("Remove:",newlist)

# 7 : .pop(index)               || removes element at index
newlist.pop(2)
print("remove by index:",newlist)