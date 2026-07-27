# OOPS(Inheritance)

# Parent Class
# A parent class (Base Class) is the class whose properties are inherited
class Animal:
    def sound(self):
        print("Animal makes a sound")
        
# Child Class
# A child class (Derived Class) inherits from the parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    pass
d=Dog()
d.sound()

# Types of Inheritance
#1. Single Inheritance
# One child inherits from one parent.
class Parent:
    def show(self):
        print("Parent Class")
class Child(Parent):
    pass
c=Child()
c.show()

# 2. Multiple Inheritance
# One child inherits from multiple parents.
class Father:
    def father(self):
        print("Father")
class Mother:
    def mother(self):
        print("Mother")
class Child(Father,Mother):
    pass
c=Child()
c.father()
c.mother()

# 3. Multilevel Inheritance
# A class inherits from another child class.
class GrandFather:
    def gf(self):
        print("Grand Father")
class Father(GrandFather):
    pass
class Son(Father):
    pass
s=Son()
s.gf()

# 4. Hierarchical Inheritance
# Multiple child classes inherit from one parent.
class Parent:
    def display(self):
        print("Parent")
class Child1(Parent):
    pass
class Child2(Parent):
    pass

# Method Overriding
# A child class provides its own implementation of a parent method.
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
d=Dog()
d.sound()

# super() Function
# super() is used to call the parent class constructor or methods.
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
s=Student("Sahil",1)
print(s.name)
print(s.roll)

# Polymorphism
class Bird:
    def sound(self):
        print("Bird Sound")
class Sparrow(Bird):
    def sound(self):
        print("Chirp")
class Crow(Bird):
    def sound(self):
        print("Caw")
s=Sparrow()
c=Crow()
s.sound()
c.sound()