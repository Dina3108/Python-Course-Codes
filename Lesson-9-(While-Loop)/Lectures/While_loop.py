#While Loop - Execute Some Condition WHILE some condition is getting false
num=int(input('Enter a Number(Greater than zero):'))
'''
if num <=0:
    print('Invalid Number')
    num=int(input('Enter Positive Number:'))
else:
    print(f'You Entered : {number}')
'''
#while loop is almost same like if condition
#But if - condition runs only one time and checks the condition one time
# But While - Loop runs multiple times until condition is true
while num <=0:
    print('Invalid Number')
    num=int(input('Enter Positive Number:'))
else:
    print(f'You Entered : {num}')