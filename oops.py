# Object-Oriented Programming Basics
# Classes and Objects
# Classes are blueprints for creating objects (instances). Objects bundle data and functions. This is useful in GenAI for modeling entities like datasets or models.

# Notes: Define a class with class keyword. Create objects by calling the class like a function.

# Example

class Dog:
    pass  # Placeholder for class body

my_dog = Dog()  # Create an object
print(type(my_dog))  # <class '__main__.Dog'>

# init Constructor
# The __init__ method initializes object attributes when created. It's like a setup function.

# Notes: Use self to refer to the instance. Called automatically on object creation.


class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

my_dog = Dog("Buddy", 3)
print(f"{my_dog.name} is {my_dog.age} years old")  # Buddy is 3 years old

# Instance Methods, Class Attributes
# Instance methods operate on objects (use self). Class attributes are shared across all instances.

# Notes: Methods are functions inside classes. Class attributes are defined outside methods.


class Dog:
    species = "Canine"  # Class attribute (shared)

    def __init__(self, name):
        self.name = name

    def bark(self):  # Instance method
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())  # Buddy says Woof!
print(Dog.species)  # Canine (accessible via class or instance)


# Inheritance and Method Overriding
# Inheritance lets a child class inherit from a parent. Overriding redefines a parent method in the child.

# Notes: Use super() to call parent methods. Useful in GenAI for extending base models.


class Animal:  # Parent class
    def sound(self):
        return "Some sound"

class Dog(Animal):  # Child class inherits
    def sound(self):  # Override
        return "Woof!"  # Overrides parent's sound

my_dog = Dog()
print(my_dog.sound())  # Woof!
