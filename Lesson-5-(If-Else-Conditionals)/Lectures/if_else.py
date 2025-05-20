'''
if- Works some code only If-condition is True
Else - works some code when the condition is False
'''
age=int(input('Enter your Age:'))
if age>=100:
    print('You are too older to sign up')
elif age>=18:
    print('You are now signed up!')
elif age<0:
    print('You Have not borm yet...!')
else:
     print('You must be 18+ to Sign Up')

response=input('Would you like food? (Y/N):')
if response=='Y':
    print('Have some food !')
else :
    print('No food for you..!')

online=True
# If variable is True no need of condition it will execute only if the value stored is true
if not online:
    print('Abhishek in Online')
else:
    print('Abhishek in Offline')

op=input('enter the operator')
a=float(input('a'))
b=float(input("b"))
if op=="+":
    print(a+b)
elif op=='-':
    print(a-b)
elif op=="*":
    print(a*b)
else:
    print(a%b)

