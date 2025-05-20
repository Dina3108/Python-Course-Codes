'''input = is a function that prompts the user to enter data and returns entered Data as a String'''
 
input('Enter you Name:')
#Like above the input function displays the user data in terminal window

#And input function also returns the entered data in the terminal as a string to store it in a variable
name=input('Enter you Name:')
age=input('Enter Your Age:')
print(f'Hi {name}...!!!')
#As age is in string where it is from input function
age=int(age)+1
print(f'Happy Birthday... Your are {age}Years Old')

#We have shortcut for typecasting in input function
age=int(input('Enter Your Age:'))