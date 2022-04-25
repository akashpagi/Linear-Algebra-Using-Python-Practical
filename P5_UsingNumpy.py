import numpy as np
a = np.array([[1,2],[3,4]])
print("Matrix A is",a)
b = np.array([[1,2],[1,1]])
print("Matrix B is",b)
print('Multiplication of two matrices a & b is')
M = ([[0,0],[0,0]])
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            M[i][j]+=a[i][k]*b[k][j]
            for r in M:
                print(r)
