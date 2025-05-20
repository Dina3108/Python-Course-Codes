'''Type casting is the process of converting variable from one datatype into other datatype'''   
name='Dinakar'
print(type(name))
name=bool(name)
print(name)
#o/p here is True becuase it stores the True Value

age=20
print(type(age))
#By Typecasting
age=str(age)
print(type(age))
age+='1'
print(age)
'''Here It is not doing Math Addition it is Doing String Concatenation'''
age=float(age)
print(type(age))
print(age)

gpa=9.05
print(type(gpa))
gpa=str(gpa)
print(type(gpa))

is_student=True
print(type(is_student))
is_student=str(is_student)
print(type(is_student))