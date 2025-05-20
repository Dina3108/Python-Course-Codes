'''
List Comprehension - A concise way to create lists in Python
                     Compact and easier to read than traditional method
     syntax:    [expression for value iterable if condition]
'''
x = [ x for x in range(1,10)]
print(x)
x_double = [ x*2 for x in range(1,10)]
print(x_double)
x_square = [ x**2 for x in range(1,10)]
print(x_square)

fruits=['apple','orange','pineapple']
fruit_list=[x.upper() for x in fruits]
print(fruit_list)



fruits=['apple','orange','pineapple']
#the below x[0] denotes the 0th index value/character of the list element
fruit_list=[x[0] for x in fruits]
print(fruit_list)

pos_num=[x for x in range(-12,11) if x>=0]
print(pos_num)
neg_num=[x for x in range(-12,11) if x<0]
print(neg_num)
odd_num=[x for x in range(1,50) if x%2==0]
print(odd_num)