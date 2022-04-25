def dot(x,y):
    return sum([x[i]*y[i] for i in range(len(x))])
	
def scalar(a,v):
    return [a*v[i] for i in range(len(v))]
	
def sub(u,v):
    return[u[i]-v[i] for i in range(len(v))]
	
def project_along(b,v):
    sigma=(dot(b,v)/dot(v,v)) if dot(v,v)!=0 else 0
    return scalar(sigma,v)
	
def project_orthogonal(b,v):
    return sub(b,project_along(b,v))
print("orthogonal projection of b=[5,-5,2] on v=[8,-2,2] is", project_orthogonal([1,1,2],[1,2,1]))

def project_orthogonalvectoret(b,s):
    for i in range(len(s)):
        v=s[i]
        b=project_orthogonal(b,v)
    return(b)
print("orthogonalvector projection of b=[5,-5,2] on s={[8,-2,2],[0,3,3]} is",project_orthogonalvectoret([1,1,2],[1,2,1]))
