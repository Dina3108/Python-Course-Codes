'''
Static methods - A method that belong to a class  rather than any object from that class(instance)
                Usually used for general utility functions
                Besy for utility functions that do need access to class data

Instance Methods - Best for operations instances of the class (objects)

class Methods - Allow operations related to the class  itself
                Take (cls) as the first parameter, which represents the class itself

                Best for class level data or require access to the class itself
'''
#All the methods that we used before are Instance methods

class Apple():
    #by using the static method this method will only be used in this class can't able to define in other classes
    @staticmethod
    def like():
        print('I like Apple')

#class Banana():
    # def like():
        #print('I like Banana')

Apple().like()
#Banana()

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    def get_info(self):
        return f'{self.name} and {self.position}'
    
    #This below method will only used in this class not in any another class
    @staticmethod
    def is_valid_position(position):
        postions_list=['Manager','Cashier','Cook']
        return position in postions_list
    
print(Employee('Harini','Manager').is_valid_position('Manager'))

class Student:
    count=0
    Total_gpa=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.count+=1
        Student.Total_gpa+=1

    #Instance Method
    def get_info(self):
        return f'{self.name} {self.age}'
    
    #Class method allows to do operations in the class itself using class variables
    @classmethod
    def get_count(cls):
        return f'Total Students : {cls.count}\n Total GPA : {cls.Total_gpa}'
    
    @classmethod
    def avg_cpa(cls):
        if cls.Total_gpa==0:
            return 0
        else:
         return cls.Total_gpa/cls.count
        
student1=Student('Dinakar',20)
student2=Student('Hariniii',20)

print(student1.get_info())
print(student2.get_count())
print(student2.avg_cpa())
