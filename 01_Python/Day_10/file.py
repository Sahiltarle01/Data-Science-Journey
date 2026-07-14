# File Handling
#Opening a File
file = open("data.txt", "r")

#Read a File
file = open("data.txt", "r")
print(file.read())
file.close()

#Read One Line
file = open("data.txt", "r")
print(file.readline())
file.close()

#Read All Lines
file = open("data.txt", "r")
print(file.readlines())
file.close()

#Write to a File
file = open("data.txt", "w")
file.write("Hello Python")
file.close()

#Append to a File
file = open("data.txt", "a")
file.write("\nWelcome Sahil")
file.close()

#Create a New File
file = open("student.txt", "x")
file.close()

#Close a File
file = open("data.txt", "r")
file.close()

#Using with Statement
with open("data.txt", "r") as file:
    print(file.read())
#The file closes automatically.

#File Exception Handling
try:
    file = open("demo.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File Not Found")
    
#Writing Multiple Lines
with open("notes.txt", "w") as file:
    file.write("Python\n")
    file.write("Data Science\n")
    file.write("Machine Learning")
    
#Reading Line by Line
with open("notes.txt", "r") as file:
    for line in file:
        print(line)
        
#Built-in Functions
import os    # use for remove the file
print(os.getcwd())

import os
print(os.path.exists("data.txt"))