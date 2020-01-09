# 0x06. Python - Classes and Objects

## Description

Learning Objectives
* Why Python programming is awesome (dont forget to tweet today, with the hashtag #pythoniscool :))
* What is OOP
* first-class everything
* What is a class
* What is an object and an instance
* What is the difference between a class and an object or instance
* What is an attribute
* What are and how to use public, protected and private attributes
* What is self
* What is a method
* What is the special __init__ method and how to use it
* What is Data Abstraction, Data Encapsulation, and Information Hiding
* What is a property
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

---

### [0. My first square](./0-square.py)
* An empty class Square that defines a square.

### [1. Square with size](./1-square.py)
* A class Square that defines a square by: (based on 0-square.py)

* Private instance attribute: size
* Instantiation with size (no type/value verification)

### [2. Size validation](./2-square.py)
* A class Square that defines a square by: (based on 1-square.py)
* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0

### [3. Area of a square](./3-square.py)
* A class Square that defines a square by: (based on 2-square.py)

* Private instance attribute: size
* Instantiation with optional size: def __init__(self, size=0):
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Public instance method: def area(self): that returns the current square area

### [4. Access and update private attribute](./4-square.py)
* A class Square that defines a square by: (based on 3-square.py)

* Private instance attribute: size:
* property def size(self): to retrieve it
* property setter def size(self, value): to set it:
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area

### [5. Printing a square](./5-square.py)
* A class Square that defines a square by: (based on 4-square.py)

* Private instance attribute: size:
* property def size(self): to retrieve it
* property setter def size(self, value): to set it:
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Instantiation with optional size: def __init__(self, size=0):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
* if size is equal to 0, print an empty line
* You are not allowed to import any module

### [6. Coordinates of a square](./6-square.py)
* A class Square that defines a square by: (based on 5-square.py)

* Private instance attribute: size:
* property def size(self): to retrieve it
* property setter def size(self, value): to set it:
* size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
* if size is less than 0, raise a ValueError exception with the message size must be >= 0
* Private instance attribute: position:
* property def position(self): to retrieve it
* property setter def position(self, value): to set it:
* position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers
* Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
* Public instance method: def area(self): that returns the current square area
* Public instance method: def my_print(self): that prints in stdout the square with the character #:
* if size is equal to 0, print an empty line
* position should be use by using space - Dont fill lines by spaces when position[1] > 0

## Author
* **Juan Portilla** - [jdpa352](https://github.com/Jdpa357)