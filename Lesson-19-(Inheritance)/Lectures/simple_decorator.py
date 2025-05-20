'''
Decorator - It is a function that takes another function (or a class) as input , extends or modifies its behaviour, and returns the enhanced function

Conditions for creating Decorator function:
  1.A decorator must accept a callable as its input argument
  2.A decorator must return another callable function
'''
def lover(func):
    def lover_name(): 
        print('My lover name is')
        func()
        print('She is very Beautiful')
    return lover_name

'''
Below is the way usual way to call a function like a decorator when it returns another callable function
z=lover(lover_name_input)
z()
'''

'''
But using the keyword of @-followed by name of decorator function
after above,call your normal function , decorator will decorate and return your decorated output but it don't modifies your base function
'''
@lover
def lover_name_input():
    print('Shri Harini')
lover_name_input()

@lover
def animal_name_input():
    print('Dog')
animal_name_input()

#while using decorator what if we pass arguments, so when we pass positional arguments we have to use args keyword in the return callable and input callable function , and when we pass keyword arguments we have to use kwargs
#so the args will store the arguments in tuple as order and will unpack it
#so the kwargs will store keyword arguments with key and values in dictionary and will open and use it

def logging(func):
    def wrapper(*args):
        print('Started logging')
        func(*args)
        print('Ended logging')
    return wrapper

@logging
def add(a,b):
    print('Addition is :',a+b)

@logging
def sub(a,b):
    print('Subtraction is :',a-b)
add(10,9)
sub(10,9)