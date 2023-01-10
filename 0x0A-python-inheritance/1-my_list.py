#!/usr/bin/python3
"""
Defines  MyList class
"""


class MyList(list):
    """
    list subclass
    """

    def print_sorted(self):
        """
        prints the list sorted (ascending sort)
        """
        print(sorted(self))
