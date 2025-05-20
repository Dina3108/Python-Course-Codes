'''
Validate User Input Exercise
1. Username is no more than 12 characters
2. Username must not contain any Digits
3. Username must not contain any spaces
'''
print('Conditions for Valid Username Input:\n1. Username is has to be Not more than 12 characters\n2. Username must not contain any Digits\n3. Username must not contain any spaces')
user_name=input('Enter Your Username:\n')
user_name= f'Welcome {user_name}' if len(user_name)<=12 and user_name.isalpha() and (user_name.find(' ')==-1) else 'Enter Per Valid Conditions'
print(user_name)