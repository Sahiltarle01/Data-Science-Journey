# Function

# Q.1 Create a function to print "Hello, Python!".
def greet():
    print("Hello, Python!")
greet()

# Q.2 Create a function that takes two numbers and returns their sum.
def sum(a,b):
    add = a+b
    print(add)
sum(10,20)

# Q.3 Create a function to check whether a number is even or odd.
def even_odd(a):
    if a % 2==0:
        print("This is even number",a)
    else:
        print("This is odd number",a)
even_odd(15)

# Q.4 Create a function to calculate the factorial of a number.
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial_iterative(5))

# Q.5 Create a function to find the largest of three numbers.
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(find_largest(10, 25, 15))

# Q.6 Create a function to count the vowels in a string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count
s = input("Enter a string: ")
print("Number of vowels:", count_vowels(s))

# Q.7 Create a function with a default argument to calculate Simple Interest.
def simple_interest(principal, time, rate=5):
    si = (principal * rate * time) / 100
    return si
p = float(input("Enter Principal: "))
t = float(input("Enter Time (years): "))
print("Simple Interest =", simple_interest(p, t))

# Q.8 Create a function using *args to calculate the sum of multiple numbers.
def calculate_sum(*args):
    total = 0
    for num in args:
        total += num
    return total
print("Sum =", calculate_sum(10, 20, 30, 40, 50))

# Q.9 Create a function using **kwargs to print student details (Name, Age, Branch, College).
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
student_details(
    Name="Sahil ",
    Age=20,
    Branch="AI & Data Science",
    College="Sanjivani University"
)

# Q.10 Write a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
num = int(input("Enter a number: "))
print("Factorial =", factorial(num))