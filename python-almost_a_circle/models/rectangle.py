# Base = __import__('base').Base
from models.base import Base

# The Rectangle class is a subclass of the Base class and represents a rectangle with width, height,
# and position attributes.
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The function is a constructor for a class that initializes the width, height, x and y
        attributes.
        
        :param width: The width parameter represents the width of an object. It is used to define the
        width of an object in a class or function
        :param height: The `height` parameter represents the height of an object. It is used to set the
        height of the object when it is initialized
        :param x: The x-coordinate of the top-left corner of the object's bounding box. It represents
        the horizontal position of the object on a 2D plane, defaults to 0 (optional)
        :param y: The `y` parameter represents the y-coordinate of the object's position. It determines
        the vertical position of the object on a coordinate plane, defaults to 0 (optional)
        :param id: The `id` parameter is used to assign a unique identifier to an instance of the class.
        It is an optional parameter and if not provided, it will be set to `None`
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """
        The function `get_width` returns the value of the private attribute `__width`.
        :return: The width of the object.
        """
        return self.__width

    """
    The function sets the width attribute of an object to a specified value.
    
    :param width: The "width" parameter is the value that will be assigned to the private attribute
    "__width" of the object
    """
    def set_width(self, width):
        """
        The function sets the width attribute of an object.
        
        :param width: The "width" parameter is the value that will be assigned to the private attribute
        "__width" of the object
        """
        self.__width = width

    def get_height(self):
        """
        The function "get_height" returns the height of an object.
        :return: The height of the object.
        """
        return self.__height

    def set_height(self, height):
        """
        The function sets the height attribute of an object.
        
        :param height: The height parameter is the value that will be assigned to the private attribute
        __height
        """
        self.__height = height

    def get_x(self):
        """
        The function `get_x` returns the value of the private variable `__x`.
        :return: The method `get_x` is returning the value of the private variable `__x`.
        """
        return self.__x

    def set_x(self, x):
        """
        The function sets the value of the private variable __x to the given parameter x.
        
        :param x: The parameter "x" is a value that will be assigned to the private attribute "__x" of the
        object
        """
        self.__x = x

    def get_y(self):
        """
        The function returns the value of the private variable __y.
        :return: The method `get_y` is returning the value of the private attribute `__y`.
        """
        return self.__y

    def set_y(self, y):
        """
        The function sets the value of the private variable __y.
        
        :param y: The parameter "y" is the value that will be assigned to the private attribute "__y"
        """
        self.__y = y
    __doc__="""
this is documentation for my class
"""

__doc__="""
this is documentation for my module
"""
