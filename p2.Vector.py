def addvec(x,y):
        return[x[i]+y[i] for i in range(len(x))] 
def subvec (x,y):
        return[x[i]-y[i] for i in range (len(x))]
def scalarmul(x,p):
        return[p*x[i] for i in range(len(x))]
def dotprod(x,y):
        return sum([x[i]*y[i] for i in range(len(x))])
u=[]
v=[]
n=int (input("Enter the length of the vectors: "))
print("Enter the elements of vector u: ")
for i in range(n):
        elem=int(input("Enter elements: "))
        u.append(elem)
print("Vector u: ",u)
print("Enter the elements of vector v: ")
for i in range(n):
        elem=int(input("Enter elements: "))
        v.append(elem)
print("Vector v: ",v)
print("Addition of vectors u and v is ",addvec(u, v))
print("Subtration of vectors u and v is ", subvec(u, v))
#au+bv
a=int (input("Enter the value of a: "))
b=int (input("Enter the value of b: ")) 
print("Sclarmultiplication of a with u is au ", scalarmul(u,a)) 
print("Sclarmultiplication of b with v is bv ",scalarmul(v,b))
print("The value of au+bv is" , addvec(scalarmul(u, a), scalarmul(v,b)))
#dot product
print("Dot product of u and v is ", dotprod(u,v))

