class Person:
    def __init__(self,x):
        self._name=x

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,x):
        if x.isalpha():
            print('Enter Valid name')
        else:
            self._name=x
            
    def name_print(self,x):
        print(f'Your name is {self._name}')
    
p1=Person('Dinakar123')
print(p1._name)
p1._name='Harini123'
print(p1._name)