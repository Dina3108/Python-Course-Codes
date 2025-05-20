'''
Nested Loop - A Loop within Another Loop(outer,inner)
              outerloop:
                 inner loop:
'''
for y in range(5):
 for x in range(1,10):
    print(x,end='')
    '''
    this end operator will add at the end of a string
    while sep=' ' sep-seperator operator will add between the value by seperating the values
    '''
 print()   #This Empty print statement will print a blank print statement on the next Line

#Going to print a Rectangle
rows=int(input('Enter the no of Rows:'))
columns=int(input('Enter the no of columns:'))
symbol=input('Enter the symbol You like to Print:')
for r in range(rows):
  for c in range(columns):
    print(symbol,end='')
  print('')