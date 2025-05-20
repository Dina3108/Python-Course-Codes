''''
format specifiers - {value:flags} format a value based on what flags are inserted

different input flags we can insert follows below:
'''

num=48394893.90990
#number in all comment line denotes our preferred input
#(number).f = round to that many decimal places (fixed point)
print(f'Number is {num:.2f}')
#:(number) = allocate to that many places as per the given number
print(f'Number is {num:20}')
#:0(number) = Allocates that much spaces and fill all the spaces with zero
print(f'Number is {num:020}')
#:< = left justify
print(f'Number is {num:<20}')
#:< = right justify
print(f'Number is {num:>20}')
#:< = center justify
print(f'Number is {num:^20}')
#:+ = use a plus sign to indicate positive value
print(f'Number is {num:+}')
#:=  =place sign to leftmost position
print(f'Number is {num:=}')
#:space = insert a space before positive numbers
print(f'Number is {num: }')
#:, = comma seperator
print(f'Number is {num:,}')

'''
We can combine format Specifiers as per our convenience also
'''
print(f'Number is {num:+,.4f}')