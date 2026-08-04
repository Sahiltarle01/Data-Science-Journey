# Python Day 13 Assignment
# Q1. Create a parent class Animal and a child class Dog. Call the parent method.
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    pass
print("Q1")
d=Dog()
d.sound()

# Q2. Create a parent class Vehicle and child class Car.
class Vehicle:
    def start(self):
        print("Vehicle Started")
class Car(Vehicle):
    pass
print("\nQ2")
c=Car()
c.start()

# Q3. Demonstrate Single Inheritance.
class Parent:
    def display(self):
        print("Parent Class")
class Child(Parent):
    pass
print("\nQ3")
ch=Child()
ch.display()

# Q4. Demonstrate Multiple Inheritance.
class Father:
    def father(self):
        print("Father Method")
class Mother:
    def mother(self):
        print("Mother Method")
class Child(Father,Mother):
    pass
print("\nQ4")
c=Child()
c.father()
c.mother()

# Q5. Demonstrate Multilevel Inheritance.
class GrandFather:
    def show(self):
        print("Grand Father")
class Father(GrandFather):
    pass
class Son(Father):
    pass
print("\nQ5")
s=Son()
s.show()

# Q6. Demonstrate Hierarchical Inheritance.
class Parent:
    def display(self):
        print("Parent Class")
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print("\nQ6")
c1=Child1()
c2=Child2()
c1.display()
c2.display()

# Q7. Create a program showing Method Overriding.
class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
print("\nQ7")
d=Dog()
d.sound()

# Q8. Use super() to call the parent constructor.
class Person:
    def __init__(self,name):
        self.name=name
class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
print("\nQ8")
s=Student("Sahil",1)
print("Name:",s.name)
print("Roll:",s.roll)

# Q9. Create two child classes and demonstrate Polymorphism.
class Bird:
    def sound(self):
        print("Bird Sound")
class Sparrow(Bird):
    def sound(self):
        print("Chirp")
class Crow(Bird):
    def sound(self):
        print("Caw")
print("\nQ9")
b1=Sparrow()
b2=Crow()
b1.sound()
b2.sound()

# Q10. Create a real-world example using Person and Student.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,branch):
        super().__init__(name,age)
        self.branch=branch
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Branch:",self.branch)
print("\nQ10")
st=Student("Sahil",20,"AI & Data Science")
st.display()
