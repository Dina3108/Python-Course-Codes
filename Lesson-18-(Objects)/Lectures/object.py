'''
Object - A bundle of related attributes (variables) and methods (functions)
      Attributes denotes the properties of an object and functions denotes its activities of the object
      Ex: phone,cup,book
      You need class to create many objects
class = used to design the structure and layout of an object
'''
from Car_module import Car
car1=Car('Tata',1999,'Black',True)
print(car1)    
#It will print you the memory address of car object 
print(car1.model)
#using the dot(.) we can access the attributes of the object
car2=Car('BMW',2019,'Blue',False)
print(car2.for_sale)
car2.drive()
car1.drive()
car2.describe()

'''
class variables - Shared among all instances of a class
                  Defined outside the construtor
                  Allow you to share data among all objects created from that class
'''
class Student:
    #by using the class variables like below it will be same and can be used for all the objects inside that class
    class_year=2022
    #You can do operations using the class variable defined outside and doing its operations inside the function
    num_students=0
    def __init__(self,x,y,z):
        self.name=x
        self.age=y
        self.marks=z
        #While doing operations using the class variable we have to use the class name as keyword inside constructor
        Student.num_students+=1
        #Here name,age,marks all are attributes of that object

#we are creating an object named Student 1 by passing the values as argument through the Student object by assigning those into a variable
student1=Student('Harini',17,100)
student2=Student('Dinakar',17,50)
#Calling the attribute of that object using dot
print(student1.name)
print(student2.marks)
#calling a class variable like below will be same for all the objects inside that class
print(student1.class_year)
print(student2.class_year)
print(student2.num_students)

student3=Student('Darshan',18,75)
student4=Student('Deva',18,64)
print(student4.num_students)
#using the object attributes using inside the formatting string
print(f'My class Graduating at {Student.class_year} has {Student.num_students} Students')
#In above we are calling the class variables that was defined out of an object and get motified inside every object