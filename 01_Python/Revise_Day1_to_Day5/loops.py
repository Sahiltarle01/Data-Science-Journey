# Day 4 - Loops

# Q16. Print numbers from 1 to 100
for i in range(1, 101):
    print(i)

# Q17. Print the multiplication table of a given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Q18. Find the factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

# Q19. Print the Fibonacci series up to n terms
n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
print()

# Q20. Count the number of digits in a number
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print("Number of digits =", count)