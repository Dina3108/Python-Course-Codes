'''
2D list - is list that contains multiple lists
'''
fruits=['apple','orange','banana','coconut']
vegetables=['carrot','beans','onion','tomato']
meats=['mutton','chicken','fish','prawn']

#2D-list
groceries=[fruits,vegetables,meats]
print(groceries)
#This will access the first list of 2D list
#which denotes like the first row of the matrix
print(groceries[0])
#this will access the 2nd element in the first row
print(groceries[0][1])
#this will access the 3rd element in the second row
print(groceries[1][2])

#in 2D lists you can't access the out of range Elements

'''
Printing the Elements like Matrix
'''
for x in groceries:
    #this will access every list
    for y in x:
        #this will access every element in the list,list that was accessed from the before loop
        print(y,end =' ')
    print()    

#Matrix Addition
a=[[1,2,1],[1,3,1],[1,4,1]]
b=[[1,1,1],[1,1,1],[1,1,1]]
list1=[]
list2=[]
list3=[]
for x in a:
        for z in x :
            for y in b:
                for k in y:
                    if len(list1)<=2:
                     list1.append(z+k)
                    elif len(list2)<=2:
                      list2.append(z+k)
                    elif len(list3)<=2:
                      list3.append(z+k)

c=[]
c.append(list1)
c.append(list2)
c.append(list3)
for x in c:
  for y in x:
      print(y,end =' ')
  print()

for x in c:
    print(x,end ='\n')