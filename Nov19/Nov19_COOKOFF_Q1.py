t = int(input())
for q in range(t):
    n,k=input().split()
    n,k=int(n),int(k)
    #n,m,k=input().split()
    #n,m,k=int(n),int(m),int(k)
    #n=int(input())
    arr=list(map(int,input().split()))
    s=0
    pos=-1
    z=0
    for i in range(n):
        s+=arr[i]
        if(s<k):
            pos=i+1
            z=55
            print("NO ",pos)
            break
        else:
            s-=k
    
    if(z!=55):
        print("YES")
   
    
        
        
            
    
