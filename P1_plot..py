'''
import matplotlib.pyplot as plt

#Addition of the two comlpex number
a=29+7j
b=10-2j
c=a+b
print("real number :",a.real)
print("Imag number :",a.imag)
print()
print("Addition of the two comlpex number is ",c)
print()
#Displaing the Conjugate of a complex number
print("Original Complex number :",a)
print("Conjugate of a complex number :",a.conjugate())
print()

# Plotting a set of complex numbers 
s={3+3j, 2+1j,5+1j,4+3j}
print('s : ',s)
X=[x.real for x in s]
Y=[x.imag for x in s]
plt.plot(X,Y,'go')  # 'g' means green color & 'o' means circle symbol
plt.axis([-6,6,-6,6])
plt.show()

import matplotlib.pyplot as plt
print('Plotting a new set for 90 degree')
print("Original Set 'S'")
S={3+3j, 2+1j,5+1j,4+3j}
print('S :',S)
S1={x*(1j) for x in S}
print()
print("Set 'S' after multiplication with (1j )")
print('S1 :',S1)
X=[x.real for x in S1]
Y=[x.imag for x in S1]
plt.plot(X,Y,'bo')
plt.show()
print()


import matplotlib.pyplot as plt
print('Plotting For 180 degree')
print("Original Set 'S'")
S={3+3j, 2+1j,5+1j,4+3j}
print('S :',S)
S1={x*(-1) for x in S}
#print()
print("Set 'S' after multiplication with (-1)")
print('S1 :',S1)
X=[x.real for x in S1]
Y=[x.imag for x in S1]
plt.plot(X,Y,'bo')
plt.title("By 180 Degree")
plt.show()

'''
import matplotlib.pyplot as plt
print('Plotting For 270 degree')
print("Original Set 'S'")
S={3+3j, 2+1j,5+1j,4+3j}
print('S :',S)
S1={x*(-1)*(1j) for x in S}
#print()
print("Set 'S' after multiplication with (-1)*(1j)")
print('S1 :',S1)
X=[x.real for x in S1]
Y=[x.imag for x in S1]
plt.plot(X,Y,'bo')
plt.show()

'''
import matplotlib.pyplot as plt
print('Scaling by a=1/2')
print("Original Set 'S'")
S={3+3j, 2+1j,5+1j,4+3j}
print('S :',S)
S1={x*(0.5) for x in S}  #a=0.5
print()
print("Set 'S' after scaling by a=1/2")
print('S1 :',S1)
X=[x.real for x in S1]
Y=[x.imag for x in S1]
plt.plot(X,Y,'go')
plt.show()

import matplotlib.pyplot as plt
print('Scaling by a=2')
print("Original Set 'S'")
S={3+3j, 2+1j,5+1j,4+3j}
print('S :',S)
S1={2*x for x in S}  
print()
print("Set 'S' after scaling by a=2")
print('S1 :',S1)
X=[x.real for x in S1]
Y=[x.imag for x in S1]
plt.plot(X,Y,'co')
plt.show()


import matplotlib.pyplot as plt
print('Scaling by a=1/3')
print("Original Set 'S'")
S={3+3j, 2+1j,5+1j,4+3j}
print('S :',S)
S1={x*(0.3333333) for x in S}  
print()
print("Set 'S' after scaling by a=1/3")
print('S1 :',S1)
X=[x.real for x in S1]
Y=[x.imag for x in S1]
plt.plot(X,Y,'co')
plt.show()
'''
