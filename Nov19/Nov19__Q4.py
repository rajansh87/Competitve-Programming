# cook your dish here
t=int(input())
for u in range(t):
    n,m=input().split(" ")
    n,m=int(n),int(m)
    arr=list(map(int,input().split()))
    dif=0
    i=0
    j=0
    mi=10000000000000
    color=[]
    ans=0
    """for i in range(n):
        k=1
        for j in range(m):
            color.append(str(k))
            k+=1
    color=color[:n]"""
    color=[i%m for i in range(n)]
    a=list(zip(arr,color))
    a.sort()
    count=[0 for i in range(n)]                        
    count[a[0][1]]+=1
    c=1
    i=0
    j=0
    while(i<n):
        if(c==m):
            dif=a[j][0]-a[i][0]
            if(mi>dif):
                mi=dif
            count[a[i][1]]-=1
            if(count[a[i][1]]==0):
                c-=1
            i+=1
        else:
            j+=1
            if(j==n):
                break
            count[a[j][1]]+=1
            if(count[a[j][1]]==1):
                c+=1
    print(mi)
            
            













