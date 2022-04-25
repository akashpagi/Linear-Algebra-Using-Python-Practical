#Find Dot Product using NumPy
import numpy as n
x = n.array([5,6,7])
y = n.array([1,2,3])
print(x)
print(y)
a = int(input("Enter Value Of a : "))
b = int(input("Enter Value Of b : "))
c = a*x + b*y
d = n.dot(x,y)
print('ax + by =',c)
print('Dot Product',d)
