1. OOP (Object Oriented Programming)
- Programming paradigm that relies on the concept of classes and objects.
- In other words, it is a way to structure your code in a efficient way

Basic Example:
class Student:
    
    (constructor)
    def __init__(self, name):
        (attributes)
        self.name = name
    
    (methods)
    def greet(self):
        return f'Hello my name is {self.name}'

(Instance of the Student Class)
christian = Student('christian')

(Accessing methods inside of the Instance)
christian.greet()

2. 4 Pillars of OOP
-- Encapsulation: Binding of data and functions (attributes and methods)
-- Abstraction: Abtracting away irrelevant information (Ex: the len() function)
-- Inheritance: Allows new objects to inherit properties from existing/parent objects
-- Polymorphism: Accesses objects of different types through the same way

3. super()
-- Refers to the parent class's attributes