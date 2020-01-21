=============================
The ``7-base_geometry`` module
=============================

Using ``BaseGeometry``
---------------------

Import the function:

>>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
    >>> bg = BaseGeometry()
    >>> type(bg)
    <class '7-base_geometry.BaseGeometry'>

If "Value" is a valid integer, function does nothing: 

>>> bg.integer_validator("name", 5)


-----
If "Value" is not an integer, it raise an TypeError:

>>> bg.integer_validator("Invalid Value", "Not a integer")
Traceback (most recent call last):
TypeError: Invalid Value must be an integer

>>> bg.integer_validator("Invalid Value", 1.0)
Traceback (most recent call last):
TypeError: Invalid Value must be an integer

>>> bg.integer_validator("Invalid Value", True)
Traceback (most recent call last):
TypeError: Invalid Value must be an integer

>>> bg.integer_validator("Invalid Value", (1, ))
Traceback (most recent call last):
TypeError: Invalid Value must be an integer

>>> bg.integer_validator("Invalid Value", [10])
Traceback (most recent call last):
TypeError: Invalid Value must be an integer

>>> bg.integer_validator("Invalid Value", {1, 7})
Traceback (most recent call last):
TypeError: Invalid Value must be an integer

>>> bg.integer_validator("Invalid Value", None)
Traceback (most recent call last):
TypeError: Invalid Value must be an integer

-----
If "Value" is less or equals to 0, it raise an ValueError:

>>> bg.integer_validator("Invalid Value", -100)
Traceback (most recent call last):
ValueError: Invalid Value must be greater than 0

>>> bg.integer_validator("Invalid Value", 0)
Traceback (most recent call last):
ValueError: Invalid Value must be greater than 0

-----
Also, Both parameters must be provided, otherwise and TypeError is raised:

>>> bg.integer_validator("hi")
Traceback (most recent call last):
TypeError: integer_validator() missing 1 required positional argument: 'value'

>>> bg.integer_validator()
Traceback (most recent call last):
TypeError: integer_validator() missing 2 required positional arguments: 'name' and 'value'
