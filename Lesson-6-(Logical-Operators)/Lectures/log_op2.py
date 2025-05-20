'''
conditional expression- A one-line shortcut for the if-else statement (ternary operator)
                        Print or assign one of two values based on a condition
                        syntax:
                        X if condition else Y
'''
num=8
print('Positive' if num>0 else 'Negative')
print('Even' if num%2==0 else 'Odd')
a=2
b=5
max_num= a if a>b else b
print(max_num)
min_num= a if a<b else b
print(min_num)
user_role='Guest'
acess='Full Access' if user_role=='Admin' else 'Limited Access'
print(acess)

x=10
print('Greater than 20' if x>20 else 'less than 20')