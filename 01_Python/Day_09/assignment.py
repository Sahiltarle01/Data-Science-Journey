# Python Day 9 Assignment

# Q1. Create and Call a Function
print("\nQ1. Create and Call a Function")
def welcome():
    print("Welcome to Python")
welcome()

# Q2. Function to Print Your Name
print("\nQ2. Function to Print Your Name")
def my_name():
    print("My Name is Sahil Shantaram Tarle")
my_name()

# Q3. Function with One Parameter
print("\nQ3. Function with One Parameter")
def greet(name):
    print("Hello", name)
greet("Sahil")

# Q4. Function with Two Parameters
print("\nQ4. Function with Two Parameters")
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student("Sahil", 20)

# Q5. Function to Add Two Numbers
print("\nQ5. Function to Add Two Numbers")
def add(a, b):
    print("Addition:", a + b)
add(10, 20)

# Q6. Function to Subtract Two Numbers
print("\nQ6. Function to Subtract Two Numbers")
def subtract(a, b):
    print("Subtraction:", a - b)
subtract(20, 10)

# Q7. Function to Multiply Two Numbers
print("\nQ7. Function to Multiply Two Numbers")
def multiply(a, b):
    print("Multiplication:", a * b)
multiply(5, 4)

# Q8. Function to Divide Two Numbers
print("\nQ8. Function to Divide Two Numbers")
def divide(a, b):
    print("Division:", a / b)
divide(20, 5)

# Q9. Function with Return Value
print("\nQ9. Function with Return Value")
def square(num):
    return num * num
result = square(5)
print("Square:", result)

# Q10. Function to Find Maximum Number
print("\nQ10. Function to Find Maximum Number")
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print("Maximum:", maximum(25, 18))

# Q11. Function with Default Parameter
print("\nQ11. Function with Default Parameter")
def country(name="India"):
    print(name)
country()
country("Japan")

# Q12. Function with Keyword Arguments
print("\nQ12. Function with Keyword Arguments")
def employee(name, salary):
    print("Name:", name)
    print("Salary:", salary)
employee(salary=50000, name="Rahul")

# Q13. Local Variable
print("\nQ13. Local Variable")
def demo():
    x = 100
    print(x)
demo()

# Q14. Global Variable
print("\nQ14. Global Variable")
y = 200
def show():
    print(y)
show()

# Q15. Lambda Function
print("\nQ15. Lambda Function")
cube = lambda x: x ** 3
print("Cube:", cube(3))

# Q16. Recursive Function
print("\nQ16. Recursive Function")
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)
countdown(5)

# Q17. Built-in Functions
print("\nQ17. Built-in Functions")
numbers = [10, 20, 30, 40, 50]
print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))

# Q18. Function to Find Average
print("\nQ18. Function to Find Average")
def average(a, b, c):
    return (a + b + c) / 3
print("Average:", average(80, 90, 70))

# Q19. Function to Check Even or Odd
print("\nQ19. Function to Check Even or Odd")
def check(num):
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
check(15)
check(20)

# Q20. Mini Project - Student Result Calculator
print("\nQ20. Student Result Calculator")
def total_marks(m1, m2, m3):
    return m1 + m2 + m3
def average_marks(total):
    return total / 3
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"
m1 = 85
m2 = 90
m3 = 80
total = total_marks(m1, m2, m3)
avg = average_marks(total)
print("Marks:", m1, m2, m3)
print("Total:", total)
print("Average:", avg)
print("Grade:", grade(avg))