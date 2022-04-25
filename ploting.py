#practical 1

'''
c=29+7j
print(c.real)
print(c.imag)
print(c.conjugate)
d=10-2j
e=c+d
print("addition is ",e)
f=c-d
print("subtraction is ",f)
print("multiplication is",c*d)
print("division is",c/d)
'''
import matplotlib.pyplot as plt
s={3+3j, 2+1j,5+1j,4+3j}
print(s)
X=[x.real for x in s]
Y=[x.imag for x in s]
plt.plot(X,Y,'ro')
plt.axis([-6,6,-6,6])
plt.show()	

#moves to second quadrant
s1={x*(1j) for x in s}
print(s1)

#moves to third quadrant
s1={x*(-1) for x in s}
print(s1)

#moves to fourth quadrant
s1={x*(-1)*(1j) for x in s}
print(s1)

#Scaling 
s={3+3j, 2+1j,5+1j,4+3j}
print(s)
s1={x*(0.5) for x in s}
print(s1)
X=[x.real for x in s1]
Y=[x.imag for x in s1]
plt.plot(X,Y,'go')
plt.show()

#Scaling 
s={3+3j, 2+1j,5+1j,4+3j}
print(s)
s1={2*x for x in s}
print(s1)
X=[x.real for x in s1]
Y=[x.imag for x in s1]
plt.plot(X,Y,'go')
plt.show()

#Translation
s={3+3j, 2+1j,5+1j,4+3j}
print(s)
c=complex(input("Enter a complex no for translation :"))
s1={x+c for x in s}
print(s1)
X=[x.real for x in s1]
Y=[x.imag for x in s1]
plt.plot(X,Y,'cD')
plt.show()
'''
