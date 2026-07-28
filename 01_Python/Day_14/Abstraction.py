# Abstraction
'''What is Abstraction?
Abstraction means showing only essential details while hiding the implementation.

Real-Life Example
When you drive a car:
You use the steering wheel.
You press the accelerator.
You don't need to know how the engine works internally.'''

# 1.Abstract Class
# An Abstract Class cannot be instantiated directly.
# It is created using the ABC module.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
# 2.Abstract Method
# An Abstract Method has no implementation in the abstract class.
# The child class must implement it.
from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Bark")
d=Dog()
d.sound()



