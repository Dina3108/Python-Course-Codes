class Car:
    #below is known as Constructor method to form an object
    def __init__(self,model,year,color,for_sale):
        #self - it will denote it to that object
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
    
    def drive(self):
        print(f'You Drive the {self.model}')
    def stop(self):
        print(f'You Stop the {self.model}')
    def describe(self):
        print(f'{self.year} {self.color} {self.model}')
    #self denotes it to its object