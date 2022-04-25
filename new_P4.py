'''
global r,c

def printmatrix(A):
    print("The Entered matrix is :")
    for i  in range(r):
        print(A[i])       

def printrows(A):
    print("Rows of the given matrix : ")
    for i in range(r):
        print("Row%d="%i,A[i])

def printrows(A):
    print("Columns of the given matrix : ")
    for j in range(r):
        print("Column%d="%j,end=" ")
        for i in range(r):
            print(A[i][j],end=" ")
        print("\n")            

def scalamul(A):
    N=[[s*A[i][j] for i in range(r)] for i range(r)]
    print("scalar multiplication is s*M = ")
    printmatrix(N)
#transpose
def transpose(A):
    T=[[A[i][j] for i in range(r)] for j in range(c)]
    print("Transpose of Matrix M = ")
    for j in range(c):
        print(T(j)]
print("Enter the dimension of the matrix :")
r=int(input("Enter no of rows : "))
c=int(input("Enter no of colums:"))
    
  



2
2
3
4
calar 2

'''

global r,c
#Display M in matrix format
def printmatrix(A):   
  print("The entered matrix is : ")
  for i in range(r):
    print (A[i])
    
#Display rows of matrix
def printrows(A):      
  print("Rows of given matrix is : ")
  for i in range(r):
    print("Row%d="%i,A[i])

#Display colums of matrix
def printcol(A):        
  print("Columns of the given matrix : ")
  for j in range(c):
    print("Column%d="%j,end=" ")
    for i in range(r):
      print(A[i][j],end=" ")
    print("")

#Scalar multiplication
def scalarmul(A,s):    
  N=[[s*A[i][j] for j in range(c)] for i in range(r)]
  print("Scalar multiplication (s*M) is  ")
  printmatrix(N)

 #Transpose 
def transpose(A):         
  T=[[A[i][j] for i in range(r)] for j in range(c)]
  print("Transpose of matrix M = ")
  for j in range(c):
    print(T[j])

print("Enter the dimension of matrix :")
r=int(input("Enter the no of rows :"))
c=int(input("Enter the no of columns :"))
M=[]
for i in range(r):
  print("Enter element of rows ",i,":")
  M.append([])
  for j in range(c):
    n=int(input("Enter element :"))
    M[i].append(n)
printmatrix(M)
printrows(M)
printcol(M)
s=int(input("Enter the scalar value:"))
scalarmul(M,s)
transpose(M)







        


    
