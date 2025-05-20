'''
for-loops - execute a block of code a fixed number of times
            you can iterate over a range , string , sequence
'''
for x in range(1,11):
    print(x)
print('Vanakkam da Mapla')    

for x in range(1,11,4):
    #like in string indexing it skips 4 indexes and access the elements
    print(x)

love='Shri Harini'
for l in love:
    if l==' ':
        continue
    #continue will only skip that Iteration
    print(l)
#We can access the string like above in For Loop

credit_number='4738-2932-3042'
for credit in credit_number:
    if credit=='-':
        break
    #break will come out of the Loop
    print(credit)