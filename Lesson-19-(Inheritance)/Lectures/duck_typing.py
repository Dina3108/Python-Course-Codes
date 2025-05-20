'''
Duck Typing - Another way to achieve polymorphism besides Inheritance
              Object must have the minimum necessary attributes/modes
              'If it looks like a duck and quacks like a duck, it must be a duck'
'''
class Animal():
    alive=True

class Dog(Animal):
    def speak(self):
        print('Im Barking')

class Cat(Animal):
    def speak(self):
        print('Im Meowwing')

class Car(Animal):
    def speak(self):
        Animal.alive=False
        print('Im Horning')

list1=[Dog(),Cat(),Car()]
for x in list1:
     x.speak()
     print(Animal.alive)

#As car can't speak but it speaks because it is having speak method
#It shows when it has the same method in all objects it doesn't method whether it is suitable or not
