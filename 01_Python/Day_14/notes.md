# Day 14 - Encapsulation & Abstraction

## What is Encapsulation?

Encapsulation is one of the four pillars of Object-Oriented Programming (OOP).

It is the process of **wrapping data (variables) and methods (functions) into a single class** while restricting direct access to the data.

Encapsulation helps protect data from unauthorized access.

### Real-Life Example

Think of an **ATM Machine**.

- You can withdraw money.
- You can check your balance.
- You cannot directly access the bank database.

The internal details are hidden from the user.

---

# Access Modifiers in Python

Python provides three types of access modifiers.

## 1. Public Members

Public members can be accessed from anywhere.

### Syntax

```python
class Student:
    def __init__(self):
        self.name = "Sahil"

s = Student()
print(s.name)
```

---

## 2. Protected Members

Protected members start with a single underscore (`_`).

They are intended to be used within the class and its child classes.

### Syntax

```python
class Student:
    def __init__(self):
        self._age = 20

s = Student()
print(s._age)
```

> **Note:** Python does not strictly restrict access to protected members. It is a naming convention.

---

## 3. Private Members

Private members start with double underscores (`__`).

They cannot be accessed directly from outside the class.

### Syntax

```python
class Student:
    def __init__(self):
        self.__marks = 95

    def show(self):
        print(self.__marks)

s = Student()
s.show()
```

---

# Getter Method

A Getter method is used to retrieve the value of a private variable.

### Example

```python
class Student:
    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks

s = Student()
print(s.get_marks())
```

---

# Setter Method

A Setter method is used to update the value of a private variable.

### Example

```python
class Student:
    def __init__(self):
        self.__marks = 90

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

s = Student()
s.set_marks(95)
print(s.get_marks())
```

---

# Advantages of Encapsulation

- Improves Data Security
- Hides Internal Data
- Better Code Organization
- Easy Maintenance
- Increases Code Reusability

---

# What is Abstraction?

Abstraction is the process of **hiding implementation details** and showing only the essential features to the user.

The user only knows **what** an object does, not **how** it does it.

### Real-Life Example

When driving a car:

- You use the steering wheel.
- You press the accelerator.
- You don't need to know how the engine works internally.

---

# Abstract Class

An Abstract Class is a class that cannot be instantiated directly.

It is created using the **ABC (Abstract Base Class)** module.

### Syntax

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

# Abstract Method

An Abstract Method is a method declared without implementation.

Every child class must implement the abstract method.

### Example

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

d = Dog()
d.sound()
```

---

# Advantages of Abstraction

- Hides Complex Logic
- Improves Security
- Makes Programs Easier to Understand
- Reduces Complexity
- Easy Maintenance

---

# Difference Between Encapsulation and Abstraction

| Encapsulation | Abstraction |
|---------------|-------------|
| Hides Data | Hides Implementation |
| Uses Access Modifiers | Uses Abstract Classes |
| Protects Data | Simplifies Complex Systems |
| Focuses on Data Security | Focuses on Essential Features |

---

# Important Terms

| Term | Meaning |
|------|---------|
| Encapsulation | Wrapping data and methods into one class |
| Public Member | Accessible from anywhere |
| Protected Member | Intended for class and subclasses |
| Private Member | Accessible only inside the class |
| Getter | Reads private data |
| Setter | Updates private data |
| Abstraction | Hides implementation details |
| Abstract Class | A class with one or more abstract methods |
| Abstract Method | A method without implementation |

---

# Interview Questions

### 1. What is Encapsulation?

Encapsulation is the process of wrapping data and methods into a single class while restricting direct access to the data.

### 2. What are Access Modifiers in Python?

- Public
- Protected
- Private

### 3. What is a Private Variable?

A private variable starts with `__` and cannot be accessed directly outside the class.

### 4. What is the purpose of Getter and Setter methods?

Getter methods retrieve private data, while Setter methods modify private data safely.

### 5. What is Abstraction?

Abstraction hides implementation details and exposes only the necessary functionality.

### 6. What is an Abstract Class?

An Abstract Class is a class that cannot be instantiated and may contain abstract methods.

### 7. What is an Abstract Method?

An Abstract Method is declared without implementation and must be implemented by child classes.

### 8. Which module is used for Abstraction in Python?

The `abc` module.

---

# Key Points

- Encapsulation protects data by controlling access.
- Public members are accessible everywhere.
- Protected members use a single underscore (`_`).
- Private members use double underscores (`__`).
- Getter methods read private variables.
- Setter methods modify private variables.
- Abstraction hides implementation details.
- Abstract classes are created using the `ABC` module.
- Child classes must implement all abstract methods.

---

# Summary

Today you learned:

- Encapsulation
- Public Members
- Protected Members
- Private Members
- Getter Methods
- Setter Methods
- Abstraction
- Abstract Classes
- Abstract Methods
- Difference between Encapsulation and Abstraction

---

# Next Topic

## Day 15 - Python Packages & Advanced Modules

Topics:
- Packages in Python
- Creating Your Own Package
- Importing Modules from Packages
- Built-in Modules
- Useful Standard Library Modules
- `os` Module
- `sys` Module
- `math` Module
- `random` Module