# Python Day 11 Notes

# Name
Sahil Shantaram Tarle

# Topic
Exception Handling and Modules

# What is Exception Handling?

Exception Handling is used to handle runtime errors without stopping the program execution.

```python
# Example of Exception Handling
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

# Why Do We Use Exception Handling?

- Prevent program crashes
- Handle runtime errors
- Display user-friendly messages
- Improve program reliability

# try Block

```python
# try Block
try:
    number=10
    print(number)
except:
    print("Error")
```

# except Block

```python
# except Block
try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero is not allowed")
```

# else Block

The else block executes only if no exception occurs.

```python
# else Block
try:
    print(20/2)
except:
    print("Error")
else:
    print("Executed Successfully")
```

# finally Block

The finally block always executes whether an exception occurs or not.

```python
# finally Block
try:
    print(100/10)
except:
    print("Error")
finally:
    print("Program Finished")
```

# Multiple Exceptions

```python
# Multiple Exceptions
try:
    num=int(input("Enter Number: "))
    print(100/num)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
```

# Raising an Exception

```python
# raise Keyword
age=-5

if age<0:
    raise ValueError("Age cannot be negative")
```

# What is a Module?

A module is a Python file that contains functions, variables, and classes which can be imported into another Python program.

# Importing a Module

```python
# Import Module
import math

print(math.sqrt(25))
```

# Import Specific Function

```python
# Import Specific Function
from math import factorial

print(factorial(5))
```

# Import Module with Alias

```python
# Import Alias
import math as m

print(m.pi)
```

# Math Module

```python
# Math Module
import math

print(math.sqrt(64))
print(math.factorial(5))
print(math.pi)
```

# Random Module

```python
# Random Module
import random

print(random.randint(1,100))
```

# Datetime Module

```python
# Datetime Module
import datetime

print(datetime.datetime.now())
```

# OS Module

```python
# OS Module
import os

print(os.getcwd())
print(os.path.exists("data.txt"))
```

# Creating Your Own Module

calculator.py

```python
# calculator.py

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
```

main.py

```python
# main.py

import calculator

print(calculator.add(10,20))
print(calculator.subtract(20,10))
```

# Difference Between try except else finally

| Block | Purpose |
|--------|----------|
| try | Write risky code |
| except | Handle errors |
| else | Executes if no error occurs |
| finally | Always executes |

# Difference Between import and from import

| import | from import |
|---------|-------------|
| Imports entire module | Imports only required function |
| Uses module name | No module name required |

# Real Life Applications

- Banking Systems
- ATM Software
- Hospital Management
- Login Systems
- Data Science
- Machine Learning
- APIs
- Automation Scripts

# Interview Questions

1. What is Exception Handling?
2. Why do we use try and except?
3. What is the difference between else and finally?
4. What is raise?
5. What is a Module?
6. What is the difference between import and from import?
7. What is an alias?
8. Name some built-in modules.
9. How do you create your own module?
10. Why are modules important?

# Keywords

Exception

try

except

else

finally

raise

Module

import

from

as

math

random

datetime

os

# Summary

Today I learned about Exception Handling and Modules in Python. I learned how to use try, except, else, finally, and raise to handle errors. I also learned how to import built-in modules like math, random, datetime, and os, and how to create my own module. These concepts help build reliable, reusable, and professional Python applications.

# Key Points to Remember

- Exception Handling prevents program crashes.
- try contains risky code.
- except handles errors.
- else executes only when no error occurs.
- finally always executes.
- raise is used to generate custom exceptions.
- Modules help organize reusable code.
- import loads a complete module.
- from import loads specific functions.
- Built-in modules save development time.
