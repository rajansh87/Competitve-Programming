def orfunc(arr):
    z=0
    for i in range(len(arr)):
        z=z|arr[i]
    return z
        
t=int(input())
for u in range(t):
    #n,k=input().split(" ")
    #n,k=int(n),int(k)
    #arr=list(map(int,input().split()))
    n=int(input())
    arr=list(map(int,input().split()))
    brr=arr.copy()
    ans1=ans2=0
    i=0
    x=0
    poping=[]
    ans=[]
    while(len(arr)!=0):
        x+=orfunc(arr)
        y=0
        z=0
        poping=[]
        for i in range(len(arr)):
            z=arr.pop(i)
            y=orfunc(arr)
            poping.append(y)
            arr.insert(i,z)
        m=0
        ind=0
        for i in range(len(poping)):
            if(m<poping[i]):
                m=poping[i]
                ind=i
        p=arr.pop(ind)
        ans.append(p)
    print(x)
    #print(ans)
    r=[]
    for i in range(len(ans)):
        z=brr.index(ans[i])
        r.append(z+1)
    s=""
    for i in range(len(r)):
        s+=str(r[i])
        s+=" "
    print(s)
        
            
        
               
               



    
    

               
               



    
    
