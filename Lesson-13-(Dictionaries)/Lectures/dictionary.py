'''
dictionary : a collection of {key:value} pairs
             ordered and changeable. No duplicates
'''
capitals={
'USA':'Washington D.C',
'India':'New Delhi',
'China':'Beijing',
'Russia':'Moscow'
}
#print(dir(capitals))
#the above will give you the list of all functions usable in dictionary

#get function will get the value from the key
print(capitals.get('USA'))

if capitals.get('India')=='New Delhi':
    print('That Capital Exist')
else:
    print("That Capital doesn't Exist")

#using update function we can add new elements or edit/update the elements in the Dictionary
capitals.update({'German':'Berlin'})
capitals.update({'USA':'New York'})
print(capitals)


#pop function will remove the specific key from the dictionary
capitals.pop('China')
print(capitals)

capitals.update({'Japan':'Berlin'})
capitals.update({'German':'Tokyo'})
#pop item will remove the last key from the Dictionary
capitals.popitem()
print(capitals)

#clear will remove all the keys from the Dictionary
#capitals.clear()

#keys fucntion will return all the keys in a Dictionary as List
keys=capitals.keys()
print(keys)

#Like using the above below for loop we can access the every key element
for key in capitals.keys():
    print(key,end=' ')

#like above
#values fucntion will return all the values in a Dictionary as List
print(capitals.values())

#items function will return the entire dictionary as list and every key:value as tupple
print(capitals.items())
#in items function first argument will return the key and second argument will return the value
for key,value in capitals.items():
    print(f'{key}:{value}',end ='\n')

for v,k in capitals.items():
    print(f'{k}:{v}',end ='\n')