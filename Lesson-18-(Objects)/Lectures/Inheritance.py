'''
Inheritance - Allow a class to inherit and methods     from Another Class
Helps with code reusability and Extensibility
class Child(Parent)
'''
class Animal:
    def __init__(self,x):
        self.name=x
        self.is_alive=True
    def eat(self):
        #In a function that was defined inside a class will followed by the keyword(self) that denotes the object that was called and '.' and the attribute inside the object that need to be called 
        print(f'{self.name} is Eating')
    def sleep(self):
        print(f'{self.name} is Sleeping')

#Below is the Inheritance we can inherit the functions and objects from one class to another class like below
class Dog(Animal):
    #after calling from inheritance also we can define another function inside an inherited object
    def speak(self):
        print(f'{self.name} is Speaking very Good')
class Cat(Animal):
    pass
lion=Dog('lion')
print(lion.name)
lion.sleep()

#Here by calling the object that was created by Inheritance and called a function inside that class
tiger=Cat('Tiger')
tiger.eat()
#Created function inside an inherited object
lion.speak()