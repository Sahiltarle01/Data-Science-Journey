# Error Handling
# Example 
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# try Block
try:
    number = 10
    print(number)
except:
    print("Error")
    
# except Block
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
    
# else Block
# Runs only if there is no exception.
try:
    print(10 / 2)
except:
    print("Error")
else:
    print("Executed Successfully")

# finally Block (Always executes whether an exception occurs or not.)
try:
    print(10 / 2)
except:
    print("Error")
finally:
    print("Program Finished")
    
# Multiple Exceptions
try:
    num = int(input("Enter Number: "))
    print(100 / num)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Cannot Divide by Zero")
    
# Raising an Exception
age = -5
if age < 0:
    raise ValueError("Age cannot be negative.")

# Example
a = input("Enter the number: ")
print(f"Multiplication of table {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!")
print("This is a ending line of a code...")

# Importing a Module
import math
print(math.sqrt(25))

# Import Specific Function
from math import factorial
print(factorial(5))

# Import with Alias
import math as m
print(m.pi)

#Useful Built-in Modules
math
import math
print(math.sqrt(64))
print(math.factorial(5))
print(math.pi)
 
#random
import random
print(random.randint(1, 100))

# datetime
import datetime
print(datetime.datetime.now())

# os
import os
print(os.getcwd())