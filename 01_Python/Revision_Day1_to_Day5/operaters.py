# Day3 - Operaters

# Q6. Check whether a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q7. Find the largest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)

# Q8. Calculate the square and cube of a number
num = int(input("Enter a number: "))
print("Square =", num ** 2)
print("Cube =", num ** 3)

# Q9. Calculate Simple Interest
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
t = float(input("Enter Time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)

# Q10. Calculate the average of five numbers
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
n4 = float(input("Enter fourth number: "))
n5 = float(input("Enter fifth number: "))
average = (n1 + n2 + n3 + n4 + n5) / 5
print("Average =", average)