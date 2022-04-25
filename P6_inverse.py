def printmatrix(A):
    for i in range(len(A)):
        print(A[i])
def Transpose(A):
    T=[[A[i][j] for i in range(len(A))] for j in range(len(A))]
    return T

c=int(input("Enter the Matrix Dimensoin: "))
r=c
m=[]
for i in range(r):
    print('Enter Elements of Rows :',i)
    m.append([])
    for j in range(c):
        n=int(input("Enter No:"))
        m[i].append(n)
print("The Entered Matrix M is ")
printmatrix(m)

d=0
if r==2:
    d = m[0][0] * m[1][1] - m[0][1] * m[1][0]
    print("Determinant=",d)
    if d==0:
        print("Matrix is Not Invertible !")
    else:
        print("Matrix is Invertible .")
        cfm=[ ]
        for i in range(2):
            cfm.append([ ])
        cfm[0].append(m[1][1])
        cfm[0].append(- m[0][1])
        cfm[1].append(- m[1][0])
        cfm[1].append(m[0][0])
        print("Co-factor Matrix :")
        printmatrix(cfm)
       
        mi= []
        for i in range(2):
            mi.append([])
            for j in range(2):
               mi[i].append(cfm[i][j] / d)
        print("Inverse Of Matrix is :")
        printmatrix(mi)
else:
    for i in range(3):
        d = d + ( m[0][i] *  ( m[1] [(i+1)%3] * m[2] [(i+2)%3] - m[1] [(i+2)%3]  * m[2] [(i+1)%3] ) )
    print("Determinant=",d)
    if d==0:
        print("Matrix  is Not Invertible !")
    else:
        print("Matrix is Invertible !")
        cfm=[ ]
        for i in range(3):
            cfm.append([ ])
            for j in range(3):
                v= ( m[(i+1)%3] [(j+1)%3] * m[(i+2)%3] [(j+2)%3] ) - ( m[(i+1)%3] [(j+2)%3] * m[(i+2)%3] [(j+1)%3] )
                cfm[i].append(v)
        print("Co-factor matrix :")	
        printmatrix(cfm)
        
        adj_m=Transpose(cfm)                
        mi=[]
        for i in range(3):
            mi.append([])
            for j in range(3):
                mi[i].append(adj_m[i][j]/d)
        print("Inverse of The Matrix  ")
        printmatrix(mi)

        
        
               
        
        















        
    
