from models.base import Base
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
        if not isinstance(width,int):
            raise TypeError('width must be an integer')
        if width<=0:
            raise ValueError('width must be > 0')
        self.__width = width
        if not isinstance(height,int):
            raise TypeError('height must be an integer')
        if height<=0:
            raise ValueError('height must be > 0')
        self.__height = height

        if not isinstance(x,int):
            raise TypeError('x must be an integer')
        if x<0:
            raise ValueError('x must be >= 0')
        self.__x = x
        if not isinstance(y,int):
            raise TypeError('y must be an integer')
        if y<0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width attribute."""
        if not isinstance(value,int):
            raise TypeError('width must be an integer')
        if value<=0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height attribute."""
        if not isinstance(value,int):
            raise TypeError('height must be an integer')
        if value<=0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x attribute."""
        if not isinstance(value,int):
            raise TypeError('x must be an integer')
        if value<0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y attribute."""
        if not isinstance(value,int):
            raise TypeError('y must be an integer')
        if value<0:
            raise ValueError('y must be >= 0')
        self.__y = value
    def area(self):
        """
        The function calculates the area of a rectangle.
        :return: The area of the rectangle, which is calculated by multiplying the height and width of
        the rectangle.
        """
        return self.height * self.width
    def display(self):
        """displays the rectangle using width and height"""
        for y in range(self.y):print()
        for i in range( self.height):
            print(' '*self.x,end='')
            for j in range(self.width):
                print("#",end='')
            print()
    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute: id, width, height, x, y"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']


        
    def __str__(self):
        "str method"
        return f"[{__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    __doc__="""doc for class"""
__doc__="""doc for module"""

if __name__ == "__main__":
    r= Rectangle(4,2)
    print(r)
    r.display()