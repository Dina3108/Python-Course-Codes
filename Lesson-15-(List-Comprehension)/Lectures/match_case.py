'''
Match Case statement (switch) : An alternative to using 'elif' statements 
Execute some code if a value matches a 'case'
Benifits: Cleaner and syntax is more readable

Like Switch Case in C Programming
'''

def day_number(day):
    match day:
        case 1:
            print('Monday')
        case 2:
            print('Tuesday')            
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')
        case 7:
            print('Sunday')
        #below is for else acts as default case executes when above all conditions are false
        case _:
            print('Invalid Day number..!')
day_number(5)
day_number(90)

def day_number_simple(day):
    match day:
        #we can use or operator like below also
        case 1 | 2 | 3 | 4:
            return True
        case 5 | 6 | 7:
            return False       
        #below is for else acts as default case executes when above all conditions are false
        case _:
            print('Invalid Day number..!')
print(day_number_simple(7))