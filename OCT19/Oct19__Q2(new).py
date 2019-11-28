t=int(input())
for u in range(t):
    n,m,q=input().split()
    n,m,q=int(n),int(m),int(q)
    #a=list(map(int,input().split()))
    a1=[]
    a2=[]
    for i in range(n):
        a1.append(0)
    for i in range(m):
        a2.append(0)
    
    for e in range(q):
        x,y=input().split(" ")
        x,y=int(x),int(y)
        x-=1
        y-=1
        a1[x]=(a1[x]+1)%2
        a2[y]=(a2[y]+1)%2
    c=0
    z=0
    for j in range(m):
        if(a2[j]==1):
            z+=1
    for i in range(n):
        if(a1[i]==0):
            c+=z
        else:
            c+=m-z
    print(c)
        
               
               



    
    
