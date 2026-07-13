# Python Day 8 Assignment

# Q1. Create and Print a Dictionary
print("\nQ1. Create and Print a Dictionary")
student = {
    "name": "Sahil",
    "age": 20,
    "branch": "AI & Data Science"
}
print(student)

# Q2. Access Dictionary Values
print("\nQ2. Access Dictionary Values")
print(student["name"])
print(student["age"])

# Q3. Access Value Using get()
print("\nQ3. Access Value Using get()")
print(student.get("branch"))

# Q4. Add a New Key-Value Pair
print("\nQ4. Add a New Key-Value Pair")
student["college"] = "Sanjivani University"
print(student)

# Q5. Update an Existing Value
print("\nQ5. Update an Existing Value")
student["age"] = 21
print(student)

# Q6. Print All Keys
print("\nQ6. Print All Keys")
print(student.keys())

# Q7. Print All Values
print("\nQ7. Print All Values")
print(student.values())

# Q8. Print All Items
print("\nQ8. Print All Items")
print(student.items())

# Q9. Check Membership
print("\nQ9. Check Membership")
print("name" in student)
print("city" in student)

# Q10. Loop Through Dictionary Keys
print("\nQ10. Loop Through Dictionary Keys")
for key in student:
    print(key)

# Q11. Loop Through Dictionary Values
print("\nQ11. Loop Through Dictionary Values")
for value in student.values():
    print(value)

# Q12. Loop Through Keys and Values
print("\nQ12. Loop Through Keys and Values")
for key, value in student.items():
    print(key, ":", value)

# Q13. Update Dictionary Using update()
print("\nQ13. Update Dictionary Using update()")
student.update({"city": "Nashik"})
print(student)

# Q14. Remove an Item Using pop()
print("\nQ14. Remove an Item Using pop()")
student.pop("city")
print(student)

# Q15. Remove an Item Using del
print("\nQ15. Remove an Item Using del")
del student["college"]
print(student)

# Q16. Find Length of Dictionary
print("\nQ16. Find Length of Dictionary")
print(len(student))

# Q17. Create a Nested Dictionary
print("\nQ17. Create a Nested Dictionary")
students = {
    "student1": {
        "name": "Sahil",
        "marks": 90
    },
    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}
print(students)

# Q18. Access Nested Dictionary
print("\nQ18. Access Nested Dictionary")
print(students["student1"]["name"])
print(students["student2"]["marks"])

# Q19. Mini Project - Student Information System
print("\nQ19. Student Information System")

student_info = {
    "Name": "Sahil",
    "Roll No": 101,
    "Branch": "AI & Data Science",
    "Marks": 88,
    "City": "Nashik"
}

print("Student Details")
for key, value in student_info.items():
    print(key, ":", value)

student_info["Marks"] = 95
student_info["Phone"] = "9876543210"
student_info.pop("City")

print("\nUpdated Student Details")
for key, value in student_info.items():
    print(key, ":", value)

# Q20. Clear Dictionary
print("\nQ20. Clear Dictionary")
sample = {
    "A": 10,
    "B": 20
}
sample.clear()
print(sample)