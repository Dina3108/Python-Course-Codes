'''
super() = Function used in a child class to call methods from a parent class
          Allows you to extend the functionality of the inherited methods 
'''
class Shape():
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
    
    def describe(self):
        print(f'It is {self.color} colured')

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        #if you want to add another new attribute to a class means you have to inherit the attributes from the parent class first
        super().__init__(color,is_filled)
        self.radius=radius
    
    def describe(self):
        print(f'Area of the Circle is {3.14*self.radius**2}' )
        #by using super function we can inherit and call the function from parent class
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled,width):
        #like below using the super function we can inherit the attributes from the parent class
        super().__init__(color, is_filled)
        self.width=width
    def colors(self):
        print(f'{self.color} is filled')

class Triangle(Square):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled,width)
        self.width=width
        self.height=height
    
    def colors(self):
        print(f'Triangle is {self.color}')
        #By below we can see that by using super function we can import the methods(functions) from the parent class
        super().colors()

sq1=Square('red',True,43)
sq1.colors()
Circle1=Circle('blue',True,90)
print(Circle1.radius)
Triangle1=Triangle('Green',False,800,900)
print(Triangle1.height)
#Function calling inherited by Super Function
Triangle1.colors()
sq1.describe()
Circle1.describe()
Triangle1.describe()
