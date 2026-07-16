# Day 1 – Python Basics

# Q1. Write a program to print your introduction (Name, Age, College, Branch).
print("Introduction...")
name = "Sahil"
age=20
college = "Sanjivani University"
branch = "AIDS"
print("Hello my name is",name)
print("My age is",age)
print("I am study in",college)
print("My branch name is",branch)

# Q2. Take two numbers as input and print their sum.
a = int(input("Enter First Num:"))
b = int(input("Enter Second Num:"))
sum = a+b
print("Sum of two numbers is",sum)

# Q3. Swap two numbers without using a third variable.
x = 5
y = 10
# The Pythonic way (Tuple Unpacking)
x, y = y, x
print(f"x: {x}, y: {y}")  # Output: x: 10, y: 5

# Q4. Calculate the area of a rectangle.
length = 10
width =20
Area = length*width
print("Area of a rectangle is",Area)

# Q5. Convert Celsius to Fahrenheit.
# Take temperature input from the user in Celsius
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32   # Conversion formula
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")   # Display Result

