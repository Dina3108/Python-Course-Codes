'''
Function - A block of reusable Code
         place () after the function name to invoke it
'''
def happy_birthday(name,age):
    print(f'Happy Birthday {name}...!')
    print(f'You are {age} Years Old')

happy_birthday('Dinakar',20)

'''
return - statement used to end a function
        and send a result back to the caller
'''
def add(a,b):
    return a+b
print(add(1,4))

'''
return - statement used to end a function
         and send a result back to the caller
'''
def create_name(first_name,last_name):
    return first_name.capitalize()+' '+last_name.capitalize()
print(create_name('Dinakar','shanmugasundaram'))

'''
4 types of Arguments:

1.Positional-In positional Arguments we have to pass the arguments in a positional order
2.Default-a default value for certain parameters,
          default is used when that argument is omitted,
          make your function more flexible, reduces no of arguments passed
3.keyword argument - an argument preceeded by an Identifier
                    helps with readability
                    order of arguments does not matter
4.arbitary argument - passing arguments using *args and **kwargs keywords
'''

def net_price(list_price,discount,tax):
    return list_price*(1-discount)*(1+tax)

#for below as it is a positional arguments we have to pass all the arguments without changing the positional order ,if we change the order means, values will mismatch 
print(net_price(500,0.2,0.1))

#below default argument inside the function bracket will show error because positional argument always has to follow keyword arguments it is same for in calling the function also
# def net_price(list_price,discount=0.2,tax):
 #   return list_price*(1-discount)*(1+tax)

def net_price(list_price,discount,tax=0.1):
    return list_price*(1-discount)*(1+tax)

print(net_price(500,0.2))
#we can change the default argument also by passing the argument in the correct position of the declared default argument
print(net_price(500,0.2,0.2))

#use-case of default argument
import time 

def stop_watch(start,end):
    for x in range(end,start,-1):
        #below end and also sep is an example of key word argument
        print(x,end='\n')
        time.sleep(1)
    print('Time Up...!!!')

#stop_watch(0,10)

#use-case of keyword argument
#stop_watch(end=20,start=10)
#like below when we are giving the argument with keyword the order doesn't matter

def get_phone_no(country,area,first,last):
    return f'{country}-{area}-{first}-{last}'
print(get_phone_no(area='456',first='78',last='90',country='123'))

'''
1.*args- allows you to pass multiple non-key arguments
        the arguments passed using *args will be stored in a tupple and we have to access the elements from the tupple
2.**kwargs- allows you to pass multiple keyword arguments
         the arguments passed using **kwargs will be stored in a dictonary and we have to access the key and values from the dictionary
'''

def list_print(*args):
    print(args)
    print(type(args))
    for x in args:
        print(x)

list_print(1,2,3)


def name(*args):
    for x in args:
        print(x,end='\n')

name('Hi','Hariniii','Enga','Iruka...!!!')

def print_address(**kwargs):
    for x,y in kwargs.items():
        print(f'{x} : {y}',end='\n')

#In below when we pass multiple key-value arguments it will store the pairs in the dictionary and we have to access every element from the dictionary
print_address(Name='Dinakar S',Mob_no='9677559454',Age=20)


#We can pass both *args and **kwargs arguments through the function

# def shipping_label(**kwargs,*args)
#the above will cause a syntax error because args is a positional argument but kwargs is a keyword argumment positional argument doen't folllow keyword argument

def shipping_label(*args,**kwargs):
    for x in args:
        print(x,end=' ')
    for x,y in kwargs.items():
        print(f'{x} : {y}',end='\n')
    if 'dob' in kwargs.keys():
        print(kwargs.get('dob'))
    


#In the below while passing the arguments first we have to pass the positional arguments then keyword arguments
#all positional arguments are stored into tupple
#all keyword arguments are stored into dictionary
shipping_label('123','456','7890',Name='Dinakar',mob_no='9677559454',age=20,dob='01-01-2005')

