from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super.__init__(id,size,size,x,y)
    def __str__(self):
        "str method"
        return f"[{__class__.__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"
    __doc__="""doc for class"""
__doc__="""doc for module"""
