# Q1. Create a list and access its elements using iter() and next().
numbers=[10,20,30,40,50]
it=iter(numbers)
print("Q1")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# Q2. Create an iterator for a tuple and print all elements.
t=(1,2,3,4,5)
it=iter(t)
print("\nQ2")
for i in it:
    print(i)

# Q3. Write a generator that yields numbers from 1 to 5.
def numbers():
    for i in range(1,6):
        yield i
print("\nQ3")
for i in numbers():
    print(i)

# Q4. Write a generator that yields even numbers from 2 to 20.
def even():
    for i in range(2,21,2):
        yield i
print("\nQ4")
for i in even():
    print(i)

# Q5. Write a generator that yields the squares of numbers from 1 to 10.
def square():
    for i in range(1,11):
        yield i*i
print("\nQ5")
for i in square():
    print(i)

# Q6. Write a generator to generate the Fibonacci series.
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
print("\nQ6")
for i in fibonacci(10):
    print(i)

# Q7. Create a generator expression to print cubes from 1 to 10.
cube=(i**3 for i in range(1,11))
print("\nQ7")
for i in cube:
    print(i)

# Q8. Write a generator that yields the characters of a string one by one.
def characters(text):
    for ch in text:
        yield ch
print("\nQ8")
for i in characters("Python"):
    print(i)

# Q9. Write a generator that counts down from a given number to 1.
def countdown(n):
    while n>=1:
        yield n
        n-=1
print("\nQ9")
for i in countdown(5):
    print(i)

# Q10. Create a program demonstrating the difference between return and yield.
def using_return():
    return "Python"

def using_yield():
    yield "Python"

print("\nQ10")
print(using_return())

g=using_yield()
print(next(g))