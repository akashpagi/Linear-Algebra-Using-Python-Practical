def scalmul (x,p):
    return [p*x[i] for i in range(len(x))]
def lc(vlist,slist):
    s = [scalmul(vlist[i],slist[i]) for i in range(len(vlist))]
    print('s :',s)
    l = [ ]
    for j in range(len(s[0])):
       sum=0
       for i in range(len(s)):
           sum=sum+s[i] [j]
       l.append(sum)
    return l
m = lc( [ [1,2,3], [0,1,4] , [2,-1,1] ] , [2,-1,3] )
print('Linear Combination is ',m)
print()
n = int(input('Enter Length Of Vector:'))
u = []
v = []
print('Enter the elements of u ')
for i in range(n):
    ele = int(input('Enter The element :'))
    u.append(ele)
print('Vector u:',u) 
print()
print('Enter the elements of v')
for i in range (n):
    ele = int(input('Enter The element :'))
    v.append(ele)
print('Vector v:',v)  
print()
print("Enter The Coffecient ")
c1 = int(input('Enter 1st Coffecient:'))
c2 = int(input('Enter 2nd Coffecient:'))
print()		
newface = [ c1 * u[i] + c2 * v[i] for i in range(len(u)) ]
print('New Face Of The Vector u and v is ',newface)
print()
avgface = [ (u[i]+v[i])/2 for i in range(len(v))]
print('Average Face Of The Vector u and v is ',avgface)

