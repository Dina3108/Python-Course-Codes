'''
Magic methods - Dunder methods (double underscore) __int__,__str__,__eq__
                they are automatically called by many of python's built-in operation
                Theya allow developers to define or customize the behaviour of objects
'''
class Book:
    def __init__(self,name,author,num_pages):
        self.name=name
        self.author=author
        self.num_pages=num_pages
    def __str__(self):
        return f'{self.name} of {self.author}'
    def __eq__(self, other):
        return self.num_pages == other.num_pages
    
    #For doing the lower than option
    def __lt__(self,x):
        return self.num_pages< x.num_pages
    
    #For doing the greater than option
    def __gt__(self,x):
        return self.num_pages> x.num_pages
    
    #for doing addition operation
    def __add__(self,x):
        return self.num_pages+x.num_pages
    
    #for checking the keyword in object
    def __contains__(self,x):
        return x in self.author or x in self.name
    
    #Used in dictionary for getting values from input of keys
    def __getitem__(self,x):
        if x=='name':
            return self.name
        elif x=='author':
            return self.author
        elif x=='num_pages':
            return self.num_pages
    
book1=Book('HarryPotter','JK Rowling',1290)
book2=Book('Piartes of the Caribean','Johnny Depp',1291)
#Using the __str__ attribute , if we try to print the book the memory address of the book object , but by using the __str__ attribute we can return defined statements by ourself 
print(book1)
#Normally equating function wont work while directly using the objects but using __eq__ we can do
print(book1==book2)
print(book1<book2)
print(book1>book2)
print(book1+book2)
print('HarryPotter' in book2)
print('HarryPotter' in book1)
print(book2['name'])
