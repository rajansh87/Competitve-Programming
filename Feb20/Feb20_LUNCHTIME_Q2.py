def subsequence(ind,arr):
    ma=0
    c=0
    for i in range(len(arr)):
        if(arr[i]!=ind):
            c+=1
        else:
            c=0
        ma=max(c,ma)
    return ma
        
    
tt=int(input())
for qwerty in range(tt):
    n,k=input().split()
    n,k=int(n),int(k)
    #n=int(input())
    arr=list(map(int,input().split()))
    ma=0
    for i in range(1,k+1):
        ma=max(subsequence(i,arr),ma)
    print(ma)


    
    """ans=[]
    a=[]
    z=0
    for i in range(len(arr)):
        if(arr[i]!=k):
            a.append(1)
            z=55
        else:
            ans.append(a)
            a=[]
            z=99
    ans.append(a)
    c=0
    ma=0
    for i in range(len(ans)):
        if(sum(ans[i])>ma):
            ma=sum(ans[i])
    
    print(ma)"""
        
            
    
