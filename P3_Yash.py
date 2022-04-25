def scalmul(x,p):
    return[p*x[i]for i in range (len(x))]
def lincomb(v,c):
    s=[scalar(v[i],c[i]) for i in range(len(v))]:
    l=[]
    
    for j in range(len(s[0])):
        sum=0
        for i in range(len(s)):
            sum=sum+s[i][j]
            l.append(sum)
    return l
print("liner combination",lincomb([[1,2,3],[3,4,5],[0,-2,1]],[1,2,-1]))

n= int(input("enter length of vectors:"))
u=[]
v=[]
print("enter  elements of u:")
for i in range(n):
	e=int(input("enter elements:"))
	u.append(e)
print("vector u=",u)

print("enter elements of v:")
for i in range(n):
	e=int(input("enter elements:"))
	v.append(e)
print("vector v=",v)

print("enter the coeifficient:")
c1=int(input("enter 1st coeifficient:"))
c2=int(input("enter 2st coeifficient:"))
newface=[c1*u[i]+c2*v[i] for i in range(len(u))]
print("new face of vector u and v is",newface)

avgface=[(u[i]+v[i])/2 for i in range(len(v))]
print("Avrage face of vector u and v is",avgface)
