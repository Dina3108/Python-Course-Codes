import random
def spin_row():
    symbols=['🍌', '🍎','🍇', '🍉','🌽']
    results=[random.choice(symbols) for x in range(3)]
    return results
def print_row(row):
    print('|'.join(row))
def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍌':
            return bet*3
        elif row[0]=='🍎':
            return bet*4
        elif row[0]=='🍇':
            return bet*5
        elif row[0]=='🍉':
            return bet*10
        elif row[0]=='🌽':
            return bet*20
    return 0
def main():
    balance=100
    print('-----------------------')
    print('Welcome to Python Slots')
    print('Symbols : 🍌 🍎 🍇 🍉🌽')

    while balance>0:
        print(f'Current Balance : {balance}')
        bet=input('Place Your Bet Amount:')
        if not bet.isdigit():
            print('Please Enter a Valid number')
            continue
        bet=int(bet)
        if bet>balance:
            print('Insufficient Funds')
            continue
        elif bet<=0:
            print('Bet must br Greater than Zero')
        row=spin_row()
        print('---Spinning---')
        balance-=bet
        print_row(row)
        payout=get_payout(row,bet)
        balance+=payout
        if payout>0:
            print(f'You Won {payout}')
        else:
            print('Sorry you lost this Round...!')
        play_again=input('Do you want to Play Again (Y/N):').upper()
        if play_again!='Y':
            print('\n\-------------------\n')
            print(f'Game Over....\nYour Final Balance : {balance}')
            print('\n\-------------------\n')
            break
if __name__=='__main__':
    main()