# Encapsulation
'''What is Encapsulation?
Encapsulation means wrapping data (variables) and methods (functions) into a single unit (class) and controlling access to the data.

Real-Life Example
Think of an ATM Machine.
You can withdraw money.
You can check your balance.
You cannot directly access the bank's database.
The internal data is hidden from the user.'''

#Access Modifiers in Python
# 1. Public Members(Public members can be accessed from anywhere)
class Student:
    def __init__(self):
        self.name="Sahil"
s=Student()
print(s.name)

# 2. Protected Members
# Protected members start with a single underscore _.
# They should be accessed only within the class and its child classes.
class Student:
    def __init__(self):
        self._age=20
s=Student()
print(s._age)

# Private Members
# Private members start with double underscores __.
# They cannot be accessed directly outside the class.
class Student:
    def __init__(self):
        self.__marks=95

s=Student()
print(s.__marks)   # Error

# To access private data, use a method.
class Student:
    def __init__(self):
        self.__marks=95
    def show(self):
        print(self.__marks)
s=Student()
s.show()

#Getter and Setter Methods
# 1.Getter (Used to retrieve private data)
class Student:
    def __init__(self):
        self.__marks=90
    def get_marks(self):
        return self.__marks
s=Student()
print(s.get_marks())

# Setter (Used to update private data)
class Student:
    def __init__(self):
        self.__marks=90
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
s=Student()
s.set_marks(98)
print(s.get_marks())

