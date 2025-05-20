initial_balance=0
rate=0
time=0
while initial_balance<=0:
    initial_balance=float(input('Enter Initial Principle Balance of your Account:'))
    if initial_balance<=0:
        print("Iniital Principle Balance can't be less than or Equal to Zero" )
while rate<=0:
    rate=float(input('Enter the Interest Rate:'))
    if rate<=0:
        print("Rate can't be less than or Equal to Zero" )
while True:
    time=float(input('Enter the Time in Years:'))
    if time<=0:
        print("Rate can't be less than or Equal to Zero" )
    else:
        break
amount=initial_balance*pow((1+(rate/100)),time)
print(f'Balance in Your Account after {time:.0f} Years : {amount:.3f}')