'''
indexing - accessing Elements of a sequence using [] (indexing operator)
syntax:
   [start:end:step]
'''
credit_number='1234-5678-9088'
#we can access the every index element of a string
print(credit_number[0])
#it will access only upto the before end element of the string
#for below it will access only upto the 4th index not to the 5th index
print(credit_number[0:5])
#without giving end number by only giving the start index number it will access all the index elements from the start index number
print(credit_number[0:])
#without giving start number by only giving the end index number it will access all the index elements upto the end index number
print(credit_number[:10])
#It will access the element from start index number then skipping by every 2 indexes
print(credit_number[3:10:2])
#if there is no start and end index number means it will access every element from 0th index by skipping 2 indexes
print(credit_number[::3])

'''
We can access the string through reverse Indexing also as last character has -1 index number then the next before one has -2 then it follows
'''
print(credit_number[-9:-5])

card_number='8707-2313-9239'
print(f'Your Card Number is XXXX-XXXX-{card_number[-4:]}')
print(card_number[::-1])