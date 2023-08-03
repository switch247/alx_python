#!/usr/bin/python3
'''Inherits from'''


def inherits_from(obj, a_class):
    """returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class; otherwise False"""

    return issubclass(type(obj), a_class) and type(obj) != a_class


__doc__ = """
this is documentation for my module
"""
