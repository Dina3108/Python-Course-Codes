import random

low_num=1
high_num=100
ans=random.randint(low_num,high_num)

guesses=0
is_running=True

print('----Python Word Guessing Game-----')
print(f'Select a number between {low_num} and {high_num}')

while is_running:
    guess_num=input('Enter your Guess (Q/q to quit):')
    
    if guess_num.lower()=='q':
        is_running=False
        print('Thank You...!!!')
        break
    elif guess_num.isdigit():
        guesses+=1
        guess_num=int(guess_num)

        if guess_num<0 or guess_num>100:
            print('The Number is out of range..!')
        elif guess_num>ans:
            print('INCORRECT..!')
            print('Too High')

        elif guess_num<ans:
            print('INCORRECT..!')
            print('Too Low')

        elif guess_num==ans:
            print('\n--------------\n')
            print(f'CORRECT..!\nThe Answer is : {ans}')
            print(f'Number of Guesses: {guesses}')