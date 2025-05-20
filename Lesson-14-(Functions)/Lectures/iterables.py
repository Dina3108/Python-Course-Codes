'''
Iterables - An object/collection that can return its elements one at a time, allowing it ot be iterated over in a loop

Iterables are List,set,tupple,string,dictionary
'''

numbers=[1,2,3,4,5]
#Tupple is also an interable
#numbers==(1,2,3,4,5)
for x in numbers:
    print(x)

#using the reversed function we can reverse the list
for x in reversed(numbers):
    print(x,end='-')

#set is also an iterable
fruits={'apple','orange','banana','Pineapple'}
for x in fruits:
    print(x)

#string is also an iterable
fr_name='apple'
for x in fr_name:
    print(x)

#Dictionary is also an Iterable
details= {'Name':'Shri Harini','Husband':'Dinakar ShanmugaSundaram'}
for x,y in details.items():
    print(f'{x} : {y}',end='\n')
    