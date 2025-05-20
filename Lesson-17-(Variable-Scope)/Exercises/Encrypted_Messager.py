import random
import string
chars=string.whitespace+string.punctuation + string.digits+string.ascii_letters
#will give you all the keyboard letters - string.punctuation
#string.digits= will give you all the numbers
#string.ascii_letters = will give you all the uppercase and lower case alphabets
#print(chars)
chars=list(chars)
key=chars.copy()
random.shuffle(key)
#shuffle function in random module will shuffle all the elements inside the list/sequence
#print(f'Chars : {chars}')
#print(f'Key : {key}')

plain_text=input('Enter a message to Encrypt :')
cipher_text=''
for x in plain_text:
    i=chars.index(x)
    cipher_text+=key[i]
print(f'Original Message : {plain_text}')
print(f'Encrypted Message : {cipher_text}')
cipher_text2=input('Enter a message to Decrypt :')
plain_text2=''
for x in cipher_text2:
    i=key.index(x)
    plain_text2+=chars[i]
print(f'Encrypted Message : {cipher_text2}')
print(f'Original Message : {plain_text2}')