print("Python Day 11 Assignment")

# Q1. Handle ZeroDivisionError
try:
    print(10/0)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Q2. Handle ValueError
try:
    num=int("Python")
except ValueError:
    print("Invalid Value")

# Q3. Using else Block
try:
    print(20/2)
except ZeroDivisionError:
    print("Error")
else:
    print("Division Successful")

# Q4. Using finally Block
try:
    print(100/10)
except:
    print("Error")
finally:
    print("Program Finished")

# Q5. Handle Multiple Exceptions
try:
    num=int(input("Enter Number: "))
    print(100/num)
except ValueError:
    print("Please Enter Numbers Only")
except ZeroDivisionError:
    print("Division by Zero is Not Allowed")

# Q6. Raise an Exception
try:
    age=-5
    if age<0:
        raise ValueError("Age Cannot Be Negative")
except ValueError as e:
    print(e)

# Q7. Import Math Module
import math
print("Square Root:",math.sqrt(64))
print("Factorial:",math.factorial(5))
print("PI:",math.pi)

# Q8. Import Random Module
import random
print("Random Number:",random.randint(1,100))

# Q9. Import Datetime Module
import datetime
print(datetime.datetime.now())

# Q10. Import OS Module
import os
print(os.getcwd())

# Q11. Check File Exists
if os.path.exists("data.txt"):
    print("File Exists")
else:
    print("File Not Found")

# Q12. Import Specific Function
from math import factorial
print("Factorial of 6:",factorial(6))

# Q13. Import Module with Alias
import math as m
print("Square Root:",m.sqrt(81))
print("PI:",m.pi)

# Q14. Calculator Functions
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Division by Zero is Not Allowed"

print("Addition:",add(10,5))
print("Subtraction:",subtract(10,5))
print("Multiplication:",multiply(10,5))
print("Division:",divide(10,5))

# Q15. Mini Project - Calculator with Exception Handling
try:
    num1=float(input("Enter First Number: "))
    num2=float(input("Enter Second Number: "))
    print("Addition:",num1+num2)
    print("Subtraction:",num1-num2)
    print("Multiplication:",num1*num2)
    print("Division:",num1/num2)
except ZeroDivisionError:
    print("Cannot Divide by Zero")
except ValueError:
    print("Invalid Input")
finally:
    print("Calculator Program Finished")
