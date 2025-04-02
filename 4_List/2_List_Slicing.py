# -------- List Slicing ---------
# Similar to String slicing   list_name[starting_indx:ending_indx] || ending indx in not included
marks = [50,65,12,69,85]
print(marks[1:4])
print(marks[:4])        # Same as [0:4]
print(marks[1:])        # Same as [1:len(marks)]
print(marks[-3:-1])