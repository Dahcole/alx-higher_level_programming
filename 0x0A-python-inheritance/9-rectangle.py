#!/usr/bin/python3
"""
Defines "Rectangle" class subclass of "Basegeometry"
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """Initializes a Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
