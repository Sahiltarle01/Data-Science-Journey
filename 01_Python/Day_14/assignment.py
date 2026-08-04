# Python Day 14 Assignment
# Q1. Create a class with a public variable and access it.
class Student:
    def __init__(self):
        self.name="Sahil"
print("Q1")
s=Student()
print(s.name)

# Q2. Create a class with a protected variable and print it.
class Student:
    def __init__(self):
        self._age=20
print("\nQ2")
s=Student()
print(s._age)

# Q3. Create a class with a private variable and access it using a method.
class Student:
    def __init__(self):
        self.__marks=90
    def show(self):
        print(self.__marks)
print("\nQ3")
s=Student()
s.show()

# Q4. Create getter and setter methods for a private variable.
class Student:
    def __init__(self):
        self.__marks=85
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        self.__marks=marks
print("\nQ4")
s=Student()
print("Old Marks:",s.get_marks())
s.set_marks(95)
print("New Marks:",s.get_marks())

# Q5. Create a BankAccount class with private balance and methods.
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient Balance")
    def display(self):
        print("Balance:",self.__balance)
print("\nQ5")
b=BankAccount(1000)
b.deposit(500)
b.withdraw(300)
b.display()

# Q6. Create an abstract class Shape with abstract method area().
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
print("\nQ6")
print("Abstract class Shape created.")

# Q7. Create child class Circle that implements area().
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area:",3.14*self.radius*self.radius)
print("\nQ7")
c=Circle(5)
c.area()

# Q8. Create an abstract class Vehicle with start() implemented in Car.
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car Started")
print("\nQ8")
car=Car()
car.start()

# Q9. Create an abstract class Employee with salary() implemented in Manager.
class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass
class Manager(Employee):
    def salary(self):
        print("Salary: 75000")
print("\nQ9")
m=Manager()
m.salary()

# Q10. Create a real-world example combining encapsulation and abstraction.
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass
class Bank(ATM):
    def __init__(self,balance):
        self.__balance=balance
    def withdraw(self):
        amount=500
        if amount<=self.__balance:
            self.__balance-=amount
            print("Withdraw:",amount)
            print("Balance:",self.__balance)
        else:
            print("Insufficient Balance")
print("\nQ10")
atm=Bank(5000)
atm.withdraw()
