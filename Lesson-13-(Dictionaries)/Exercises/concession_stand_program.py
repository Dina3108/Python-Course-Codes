menu={
'pizza':3.00,'nachos':4.50,'popcorn':6.00,'fries':2.50,'chips':1.00,'pretzel':3.50,'soda':3.00,'lemonade':4.25
}
print('-----MENU------')
for x,y in menu.items():
    print(f'{x:10}:{y:.2f}')
print('-----------------')

cart=[]
total=0

while True:
    food=input('Select an Item from the Menu (Q/q to Quit):').lower()
    #we can give lower on above and make it input as lowercase
    if food=='q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
    
print('Items you have Selected:')
print(cart)

for x in cart:
    total+=menu.get(x)

print(f'Your total bill Price : {total:.2f}')