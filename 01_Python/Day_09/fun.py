# Function
# Example
def greet():
    print("Welcome Sahil")
greet()

#Function with Parameters
def greet(name):
    print("Hello", name)
greet("Sahil")
greet("Rahul")

#Function with Multiple Parameters
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student("Sahil", 20)

#Function with Return Value
def add(a, b):
    return a + b
result = add(10, 20)
print(result)

#Difference Between print() and return
#1. print():This only displays output.
def demo():
    print("Python")
demo()

#2. return::return sends a value back to the caller.
def add(a, b):
    return a + b
x = add(5, 10)
print(x)

#Default Parameters
def country(name="India"):
    print(name)
country()
country("Japan")

#Keyword Arguments
def student(name, age):
    print(name)
    print(age)
student(age=20, name="Sahil")

#Variable Scope
#1. Local Variable
def demo():
    x = 100
    print(x)
demo()

#2. Global Variable
x = 100
def demo():
    print(x)
demo()

#Lambda Function
#A lambda function is a small anonymous function.
square = lambda x: x * x
print(square(5))

#Recursive Function
#A function calling itself is called recursion.
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)

#Built-in Functions
numbers = [10,20,30]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# WAF to print a number is even or odd
def even_odd(num):
    if num%2==0:
        print("This is even number:",num)
    else:
        print("This is odd number:",num)
even_odd(10)
even_odd(17)