t=int(input())
for r in range(t):
    #n,query=input().split(" ")
    #n,query=int(n),int(query)
    #n=int(input())
    #n,m=input().split(" ")
    #n,m=int(n),int(m)
    n=int(input())
    arr=[0]
    for i in range(n-1):
        x=arr[-1]
        if(x not in arr[:-1]):
            arr.append(0)
        else:
            b=arr[:-1].copy()
            b.reverse()
            pos=b.index(x)
            pos=len(b)-pos
            z=len(arr)-pos
            arr.append(z)

    ans=arr.count(arr[n-1])
    #print(arr)
    print(ans)
            
            
    
        
    
            
        
