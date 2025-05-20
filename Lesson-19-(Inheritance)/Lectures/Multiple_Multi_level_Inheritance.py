'''
Multiple Inheritance - inherit from more than one parent class
Multilevel Inheritance - inherit from a parent which inherits from another parent
'''
class Animal:
    def eat(self):
        print('Animal is Eating')
    def sleep(self):
        print('Animal is Sleeping')

    def __init__(self,x):
        self.name=x

class Prey(Animal):
    #As below is an instance method we have to use the self keyword as an argument
    def flee(self):
        print(f'{self.name} is fleeing')
class Predator(Animal):
    #by using the static method and also it's keyword we can call a function without using self keyword and also without using any attributes of that class
    @staticmethod
    #static method can also be called without declaring the __init__ constructor/instance function
    #As below is using static method we can't use any self and its attributes
    def hunt():
        print('This animal is Hunting')

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass


p=Prey('P')
#Below is known as Multilevel Inheritance it gets inherited from its parent that was also inherited from another parent
p.eat()
p.flee()
q=Predator('q')
q.hunt()

rabbit=Rabbit('rabbit')
rabbit.flee()

#Below is known as Multiple inheritnace it can get inherited from 2/>2 classes also
fis=Fish('Fish')
fis.hunt()
fis.flee()
fis.sleep()
