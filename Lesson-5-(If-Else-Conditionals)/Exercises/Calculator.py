operator=input('Enter the Operator (+ - * / % **):')
num1=float(input('Enter the Number 1 :'))
num2=float(input('Enter the Number 2 :'))
if operator=='+':
    print(round(num1+num2,3))
elif operator=='-':
    print(round(num1-num2,3))
elif operator=='*':
    print(round(num1*num2,3))
elif operator=='/':
    print(round(num1/num2,3))
elif operator=='%':
    print(round(num1%num2,3))
elif operator=='**':
    print(round(num1**num2))
else:
    print(f'{operator} is Invalid Operator')


 