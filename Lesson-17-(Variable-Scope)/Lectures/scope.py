'''
Variable Scope = where a variable is visible and accessible
Scope resolution= (LEGB) Local -> Enclosed -> Global -> Built-in

 Local - variable that was declared inside a particular  function that can't be used outside the function

 Enclosed - variable that was declared inside a function can be used in an another function that was declared inside that function

 Global - variable declared outside the function in the maincode that can be used in all functions

 Built-in - variable that was declared from an Imported Module
'''

#Local variable scope resolution
'''
Below Function shows Error and explains that variable 'a' declared in func1()
can't usable in func2()

variable 'b' declared in func2()
can't usable in func1()

def func1():
    a=1
    print(b)
def func2():
    b=1
    print(a)    
'''
def func1():
    a=1
    def func2():
      #here as it don't have local variable it got accessed from the enclosed variable from it's enclosed main function
      print(a)
      #If we declare below local variable means , local variable get's first prioritized
      #a=10
      #print(a)
    func2()
func1()

#Global Variable declaration
def func1():
   print(x)

def func2():
   print(x)

#By declaring the below global variable we can declare in all written function
x=2
func1()
func2()   

#Built-in Variable Declaration
from math import e
#By using the Built-in variable we can use in all the below main Codes
print(e)
#we can modify the built-in variable as global variable
def e_func():
 e=3
 print(e)
e_func()