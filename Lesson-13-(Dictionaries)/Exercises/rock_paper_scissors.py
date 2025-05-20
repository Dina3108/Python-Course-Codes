import random

options=('rock','paper','scissors')
computer=random.choice(options)

running = True

while running:
    player=input('Enter a choice (rock , paper, scissors):')

    while player not in options:
        print('---Enter Valid Options---')
        player=input('Enter a choice (rock, paper, scissors):')
    print(f'Player : {player}')
    print(f'Computer : {computer}')

    if player==computer:
        print('Its Tie....!!!')
    elif (player=='rock' and computer=='scissors') or (player=='scissors' and computer=='paper') or (player=='paper' and computer=='rock'):
        print('You Win...!!!')
    else:
        print('You Lost...!!\nBetter Luck Next Time...!!!')

    play_again=input('Want to Play Again(Yes/No):')
    if play_again.capitalize()=='Yes':
            running=True
    else:
            print('Thank you..!!!')
            running=False