from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ initializer"""
        self.size=size
        super().__init__(self.size, self.size, x, y, id)
    @property
    def size(self):
        return self._width

    @size.setter
    def size(self, value):
        if not isinstance(value,int):
            raise TypeError('width must be an integer')
        if value<=0:
            raise ValueError('width must be > 0')
        self._width = value
        if not isinstance(value,int):
            raise TypeError('height must be an integer')
        if value<=0:
            raise ValueError('height must be > 0')
        self._height = value


    def __str__(self):
        "str method"
        return f"[{__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"
    __doc__="""doc for class"""
__doc__="""doc for module"""

if __name__ == "__main__":
    r= Square(4)
    # print(r)
    r.display()