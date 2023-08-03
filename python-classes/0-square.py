#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size

    def area(self):
        print(Square.area.__doc__)
        return self.__size ** 2
    __doc__ = """
    this is documentation for my class
    """


__doc__ = """
this is documentation for my module
"""
