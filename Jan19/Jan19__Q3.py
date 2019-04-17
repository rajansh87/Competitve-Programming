n=input()
m=input()
a=[]
b=[]
i=0
while(i<n):
    p=input()
    a.append(p)
    i=i+1
    
i=0
while(i<m):
    q=input()
    b.append(q)
    i=i+1
z=0
j=0
i=0
s=[]
while(i<n):
    j=0
    while(j<m):
        s.append(a[i]+b[j])
        j=j+1
    i=i+1


j=0
i=0
while(i<n*m):
    if(s.count(s[i])==1):
        print i," "
    i=i+1
