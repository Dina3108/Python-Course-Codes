'''
Property -It is a Decorator used to define a method as a property (it can be accessed like an attribute)
         Benifit : Add additional logic when read, write , or delete attributes
         Gives you getter , setter , and deleter method
'''
class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height

    def __str__(self):
        return f'Rectangle with dimnesions of {self._width} * {self._height}'
    
#Using property attribute we can define a method as attribute
    @property
    def width(self):
        return f'{self._width:.1f}cm'
    
    @property
    def height(self):
        return f'{self._height:.1f}cm'
    
    #using setter method in property attribute we can directly modify the base solution variable
    @width.setter
    def width(self,new_width):
        if new_width>0:
            self._width=new_width
        else:
            print('Width must be greater than Zero')

    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print('Height must be greater than Zero')

    #using deletor method we can delete an attribute from base object 
    @width.deleter
    def width(self):
        del self._width
        print('Width has been deleted')

    @height.deleter
    def height(self):
        del self._height
        print('Height has been deleted')
    
Rectangle1=Rectangle(10,5)
print(Rectangle1)
#As it is a property attribute we are defining a value into a variable
Rectangle1.width=0
Rectangle1.height=25
print(Rectangle1)

#By using the del keyword like below we can delete an attribute from a class
del Rectangle1.width
del Rectangle1.height

