# --------- Dictionary Methods ------------
# .keys()                       || returns all keys
student = {
    "name":"Vivek anand",
    "Age":45,
    "Marks":95
}
print(student.keys())
print(list(student.keys()))     # Convert in list   Typecast
print(len(list(student.keys())))    # extract length of student keys

print("Values method")
# .values()                       || return all values
print(student.values())
print(list(student.values()))   # convert in list

print("item method")
# .items()                        || returns all (key,val) pairs as tuples
emp = {
    "name":"Vivek Anand",
    "Det":{
        "ID":102,
        "salary":55000,
        "Deprtment":"HR"
    }
}

print(emp.items())                  # return all pair values as tuple form
print(list(emp.items()))            # convert in lis 
pairs = list(emp.items())
print(pairs[0])                     # access first pair
print(pairs[1])                     # access first pair

print(".get method")
# .get("key")                       || returns the key according to value
print(emp.get("name"))

print(".update(newdict)")
# .update(newDict)                  || inserts the specified items to the dictionary
emp.update({"Age":19})              # inserts new key in dictionary
print(emp)

emp.update({"name":"Khushi Kumar"}) # update old key value 
print(emp)

new_dict = {"city":"Patna","Mobile":7481873859}
emp.update(new_dict)                # insert new dictionary
print(emp)      

