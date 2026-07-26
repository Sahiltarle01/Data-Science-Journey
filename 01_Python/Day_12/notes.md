# Day 12 - Object-Oriented Programming (OOP)

## What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm that uses **Classes** and **Objects** to organize code. It helps make programs reusable, organized, and easy to maintain.

**Example:**
- Class = Blueprint of a House
- Object = Actual House

---

# Class

A class is a blueprint for creating objects.

### Syntax

```python
class Student:
    pass
```

---

# Object

An object is an instance of a class.

### Syntax

```python
class Student:
    pass

s1 = Student()
```

---

# Constructor (__init__)

A constructor is a special method that is automatically called when an object is created.

### Syntax

```python
class Student:
    def __init__(self):
        print("Constructor Called")

s1 = Student()
```

---

# self Keyword

- `self` refers to the current object.
- It is used to access attributes and methods of the class.

### Example

```python
class Student:
    def display(self):
        print("Hello")

s1 = Student()
s1.display()
```

---

# Attributes

Attributes are variables that belong to an object.

### Example

```python
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Student("Sahil",20)
```

---

# Methods

Methods are functions defined inside a class.

### Example

```python
class Student:
    def display(self):
        print("Hello Python")
```

---

# Multiple Objects

One class can create multiple objects.

### Example

```python
class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Sahil")
s2 = Student("Rahul")
```

---

# Real-Life Example

```python
class Laptop:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)

lap = Laptop("Dell",65000)
lap.display()
```

---

# Advantages of OOP

- Code Reusability
- Easy Maintenance
- Better Code Organization
- Real-World Modeling
- Easy Debugging
- Faster Development

---

# Important Terms

| Term | Meaning |
|------|---------|
| Class | Blueprint |
| Object | Instance of a Class |
| Constructor | Special Method (`__init__`) |
| self | Refers to Current Object |
| Attribute | Variable inside a Class |
| Method | Function inside a Class |

---

# Interview Questions

### 1. What is OOP?
Object-Oriented Programming is a programming paradigm based on classes and objects.

### 2. What is a Class?
A class is a blueprint used to create objects.

### 3. What is an Object?
An object is an instance of a class.

### 4. What is a Constructor?
A constructor is a special method (`__init__`) that is automatically called when an object is created.

### 5. What is the use of self?
`self` refers to the current object and is used to access attributes and methods.

### 6. What are Attributes?
Attributes are variables that store data inside an object.

### 7. What are Methods?
Methods are functions defined inside a class.

---

# Key Points

- OOP stands for Object-Oriented Programming.
- A class is a blueprint.
- An object is created from a class.
- `__init__()` is called automatically when an object is created.
- `self` refers to the current object.
- Attributes store object data.
- Methods define object behavior.
- One class can create multiple objects.

---

# Summary

Today you learned:

- Introduction to OOP
- Class
- Object
- Constructor (`__init__`)
- self Keyword
- Attributes
- Methods
- Multiple Objects
- Real-Life Examples
