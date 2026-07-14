# Python Day 10 Notes

# Name
Sahil Shantaram Tarle

# Topic
File Handling

# What is File Handling?

File Handling is used to create, read, write, update and manage files in Python. It helps us store data permanently.

```python
# Opening a File
file = open("data.txt", "r")
```

# Why Do We Use File Handling?

File Handling is used to

- Store data permanently
- Read datasets
- Save reports
- Store logs
- Read CSV files
- Work with Machine Learning datasets

# Opening a File

```python
# Open File in Read Mode
file = open("data.txt", "r")
```

# File Modes

| Mode | Description |
|------|-------------|
| r | Read File |
| w | Write File |
| a | Append File |
| x | Create New File |
| r+ | Read and Write |
| w+ | Write and Read |
| a+ | Append and Read |

# Read Entire File

```python
# Read Complete File
file = open("data.txt", "r")

print(file.read())

file.close()
```

# Read One Line

```python
# Read First Line
file = open("data.txt", "r")

print(file.readline())

file.close()
```

# Read All Lines

```python
# Read All Lines
file = open("data.txt", "r")

print(file.readlines())

file.close()
```

# Write into a File

```python
# Write Data
file = open("data.txt", "w")

file.write("Hello Python")

file.close()
```

# Append Data

```python
# Append Data
file = open("data.txt", "a")

file.write("\nWelcome Sahil")

file.close()
```

# Create a New File

```python
# Create File
file = open("student.txt", "x")

file.close()
```

# Close a File

```python
# Close File
file = open("data.txt", "r")

file.close()
```

Always close the file after using it.

# Using with Statement

The with statement automatically closes the file after use.

```python
# Using with Statement
with open("data.txt", "r") as file:
    print(file.read())
```

# Exception Handling

```python
# File Exception Handling
try:
    file = open("demo.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File Not Found")
```

# Writing Multiple Lines

```python
# Writing Multiple Lines
with open("notes.txt", "w") as file:
    file.write("Python\n")
    file.write("Data Science\n")
    file.write("Machine Learning\n")
```

# Reading Line by Line

```python
# Reading Line by Line
with open("notes.txt", "r") as file:
    for line in file:
        print(line)
```

# Current Working Directory

```python
# Current Working Directory
import os

print(os.getcwd())
```

# Check File Exists

```python
# Check File Exists
import os

print(os.path.exists("data.txt"))
```

# Common File Methods

| Method | Description |
|---------|-------------|
| read() | Read complete file |
| readline() | Read one line |
| readlines() | Read all lines |
| write() | Write data |
| close() | Close file |

# Difference Between File Modes

| Mode | Purpose |
|------|---------|
| r | Read Only |
| w | Write (Overwrite) |
| a | Append |
| x | Create New File |
| r+ | Read and Write |
| a+ | Append and Read |

# Real Life Applications

- Student Management System
- Banking Software
- Hospital Management
- Data Science
- Machine Learning
- CSV Files
- Log Files
- Reports
- Web Applications

# Interview Questions

1. What is File Handling?
2. Why do we use File Handling?
3. What is the difference between r and w mode?
4. What is the difference between w and a mode?
5. What is the with statement?
6. Why should we close a file?
7. What is FileNotFoundError?
8. What does read() do?
9. What does readline() do?
10. What does readlines() do?

# Keywords

File Handling

open()

close()

read()

readline()

readlines()

write()

append()

with

File Modes

Exception Handling

FileNotFoundError

os.getcwd()

os.path.exists()

# Summary

Today I learned about Python File Handling. I learned how to open files, read data, write data, append data, create files, close files, use the with statement, handle file exceptions, check file existence, and display the current working directory. File Handling is widely used in Data Science, Machine Learning, CSV files, log files, and real-world software applications.

# Key Points to Remember

- File Handling stores data permanently.
- open() is used to open files.
- read() reads the complete file.
- readline() reads one line.
- readlines() reads all lines.
- write() writes data.
- a mode appends data.
- w mode overwrites existing data.
- Always close files after use.
- with automatically closes the file.
- Use try-except to handle file errors.
