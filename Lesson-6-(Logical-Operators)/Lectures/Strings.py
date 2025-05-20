name=input('Enter your Name :')
#len function in string counts the number of characters in the word inclluding the spaces
print(len(name))
#find function will find the specific character and returns the index number where it was from left to right direction
print(name.find('n'))
# If the character is not found it will return the index number as -1
#rfind function will return the last occurence of the character it will return its index number
print(name.rfind('a'))
#capitalize function will return the string by capitalising the first letter
print(name.capitalize())
#upper will convert all to uppercase
#lower will convert all to lowercase
print(name.lower())
print(name.upper())
#is_digit function will check the string contains all as numbers
print(name.isdigit())
#is_alpha function will check the string contains all as string without any space
print(name.isalpha())
ph_no=(input('Enter your Mobile Number:'))
#count function will count the number of characters that were occured
print(ph_no.count('0'))
print(ph_no.replace('-',''))
#replace function will replace the specified character into another character
print(help(str))