# Python Day 7 Notes

# Name
Sahil Shantaram Tarle

# Topic
Tuples and Sets

# What is a Tuple?

A tuple is an ordered collection of elements. Tuples are immutable, which means their values cannot be changed after creation.

```python
# Creating a Tuple
student = ("Sahil", 20, "AI & Data Science")
print(student)
```

# Why Use Tuples?

Tuples are used when data should not change.

Examples:
- Date of Birth
- GPS Coordinates
- Student Roll Number
- RGB Colors

# Creating Tuples

```python
# Integer Tuple
numbers = (10, 20, 30, 40)

# String Tuple
fruits = ("Apple", "Banana", "Mango")

# Mixed Tuple
data = (101, "Python", 95.5, True)
```

# Single Element Tuple

```python
# Single Element Tuple
num = (10,)
print(type(num))
```

# Tuple Indexing

```python
# Accessing Tuple Elements
fruits = ("Apple", "Banana", "Mango")

print(fruits[0])
print(fruits[1])
print(fruits[-1])
```

# Tuple Slicing

```python
# Tuple Slicing
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

# Tuple Methods

```python
# count() Method
numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
```

```python
# index() Method
numbers = (10, 20, 30)

print(numbers.index(20))
```

# Tuple Functions

```python
# Tuple Functions
numbers = (10, 20, 30, 40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

# Loop Through Tuple

```python
# Loop Through Tuple
numbers = (10, 20, 30, 40)

for i in numbers:
    print(i)
```

# Tuple Unpacking

```python
# Tuple Unpacking
student = ("Sahil", 20, "AI & Data Science")

name, age, branch = student

print(name)
print(age)
print(branch)
```

# What is a Set?

A set is an unordered collection of unique elements.

Duplicate values are automatically removed.

# Creating Sets

```python
# Creating a Set
fruits = {"Apple", "Banana", "Mango"}

print(fruits)
```

# Duplicate Values

```python
# Duplicate Values are Removed
numbers = {10, 20, 20, 30, 30, 40}

print(numbers)
```

# Add Element

```python
# add() Method
fruits.add("Orange")

print(fruits)
```

# Remove Element

```python
# remove() Method
fruits.remove("Banana")

print(fruits)
```

# Discard Element

```python
# discard() Method
fruits.discard("Apple")

print(fruits)
```

# Pop Method

```python
# pop() Method
fruits.pop()

print(fruits)
```

# Clear Method

```python
# clear() Method
fruits.clear()

print(fruits)
```

# Set Operations

```python
# Creating Two Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

```python
# Union
print(A | B)
```

```python
# Intersection
print(A & B)
```

```python
# Difference
print(A - B)
```

```python
# Symmetric Difference
print(A ^ B)
```

# Membership Operator

```python
# Membership Operator
subjects = {"Python", "SQL", "Machine Learning"}

print("Python" in subjects)
print("Java" in subjects)
```

# Remove Duplicates from List

```python
# Remove Duplicate Values
marks = [80, 90, 80, 75, 90, 95]

unique_marks = set(marks)

print(unique_marks)
```

# Difference Between List, Tuple and Set

| Feature | List | Tuple | Set |
|---------|------|--------|-----|
| Symbol | [] | () | {} |
| Ordered | Yes | Yes | No |
| Mutable | Yes | No | Yes |
| Duplicate Values | Yes | Yes | No |
| Indexing | Yes | Yes | No |

# Real Life Applications

- Student Management System
- Banking System
- Shopping Cart
- Machine Learning
- Data Science
- Removing Duplicate Data
- Contact Management
- GPS Coordinates

# Interview Questions

1. What is a Tuple?
2. What is a Set?
3. What is the difference between List and Tuple?
4. Why are Tuples immutable?
5. What is the difference between remove() and discard()?
6. Can Sets contain duplicate values?
7. What is Union?
8. What is Intersection?
9. What is Tuple Unpacking?
10. Why are Sets unordered?

# Keywords

Tuple

Set

Immutable

Mutable

count()

index()

add()

remove()

discard()

pop()

clear()

Union

Intersection

Difference

Symmetric Difference

Tuple Unpacking

# Summary

Today I learned about Tuples and Sets. I learned how to create tuples and sets, access elements, use tuple methods like count() and index(), and set methods like add(), remove(), discard(), pop(), and clear(). I also learned about union, intersection, difference, symmetric difference, and tuple unpacking. These concepts are useful in Python programming and Data Science.

# Day 7 Completed