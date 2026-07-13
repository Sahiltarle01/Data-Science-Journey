# Python Day 9 Notes

# Name
Sahil Shantaram Tarle

# Topic
Functions

# What is a Function?

A function is a reusable block of code that performs a specific task. It helps avoid writing the same code multiple times.

```python
# Creating a Function
def greet():
    print("Hello Python")

greet()
```

# Why Do We Use Functions?

Functions help us:

- Reduce code repetition
- Improve readability
- Reuse code
- Make programs easier to maintain

# Creating a Function

```python
# Function Without Parameters
def hello():
    print("Welcome to Python")

hello()
```

# Function with One Parameter

```python
# Function with One Parameter
def greet(name):
    print("Hello", name)

greet("Sahil")
```

# Function with Multiple Parameters

```python
# Function with Two Parameters
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Sahil", 20)
```

# Function with Return Value

```python
# Function Returning a Value
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

# Difference Between print() and return

print() displays the output on the screen.

return sends the result back to the function call.

```python
# Using print()
def demo():
    print("Python")

demo()
```

```python
# Using return
def square(num):
    return num * num

print(square(5))
```

# Default Parameter

```python
# Default Parameter
def country(name="India"):
    print(name)

country()
country("Japan")
```

# Keyword Arguments

```python
# Keyword Arguments
def employee(name, salary):
    print(name)
    print(salary)

employee(salary=50000, name="Rahul")
```

# Local Variable

A local variable is created inside a function and can only be used inside that function.

```python
# Local Variable
def demo():
    x = 100
    print(x)

demo()
```

# Global Variable

A global variable is created outside the function and can be accessed anywhere.

```python
# Global Variable
x = 100

def show():
    print(x)

show()
```

# Lambda Function

A lambda function is a small anonymous function.

```python
# Lambda Function
square = lambda x: x * x

print(square(5))
```

# Recursive Function

A recursive function calls itself until a condition becomes false.

```python
# Recursive Function
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)
```

# Built-in Functions

```python
# Built-in Functions
numbers = [10, 20, 30, 40]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

# Function to Find Addition

```python
# Addition Function
def add(a, b):
    return a + b

print(add(15, 10))
```

# Function to Find Square

```python
# Square Function
def square(num):
    return num * num

print(square(8))
```

# Function to Find Maximum

```python
# Maximum Function
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(20, 15))
```

# Function to Find Average

```python
# Average Function
def average(a, b, c):
    return (a + b + c) / 3

print(average(80, 90, 100))
```

# Difference Between Function Types

| Function Type | Example |
|--------------|---------|
| No Parameter | hello() |
| Parameter | greet(name) |
| Return Value | add(a, b) |
| Lambda Function | lambda x:x*x |
| Recursive Function | countdown() |

# Real Life Applications

- Student Management System
- Banking Software
- ATM Machine
- Data Science
- Machine Learning
- Web Development
- Games
- APIs
- Automation Scripts

# Interview Questions

1. What is a Function?
2. Why do we use Functions?
3. What is the difference between print() and return?
4. What are Parameters?
5. What are Arguments?
6. What is a Lambda Function?
7. What is a Recursive Function?
8. What is the difference between Local and Global Variables?
9. What is a Built-in Function?
10. Why are Functions important?

# Keywords

Function

Parameter

Argument

Return

print()

Lambda Function

Recursive Function

Local Variable

Global Variable

Default Parameter

Keyword Argument

Built-in Function

# Summary

Today I learned about Python Functions. I learned how to create functions, call functions, use parameters, return values, default parameters, keyword arguments, local variables, global variables, lambda functions, recursive functions, and built-in functions. Functions help make code reusable, organized, and easier to maintain. They are widely used in Python, Data Science, Machine Learning, Web Development, and Automation.

# Key Points to Remember

- Functions make code reusable.
- A function is created using the def keyword.
- Parameters receive values.
- Arguments are passed while calling a function.
- return sends a value back.
- print() only displays output.
- Lambda functions are anonymous functions.
- Recursive functions call themselves.
- Local variables exist inside functions.
- Global variables can be accessed throughout the program.
