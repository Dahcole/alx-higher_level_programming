#!/usr/bin/python3
"""
Defines the class MyInt
"""


class MyInt(int):
    """rebel version of an int"""
    def __eq__(self, other):
        """returns the opposite of equal(eq)"""
        return int(self) != other

    def __ne__(self, other):
        """returns the opposite of not equal(ne)"""
        return int(self) == other
