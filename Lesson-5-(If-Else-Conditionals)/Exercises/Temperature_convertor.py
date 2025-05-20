unit=input('Whether the Unit is (C/F/K):')
temp=float(input('Enter the Temperature : '))
if unit=='C':
    fahren=(9/5)*temp+32
    kelvin=temp+273.15
    print(f'Converted Temperatures :\nFahrenheit{round(fahren,3)}F\nKelvin:{round(kelvin,3)}K')
elif unit=='F':
    celcius=(5/9)*temp-32
    kelvin=celcius+273.15
    print(f'Converted Temperatures :\nCelcius:{round(celcius,3)}C\nKelvin:{round(kelvin,3)}K')
elif unit=='K':
    celcius=temp-273.15
    fahren=(9/5)*celcius+32
    print(f'Converted Temperatures :\nCelcius:{round(celcius,3)}C\nFahren:{round(fahren,3)}F')
else:
    print(f'{unit} is Invalid Unit')

