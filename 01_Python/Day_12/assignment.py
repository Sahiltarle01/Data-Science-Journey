# Python Day 12 Assignment
# Q1. Create a class Student and create one object.
class Student:
    pass
s1=Student()
print("Q1:",s1)

# Q2. Create a class Employee with name and salary.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
e=Employee("Sahil",50000)
print("\nQ2")
print("Name:",e.name)
print("Salary:",e.salary)

# Q3. Create a class Car with brand and price.
class Car:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
print("\nQ3")
c=Car("Toyota",1200000)
c.display()

# Q4. Create two objects of the same class and print their details.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)
print("\nQ4")
p1=Person("Sahil",20)
p2=Person("Rahul",21)
p1.display()
p2.display()

# Q5. Create a class Book with title and author.
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
print("\nQ5")
b=Book("Python Programming","Guido van Rossum")
b.display()

# Q6. Create a class Mobile with brand, model and price.
class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Price:",self.price)
print("\nQ6")
m=Mobile("Samsung","S24",75000)
m.display()

# Q7. Create a class Circle to calculate the area.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
print("\nQ7")
c=Circle(5)
print("Area:",c.area())

# Q8. Create a class Rectangle to calculate the area.
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
print("\nQ8")
r=Rectangle(10,5)
print("Area:",r.area())

# Q9. Create a BankAccount class with Deposit, Withdraw and Display Balance methods.
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("Insufficient Balance")
    def display(self):
        print("Balance:",self.balance)
print("\nQ9")
acc=BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()

# Q10. Create a Student class with Name, Roll Number and Marks. Create 3 objects.
class StudentDetails:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.roll)
        print("Marks:",self.marks)
print("\nQ10")
s1=StudentDetails("Sahil",1,90)
s2=StudentDetails("Rahul",2,85)
s3=StudentDetails("Amit",3,88)
s1.display()
s2.display()
s3.display()