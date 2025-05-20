foods=[]
prices=[]
total=0

while True:
    food=input('Enter a food to buy ( q to quit):')
    if food.lower()=='q':
        #this food.lower will convert the uppercase 'Q' into lowercase
        break
    else:
        price=float(input(f'Enter the price for your {food} :'))
        foods.append(food)
        prices.append(price)
print('Your Ordered Foods are:\n')
for x in foods:
    print(x,end='\n')
sum=0
for x in prices:
    sum+=x
print(f'Your Total Purchased Price : {sum}')