weight=float(input('Enter Your Weight:'))
unit=input('Enter the Unit you Entered (K- kg)/(L - Lbs):')
if unit=='K':
    weight*=2.205
    print(f'Your Weight is : {weight}lbs')
elif unit=='L':
    weight/=2.205
    print(f'Your Weight is : {weight}kgs') 
else:
    print(f'{unit} is Invalid Unit')   