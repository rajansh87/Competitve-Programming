tt=int(input())
for qwerty in range(tt):
    ans="Case #"
    n=int(input())
    #a,b=map(int,input().split())
    A=list(map(int,input().split()))            
    #brr=list(map(int,input().split()))            
    
    dp = {}
    prev = A[0]
    d = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            ## In Every iteration, we first check if i th index along with A[j]-A[i]
            ## difference has been memotized. If yes, we add jth index along with
            ## same difference as key in dp, and value is 1+dp[(i,A[j]-A[i])] and
            ## remove the previous memo (to save space). If the original memo wasn't 
            ## present, we memotize it now.
            if j==i+1:
                if (i,A[j]-A[i]) in dp:
                    dp[(j,A[j]-A[i])]  = 1+dp[(i,A[j]-A[i])]
                    del dp[(i,A[j]-A[i])]
                else: dp[(j,A[j]-A[i])] = 1
    maxx = 0
    ## we now find the maximum count
    for i in dp:
        if dp[i]>maxx: maxx = dp[i]
    mi=(maxx+1)

        
                
    ans+=str(qwerty+1)+":"
    print(ans,mi,sep=" ")

#===================================================        
tt=int(input())
for qwerty in range(tt):
    ans="Case #"
    n=int(input())
    #a,b=map(int,input().split())
    arr=list(map(int,input().split()))            
    z=2
    v=2
    dif=arr[1]-arr[0]
    for i in range(2,n):
        if arr[i]-arr[i-1]==dif:
            v+=1
        else:
            dif=arr[i]-arr[i-1]
            z=max(z,v)
            v=2
    mi=max(z,v)
    


    
                
    ans+=str(qwerty+1)+":"
    print(ans,mi,sep=" ")
        
