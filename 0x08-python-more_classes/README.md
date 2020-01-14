# 0x08. Python - More Classes and Objects

## Description

Learning Objectives
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
* What are the special __str__ and __repr__ methods and how to use them
* What is the difference between __str__ and __repr__
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

### [0. Simple rectangle](./0-rectangle.py)
* An empty class Rectangle that defines a rectangle:

### [1. Real definition of a rectangle](./1-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

### [2. Area and Perimeter](./2-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

### [3. String representation](./3-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

### [4. Eval is magic](./4-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 3-rectangle.py)

### [5. Detect instance deletion](./5-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 4-rectangle.py)

### [6. How many instances](./6-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 5-rectangle.py)

### [7. Change representation](./7-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 6-rectangle.py)

### [8. Compare rectangles](./8-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 7-rectangle.py)

### [9. A square is a rectangle](./9-rectangle.py)
* A class Rectangle that defines a rectangle by: (based on 8-rectangle.py)

### Class summary:
* Private instance attribute: width:
* property def width(self): to retrieve it
* property setter def width(self, value): to set it:

* Private instance attribute: height:
* property def height(self): to retrieve it
* property setter def height(self, value): to set it:

* Public class attribute number_of_instances:
* Incremented during each new instance instantiation
* Decremented during each instance deletion

* Public class attribute print_symbol:
* Used as symbol for string representation
* Can be any type

* Instantiation with optional width and height: def __init__(self, width=0, height=0):
* Public instance method: def area(self): that returns the rectangle area
* Public instance method: def perimeter(self): that returns the rectangle perimeter:

* print() and str() should print the rectangle with the character #

* repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()

* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

* Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
* rect_1 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_1 must be an instance of Rectangle
* rect_2 must be an instance of Rectangle, otherwise raise a TypeError exception with the message rect_2 must be an instance of Rectangle
* Returns rect_1 if both have the same area value

* Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size

## Author
* **Juan Portilla** - [jdpa352](https://github.com/Jdpa357)