'''
Exception - An event that interrupts the flow of a program (Zero Division Error, TypeError, ValueError)
          1.try, 2.except, 3.finally
'''
#Zerodivision Error occurs if you divide the element by zero
#Type Error - will occur if you try to do opertaions between 2 different datatypes
#Value error - will occur if you try typecast the wrong datatype
try:
    #In try block write the code you want to Execute
    number=int(input('Enter a number : '))
    print(1/number)
#when this error happens means it instead of showing error in the compiler it will print the below statement
except ZeroDivisionError:
    print('You cant divide number by Zero')
except ValueError:
    print('Enter only numbers Please!')
#Exception will work other errors rather than the above mentioned errors
except Exception:
    print('Something went Wrong...!')
    #Finally block will execute at the program even if error occurs/ not occurs
finally:
    print('Do some Code Cleanup Here')