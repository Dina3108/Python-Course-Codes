'''
if __name__=='__main__': (this script can be imported OR run standalone) 
          functions and classes in this module can be reused
          without the main block of code executing
          Uses: Code is Modular,
          helps readability,
          leaves no global variables
          avoid unintented execution

Using the above if condition, if it satisfies or gives main means only it will work in that file

if the module was imported in that file that __name__  if-condition will give the imported module name
'''
def main():
    print(__name__)
food='pizza'
if __name__=='__main__':
    main()
    print(f'My Favourite Food is {food}')
    #This doder == main codes only executes in this source file and the code were written in the file
print('This is from Source File')

