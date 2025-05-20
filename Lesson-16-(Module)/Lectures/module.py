'''
module - a file containing code you want to include in your program
use 'import'  to include a module (built-in on your own)
useful to break up a large program reusable seperate files
'''
#using as keyword we can import and name the module as per our convenience

#import math as m
#print(m.pi)

#like below we can import seperate function from a module
from math import e
#As we are only importing the exponential function no need of math. module keyword
print(e)
#in below orderly variables get assigned to orderly values
'''
In below e has been modified as 5 so it can't take the exponential value from the library
a,b,c,d,e=1,2,3,4,5
print(e**a)
print(e**d)
'''
a,b,c,d=1,2,3,4
print(e**a)
print(e**d)
