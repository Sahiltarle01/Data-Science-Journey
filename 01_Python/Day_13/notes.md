# Day 13 - Inheritance in Python

## What is Inheritance?

Inheritance is an Object-Oriented Programming (OOP) feature that allows one class to inherit the properties and methods of another class.

It promotes **Code Reusability** and reduces duplicate code.

**Example:**
- Parent Class → Animal
- Child Class → Dog

A Dog is an Animal, so it can use the properties and methods of the Animal class.

---

# Parent Class

A Parent Class (Base Class) is the class whose properties and methods are inherited.

### Example

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")
```

---

# Child Class

A Child Class (Derived Class) inherits from the Parent Class.

### Example

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()
```

---

# Types of Inheritance

## 1. Single Inheritance

One child class inherits from one parent class.

### Example

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## 2. Multiple Inheritance

One child class inherits from multiple parent classes.

### Example

```python
class Father:
    pass

class Mother:
    pass

class Child(Father, Mother):
    pass
```

---

## 3. Multilevel Inheritance

A child class becomes the parent of another class.

### Example

```python
class GrandFather:
    pass

class Father(GrandFather):
    pass

class Son(Father):
    pass
```

---

## 4. Hierarchical Inheritance

Multiple child classes inherit from one parent class.

### Example

```python
class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass
```

---

# Method Overriding

Method Overriding means a child class provides its own implementation of a method that already exists in the parent class.

### Example

```python
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")
```

---

# super() Function

The `super()` function is used to call the parent class constructor or methods from the child class.

### Example

```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
```

---

# Polymorphism (Introduction)

Polymorphism means **One Method, Many Forms**.

Different classes can have methods with the same name but different implementations.

### Example

```python
class Bird:
    def sound(self):
        print("Bird Sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

class Crow(Bird):
    def sound(self):
        print("Caw")
```

---

# Advantages of Inheritance

- Code Reusability
- Reduces Code Duplication
- Easy Maintenance
- Faster Development
- Better Code Organization

---

# Important Terms

| Term | Meaning |
|------|---------|
| Parent Class | Base Class |
| Child Class | Derived Class |
| Inheritance | Reusing properties and methods of another class |
| Method Overriding | Redefining a parent class method |
| super() | Calls the parent class constructor or method |
| Polymorphism | One Method, Many Forms |

---

# Interview Questions

### 1. What is Inheritance?
Inheritance is the process of acquiring the properties and methods of one class into another class.

### 2. What is a Parent Class?
A Parent Class is the class whose members are inherited.

### 3. What is a Child Class?
A Child Class is the class that inherits from the Parent Class.

### 4. What is Method Overriding?
Method Overriding means redefining a method of the parent class in the child class.

### 5. What is the use of `super()`?
It is used to access the parent class constructor or methods.

### 6. What is Polymorphism?
Polymorphism means one method can have different implementations in different classes.

### 7. Name the types of inheritance in Python.
- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance

---

# Key Points

- Inheritance allows code reuse.
- A Child Class inherits from a Parent Class.
- Python supports four main types of inheritance.
- Method Overriding changes the behavior of a parent method.
- `super()` calls the parent class constructor or methods.
- Polymorphism allows the same method name with different implementations.

---

# Summary

Today you learned:

- Inheritance
- Parent and Child Classes
- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Method Overriding
- super() Function
- Introduction to Polymorphism
