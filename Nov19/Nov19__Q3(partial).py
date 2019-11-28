import math
def calcDist(x1,y1,x2,y2,x3,y3,x4,y4):
    da=(x2-x1)**2
    db=(y2-y1)**2
    #print(da+db)
    d1=math.sqrt(da+db)
    da=(x3-x2)**2
    db=(y3-y2)**2
    #print(da+db)
    d2=math.sqrt(da+db)
    da=(x4-x3)**2
    db=(y4-y3)**2
    #print(da+db)
    d3=math.sqrt(da+db)
    dis=d1+d2+d3
    return dis

def dist(x1,y1,x2,y2):
    d1=(x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)
    d=math.sqrt(d1)
    return d



t=int(input())
for r in range(t):
    x,y=input().split(" ")
    x,y=int(x),int(y)
    n,m,l=input().split(" ")
    n,m,l=int(n),int(m),int(l)
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    arr=list(map(int,input().split()))
    i=0
    while(i<2*n):
        a.append(arr[i])
        b.append(arr[i+1])
        i+=2
    arr=list(map(int,input().split()))
    i=0
    while(i<2*m):
        c.append(arr[i])
        d.append(arr[i+1])
        i+=2
    arr=list(map(int,input().split()))
    i=0
    while(i<2*l):
        e.append(arr[i])
        f.append(arr[i+1])
        i+=2
    """ma=1000000000000000000
    for i in range(n):
        for j in range(m):
            for k in range(l):
                ans=calcDist(x,y,a[i],b[i],c[j],d[j],e[k],f[k])
                #print("ans : ",ans)
                if(ma>ans):
                    ma=ans
    print(ma)"""
    pa=[]
    pb=[]
    ab=[]
    ba=[]
    ans=1000000000000
    for i in range(n):
        pa.append(0)
        ba.append(0)
    for i in range(m):
        pb.append(0)
        ab.append(0)
    for i in range(n):
        pa[i]=(dist(x,y,a[i],b[i]))
    for i in range(m):
        pb[i]=(dist(x,y,c[i],d[i]))
    for i in range(n):
        ba[i]=100000000000
        for j in range(m):
            ba[i]=min(ba[i],pb[j]+dist(a[i],b[i],c[j],d[j]))
    for i in range(m):
        ab[i]=10000000000
        for j in range(n):
            ab[i]=min(ab[i],pa[j]+dist(c[i],d[i],a[j],b[j]))
    for i in range(l):
        for j in range(n):
            ans=min(ans,ba[j]+dist(e[i],f[i],a[j],b[j]))
        for j in range(m):
            ans=min(ans,ab[j]+dist(e[i],f[i],c[j],d[j]))
    print(ans)
            
    
    
                    
    
            
        
