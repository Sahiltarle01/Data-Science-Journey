# Python Day 7 Assignment

# Q1. Create and Print a Tuple
print("\nQ1. Create and Print a Tuple")
t1 = ("Apple", "Banana", "Mango", "Banana")
print(t1)

# Q2. Print First Element of Tuple
print("\nQ2. Print First Element of Tuple")
print(t1[0])

# Q3. Print Last Element of Tuple
print("\nQ3. Print Last Element of Tuple")
print(t1[-1])

# Q4. Perform Tuple Slicing
print("\nQ4. Perform Tuple Slicing")
print(t1[1:3])

# Q5. Count Occurrence of an Element
print("\nQ5. Count Occurrence of 'Banana'")
print(t1.count("Banana"))

# Q6. Find Index of an Element
print("\nQ6. Find Index of 'Mango'")
print(t1.index("Mango"))

# Q7. Find Length of Tuple
print("\nQ7. Find Length of Tuple")
numbers = (10, 20, 30, 40, 50)
print(len(numbers))

# Q8. Find Maximum, Minimum and Sum
print("\nQ8. Find Maximum, Minimum and Sum")
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Q9. Print Tuple Elements Using Loop
print("\nQ9. Print Tuple Elements Using Loop")
for i in numbers:
    print(i)

# Q10. Create and Print a Set
print("\nQ10. Create and Print a Set")
set1 = {"Apple", "Banana", "Mango"}
print(set1)

# Q11. Add an Element into Set
print("\nQ11. Add an Element into Set")
set1.add("Orange")
print(set1)

# Q12. Remove an Element from Set
print("\nQ12. Remove an Element from Set")
set1.remove("Banana")
print(set1)

# Q13. Discard an Element
print("\nQ13. Discard an Element")
set1.discard("Pineapple")
print(set1)

# Q14. Remove Random Element Using pop()
print("\nQ14. Remove Random Element Using pop()")
set1.pop()
print(set1)

# Q15. Perform Union Operation
print("\nQ15. Union of Two Sets")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)

# Q16. Perform Intersection Operation
print("\nQ16. Intersection of Two Sets")
print(A & B)

# Q17. Perform Difference Operation
print("\nQ17. Difference of Two Sets")
print(A - B)

# Q18. Perform Symmetric Difference
print("\nQ18. Symmetric Difference")
print(A ^ B)

# Q19. Remove Duplicate Values from List
print("\nQ19. Remove Duplicate Values from List")
marks = [80, 90, 80, 75, 90, 95, 75]
unique_marks = set(marks)
print(unique_marks)

# Q20. Check Membership in Set
print("\nQ20. Check Membership")
subjects = {"Python", "SQL", "Machine Learning"}
print("Python" in subjects)
print("Java" in subjects)

# Q21. Tuple Unpacking
print("\nQ21. Tuple Unpacking")
student = ("Sahil", 20, "AI & Data Science")
name, age, branch = student
print(name)
print(age)
print(branch)

# Q22. Mini Project - Student Subject Manager
print("\nQ22. Student Subject Manager")
student1 = {"Python", "SQL", "Machine Learning", "Statistics"}
student2 = {"Python", "Excel", "Statistics", "Power BI"}
print("Student 1 Subjects:", student1)
print("Student 2 Subjects:", student2)
print("Common Subjects:", student1 & student2)
print("All Subjects:", student1 | student2)
print("Only Student 1 Subjects:", student1 - student2)
print("Only Student 2 Subjects:", student2 - student1)
print("\nDay 7 Assignment Completed Successfully")