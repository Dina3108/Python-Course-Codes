import math

radius=float(input('Enter the Radius of the Circle:'))
circumference=2*(math.pi)*radius
print(f'The Circumference of the Circle  : {round(circumference,2)}')

Area=(math.pi)*pow(radius,2)
print(f'Area of the Circle:{round(Area,2)} cm^2')

a=float(input('Enter the a - side of the Triangle:'))
b=float(input('Enter the b - side of the Triangle:'))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f'Other Side of the Triangle : {round(c,2)}')