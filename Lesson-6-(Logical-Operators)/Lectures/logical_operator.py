'''
logical operators = evaluate multiple conditions (or,and,not)
or = at least one condition must be true
and = both conditions must be true
not = inverts the condition (False to True,True to False)
'''
temp=27
is_sunny=False
if temp>=28 and is_sunny:
    print('It is HOT Outside 🥵')
    print('It is Sunny ☀️')
elif temp<=0 and is_sunny:
    print('It is COLD Outside 🥶')
    print('It is Sunny ☀️')
elif 28>temp>0 and is_sunny:
    print('It is Warm Outside 😇')
    print('It is Sunny ☀️')
elif temp<=0 and not is_sunny:
    print('It is HOT Outside 🥵')
    print('It is Cloudy ☁️')
elif temp<=0 and not is_sunny:
    print('It is COLD Outside 🥶')
    print('It is Cloudy ☁️')
elif 28>temp>0 and not is_sunny:
    print('It is Warm Outside 😇')
    print('It is Cloudy ☁️')

