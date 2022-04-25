#Find Inverse Of The Matrix using NumPy
import numpy as np
print(" Enter elements of matrix A seprated by ',' and rows seprated by ';' ")
s = input()
A = np.mat(s)
r = A.shape[0]
c=A.shape[1]

print("Dimension Of Matrix A = ", A.shape)
print("Matrix A : ")
print(A)
d = np.linalg.det(A)
print("Determinant : ", d)
if d !=0:
    inv = np.linalg.inv(A)
    print("Inverse Of Matrix : ")
    print(inv)
else:
    print("Matrix Is Not invertible !")
