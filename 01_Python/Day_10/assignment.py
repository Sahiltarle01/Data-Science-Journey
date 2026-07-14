# Python Day 10 Assignment
# Q1. Create and Write Data into a File
print("\nQ1. Create and Write Data into a File")
file = open("data.txt", "w")
file.write("Hello Sahil\n")
file.write("Welcome to Python File Handling.\n")
file.write("This is Day 10 Assignment.\n")
file.close()
print("Data Written Successfully")

# Q2. Read Entire File
print("\nQ2. Read Entire File")
file = open("data.txt", "r")
print(file.read())
file.close()

# Q3. Read First Line
print("\nQ3. Read First Line")
file = open("data.txt", "r")
print(file.readline())
file.close()

# Q4. Read All Lines
print("\nQ4. Read All Lines")
file = open("data.txt", "r")
print(file.readlines())
file.close()

# Q5. Append Data
print("\nQ5. Append Data")
file = open("data.txt", "a")
file.write("I want to become a Data Scientist.\n")
file.close()
print("Data Appended Successfully")

# Q6. Read Updated File
print("\nQ6. Read Updated File")
file = open("data.txt", "r")
print(file.read())
file.close()

# Q7. Using with Statement
print("\nQ7. Using with Statement")
with open("data.txt", "r") as file:
    print(file.read())

# Q8. Check File Exists
print("\nQ8. Check File Exists")
import os
if os.path.exists("data.txt"):
    print("File Exists")
else:
    print("File Not Found")

# Q9. Display Current Working Directory
print("\nQ9. Current Working Directory")
print(os.getcwd())

# Q10. Handle File Exception
print("\nQ10. Handle File Exception")
try:
    file = open("demo.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File Not Found")

# Q11. Create Another File
print("\nQ11. Create Another File")
file = open("student.txt", "w")
file.write("Name : Sahil\n")
file.write("Branch : AI & Data Science\n")
file.write("Marks : 90\n")
file.close()
print("student.txt Created")

# Q12. Read student.txt
print("\nQ12. Read student.txt")
with open("student.txt", "r") as file:
    print(file.read())

# Q13. Append Student Data
print("\nQ13. Append Student Data")
with open("student.txt", "a") as file:
    file.write("City : Nashik\n")
print("Data Appended")

# Q14. Read Updated student.txt
print("\nQ14. Read Updated student.txt")
with open("student.txt", "r") as file:
    print(file.read())

# Q15. Mini Project - Student Record System
print("\nQ15. Student Record System")
with open("students.txt", "w") as file:
    file.write("Name : Sahil\n")
    file.write("Roll No : 101\n")
    file.write("Branch : AI & Data Science\n")
    file.write("Marks : 95\n")
    file.write("--------------------------\n")
    file.write("Name : Rahul\n")
    file.write("Roll No : 102\n")
    file.write("Branch : Computer Science\n")
    file.write("Marks : 90\n")
print("Student Records Saved Successfully")
print("\nReading Student Records")
with open("students.txt", "r") as file:
    print(file.read())
