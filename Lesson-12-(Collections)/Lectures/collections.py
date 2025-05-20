'''
Collection - single 'variable' used to store multiple values

List - [] ordered and changable. Duplicates Ok
Set - {}  unordered and immutable .but we can Add/ Remove elements. No duplicates
Tupple - () ordered and unchangeable. Duplicates OK. FATSER in Efficiency in Accessing Elements
'''
fruits=['apple','orange','banana','coconut']
print(fruits)
#we can access every index of the List
#but can't access the element index which is not present in the List
print(fruits[2])
#We can access elements like we use in string indexing
print(fruits[::-1])

for x in fruits:
    print(x)
    #This loop variable will access every element in a sequence

#dir function will gives all the function that was under that specific datatype/object/sequence
print(dir(fruits))
#help function will explain about that every function
#print(help(fruits))
print(len(fruits))
print('apple' in fruits)
print('pineapple' in fruits)
fruits[0]='pineapple'
print('pineapple' in fruits)
fruits.append('Peach')
print(fruits)
fruits.remove('Peach')
fruits.insert(0,'Apple')
print(fruits)
fruits.sort()
#It will sort as a list in ascending order or in Alphabetic Order
fruits.reverse()
#fruits.clear()
print(fruits.index('Apple'))
fruits.append('apple')
print(fruits.count('Apple'))
#It will count and give you the no of elements in the list

fruits_2={'apple','banana','mango'}
print(len(fruits_2))
'''
The below will don't work because we can't access the elements in the set
'''
#print(fruits_2[0])
fruits_2.add('Milk')
#but we can add or remove elements from the set
print(fruits_2)
fruits_2.remove('Milk')
print(fruits_2)

fruits_3=('apple','banana','peach','apple')
#in tupple we can't change order like below
#print(fruits_3.sort())
print(fruits_3.index('apple'))
print(fruits_3.count('apple'))