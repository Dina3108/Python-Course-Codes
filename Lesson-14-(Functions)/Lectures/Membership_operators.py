'''
Membership Operators - used to test whether a value or variable is found in a sequence
(string, list , tupple , set , dictionary)
1.in
2. not in
'''

#Word guessing Game
word='Shri Harini'
running=True
while running:
    guess=input('Guess a letter in a Secret Word(Q/q to Quit):')
    if guess.lower()=='q':
        print('Bye Better Luck Next Time...!')
        break
    elif guess in word:
        print('You are Correct')
        print('Bye...!')
        running=False
        
    else:
        print('INCORRECT...!!!')

students={'Aadhi','Darshan','Deva'}
guess=input('Enter the Student Name :')
if guess not in students:
    print(f'{guess} is not Found')
else:
    print(f'{guess} is a Student')


#We can use mmembership operator in dictionary also
marks={'Dinakar':90,'Harinii..!!!':105,'Parkavi':89}
for x in marks:
    #like indexing the key in the dictionary also will give you the value
    print(f'{x} : {marks[x]}')

email='dinakarsri111gmail.com'
if '@' in email and '.' in email:
    print('Valid Email')
else:
    print('Invalid Mail ID')