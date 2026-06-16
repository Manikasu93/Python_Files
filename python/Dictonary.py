# Exercise 1: Basic Dictionary Operations
d1={
    "fname":"Mani",
    "lname":"Knata",
    "age":"24"
}

print(d1)
print(d1["age"]) #Printing Specific keyvalue
d1["location"]="Noida" #adding
print(d1)
del d1["age"]
print(d1)
d1["lname"]="Eswar"
print(d1)

# Exercise 2: Dictionary Operations

# Exercise 3: Dictionary from Two Lists
d1=["Fname","Lname","age"]
d2=["Ramesh","K","27"]
my_dict=dict(zip(d1,d2))
print(my_dict)


# Exercise 4: Clear Dictionary
d1={
    "fname":"Mani",
    "lname":"Knata",
    "age":"24"
}
print(d1)
d1.clear()
print(d1)

# Exercise 5: Merge Dictionaries
d1={
    "fname":"Mani",
    "lname":"Knata",
    "age":"24"
}
d2={
    "fname":"apple",
    "2fname":"banana",
}
m={**d1,**d2}
print(m)


# Exercise 6: Access Nested Dictionary
person = {"name": "Carol", 
          "address": {"city": "Paris", 
                      "zip": "75001"}}
print(person["address"]["zip"])

# Exercise 7: Access ‘history’ Key From a Nested Dictionary

student = {"name": "Dave",
            "grades": {"math": 88, 
                       "science": 92,
                         "history": 75}}
print(student["grades"]["history"])

# Exercise 8: Initialize Dictionary with Default Values

# Given Input: keys = ["math", "science", "english", "history"] and default = 0
keys = ["math", "science", "english", "history"]
default = 0
key1=dict.fromkeys(keys,default)
print(key1)
# Expected Output: {'math': 0, 'science': 0, 'english': 0, 'history': 0}

# Exercise 9: Rename a Key of Dictionary
d1={
    "fname":"Mani",
    "lname":"Knata",
    "age":"24"
}
d1["lastn"]=d1.pop("lname")
print(d1)
# Exercise 10: Delete a List of Keys
d1={
    "fname":"Mani",
    "lname":"Knata",
    "age":"24"
}
d2=["lname","age"]

for i in d2:

    d1.pop(i)

print(d1)