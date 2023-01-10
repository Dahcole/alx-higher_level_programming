#!/usr/bin/python3
"""
Defines Square class sublass of "Rectangle" subclass of "Basegeometry"
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """Initializes Square's side size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """returns the square's description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
