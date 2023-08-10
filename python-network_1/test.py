class Human:
    count=0
    def __init__(self,name="chala",age=0):
        """asdgadfg """
        Human.count += 1
        self.__name = name
        self.__age = age
        
    def walk(self):
        print("walking")    
        
    @classmethod
    def test(self):
        print("class method")
    
    @property
    def name(self):
        """getter for name"""
        return self.__name
    
    def set_name(self,value):
        """sddfsdf"""
        self.__name= value
    
    @property
    def age(self):
        """asdfasdfasf"""
        return self.__age
    @age.setter
    def age(self,value):
        """ asfdasdf"""
        self.__age = value
        



        __doc__ = """
    this is documentation for my class
    """
    

__doc__ = """
this is documentation for my module
"""



h1 = Human("eyob",2)
print(h1.name)
h1.walk()

h2 = Human()
print(h2.name)

h3 = Human("abel",90)
print(h3.name)

# h2.name = "new name"

h2.set_name("new name")
print(h2.name)


print(Human.count)
Human.test()



# document 
# atribute ,methods, __init__