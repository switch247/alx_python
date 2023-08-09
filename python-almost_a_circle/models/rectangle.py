Base = __import__('base').Base

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
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

__doc__="""
this is documentation for my module
"""
