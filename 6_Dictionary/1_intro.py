# ----------- Dictionary in Python -------------
# Dictionaries are used to store data values in key:value pairs
# They are unordered, mutable(changeable) & don't allow duplicate keys.
student = {
    "Name":"Vivek Anand",
    "Age" :19,
    "Marks":[75,85,84],
    "Vehicle":"Bike",
}
print(student)
print(student["Name"])
student["Name"]="Vivan Anand"
print(student["Name"])
print(student)

# Nested Dictionary 
print("Nested")
dictionary = {
    "name":"Satyam Kumar",
    "Age":20,
    "Subject":{
        "phy":97,
        "mth":85,
        "sc":65
    }
}
print(dictionary)                    # print whole dictionary with nested dictionary
print(dictionary["Subject"])        # print only inner dictionary
print(dictionary["Subject"]["mth"]) # print element of inner dictionary
print(dictionary["Subject"]["phy"]) # print element of inner dictionary
print(dictionary["Subject"]["sc"]) # print element of inner dictionary