# LAUP Practical 8
#Q1)
print('Q1)Find CGD of 2 Numbers ')
a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
def GCD(a,b):
    if b==0:
        return(a)
    else:
        return(GCD(b,a%b))
print("GCD Of ",a,"&",b ,"is",GCD(a,b))
print()

#Q2)
print('Q2)Find a & b Such as a^2-b^2=N')
N=int(input("Enter  Number : "))
def Check(a,b,n):
    if (a*a)-(b*b)==n:
        print("a =",a, "b =",b)
for i in range(0,N+1):
    for j in range(0,N+1):
        Check(i,j,N)
