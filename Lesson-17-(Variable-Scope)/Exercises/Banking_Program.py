def show_balance(balance):
    print(f'Your Balance is ${balance:.2f}')
def deposit():
    amount=float(input('Enter an Amount to be deposited : '))
    if amount<0:
        print('This is not Valid Amount')
    else:
        return amount
def withdraw(balance):
    amount=float(input('Enter an Amount to Withdraw : '))
    if amount<0:
        print('Amount must be greater than Zero')
    elif amount>balance:
        print('Insufficient Funds...!')
    else:
        return amount 
def main():
    is_running=True
    balance=0
    while is_running:
        print('---Banking Program---')
        print('1.Show Balance')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.Exit')

        choice=int(input('Enter your choice (1-4):'))
        if choice==1:
            show_balance(balance)
        elif choice==2:
            balance+=deposit()
        elif choice==3:
            balance-=withdraw(balance)
        elif choice==4:
            is_running=False
        else:
            print('This is not a Valid Choice')
            
        print('Thankyou so much have a Nice Day...!')
if __name__=='__main__':
    main()