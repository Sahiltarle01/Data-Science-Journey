# Object oriented programming

# 1. Class
# A class is a blueprint.
class Student:
    pass

# 2. Object
# An object is created from a class.
class Student:
    pass
s1 = Student()
print(s1)

# 3. Constructor (__init__())
# A constructor runs automatically whenever an object is created.
class Student:
    def __init__(self):
        print("Object Created")
s1 = Student()

# 4. self Keyword
# self refers to the current object.
class Student:
    def display(self):
        print("Hello")
s1 = Student()
s1.display()

# 5. Attributes
# Attributes store object data.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
s1 = Student("Sahil",20)
print(s1.name)
print(s1.age)

# 6. Methods
# Methods are functions inside a class.
class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
s1=Student("Sahil")
s1.display()

# 7. Multiple Objects
class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(self.name)
s1=Student("Sahil")
s2=Student("Rahul")
s1.display()
s2.display()

# 8. Real Example
class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand :",self.brand)
        print("Price :",self.price)
lap=Laptop("Dell",65000)
lap.display()

