# Dictionary
# A Dictionary stores data in Key : Value pairs.
student = {
    "name": "Sahil",
    "age": 20,
    "branch": "AI & Data Science"
}
print(student)

# Creating Dictionaries
student = {
    "name": "Sahil",
    "age": 20,
    "city": "Nashik"
}

# Access Dictionary Values
print(student["name"])
print(student["age"])

# Using get()
print(student.get("city"))

#Add New Item
student["college"] = "Sanjivani University"
print(student)

#Update Existing Value
student["age"] = 21

# Remove Item
#Using pop()
student.pop("city")

#Using del
del student["age"]

#Clear Dictionary
student.clear()

#Dictionary Methods
#1. keys()
print(student.keys())

#2. values()
print(student.values())

#3. items()
print(student.items())

#4. update()
student.update({"city":"Nashik"})

#Loop Through Dictionary
for key in student:
    print(key)
    
# Print Values
for value in student.values():
    print(value)
    
#Print Both
for key, value in student.items():
    print(key, value)
    
#Membership Operator
print("name" in student)

#Nested Dictionary
students = {
    "student1":{
        "name":"Sahil",
        "marks":90
    },
    "student2":{
        "name":"Rahul",
        "marks":85
    }
}
print(students["student1"]["name"])

#Dictionary Functions
print(len(student))