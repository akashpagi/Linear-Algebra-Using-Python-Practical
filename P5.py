global r1,c1,r2,c2
# Display M in matric Format
def printmatrix(A):
    for i in range(len(A)):
        print(A[i])        
#Matrix Addtion
def MatrixAdd(A,B):
    c=[ [A[i][j] + B[i][j] for j in range(len(B[0]))] for i in range(len(A))]
    print('Addition of two Matrix = ')
    printmatrix(c)
#Matrix Multiplication
def MatrixMul(A,B):
    C= [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    print('Multiplication of two Matrix = ')
    printmatrix(C)
#Matrix Vector Multiplication
def Matrix_VMul(A,v):
    C= [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
    print('Matrix Vector Multiplication (M1*v) = ',C)    
# Vector Matrix Multiplication
def V_MatrixMul(v,A):
    C= [sum(v[j]*A[j][i] for j in range(len(v))) for i in range(len(A))]
    print('Vector Matrix Multiplication (v*M1) = ',C)
#Enter (r X c) Matrix M
print('Enter the Dimention of Matrix 1 ')
r1=int(input('Enter No. of Rows : '))
c1=int(input('Enter No. of Columns : '))
M=[]
for i in range(r1):
    print('Enter Elements of row',i,':')
    M.append([ ])
    for j in range(c1):
        n=int(input('Enter No :'))
        M[i].append(n)
print('The Entered Matrix M1 is ')
printmatrix(M)
print()
#Enter (r X c) Matrix N
print('Enter the Dimention of Matrix 2 ')
r2=int(input('Enter No. of Rows : '))
c2=int(input('Enter No. of Columns : '))
print()
N=[]
for i in range(r2):
    print('Enter Elements of row',i,':')
    N.append([ ])
    for j in range(c2):
        n=int(input('Enter No :'))
        N[i].append(n)
print('The Entered Matrix M2 is ')
printmatrix(N)
print()
print('Select Operation')
print('1.Matrix Addition')
print('2.Matrix Multiplication')
print('3.Matrix Vector Multiplication')
print('4.Vector Matrix Multiplication')
while True:
    Ch=int(input('Enter Choice For Operation : '))
    if Ch==1:
        if(r1,c1)==(r2,c2):
            MatrixAdd(M,N)
        else:
            print('Invalid Matrix: Addtion is performed on same sizes of matrix')            
    elif Ch==2:
        if c1==r2:
            MatrixMul(M,N)
        else:
            print('Invalid Matrix: To Multiply Two Matrices Matrix1 cols = Matrix2 Rows matrix')
    elif Ch==3:
        s=input('Enter Elements of Vector Separated by Spaces :')
        v=[int(x) for x in s.split()]
        print(len(v))
        if len(v)!=r1:
            print("Invalid Vector ! add vector of%d elements (Columns of M1) %r1")
        else:
            Matrix_VMul(M,v)
    elif Ch==4:
        s=input('Enter Elements of Vector Separated by Spaces :')
        v=[int(x) for x in s.split()]
        print(len(v))
        if len(v)!=r1:
            print("Invalid Vector ! add vector of%d elements (Rows of M1) %r1")
        else:
            V_MatrixMul(v,M)
    else:
        break
            
            







              
        
    












    
    




    




    
    
    
    
