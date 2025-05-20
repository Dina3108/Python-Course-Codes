'''
Polymorphism - Greek Word that means to 'Have many forms or faces'
poly - many
Morphe - form

   Two ways to achieve Polymorphism ( Conditions )
   1. Inheritance = An object could be created of the same type as parent class
   2. Duck typing - Object must have necessary attributes/modes
'''
from abc import ABC , abstractmethod
class Shape(ABC):
    # ABC is a class that cannot be instantiated on its own and is designed to be subclassed by other classes

    #Using the abstractmethod the method has to be compulsorily implemented by all other sub-classes of the class
    @abstractmethod
    def Area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius=radius
    
    def Area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self,radius):
        super().__init__()
        self.side=radius
    
    def Area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,base,height):
        super().__init__()
        self.base=base
        self.height=height

    def Area(self):
        return 0.5*self.base*self.height

class Pizza(Shape):
    def __init__(self,radius,topping):
        super().__init__()
        self.radius=radius
        self.topping=topping

    def Area(self):
        return 3.14*self.radius**2
    
    def topp(self):
        print(f'Pizza is topped with {self.topping}')

#We can store the classes in a list and we can call those classes through for loop
circle1=Circle(3)
Square1=Square(25)
Triangle1=Triangle(2,5)
#shapes=[circle1,Square1,Triangle1]
#we can store the object directly by calling and call in the list
shapes=[Circle(3),Square(25),Triangle(2,5)]
def calculate_Area(x):
    return x.Area()

print(calculate_Area(circle1))
#print(calculate_Area(Triangle1))
print(calculate_Area(Square1))
#Here in above Calculate Area is polymorphic because as long as the object has the Area method it will give different output for different objects

print(Pizza(8,'Maradona').Area())
Pizza(8,'Maradona').topp()