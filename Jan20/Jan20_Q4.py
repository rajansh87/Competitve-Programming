"""def countIncreasing(arr, n):
    cnt = 0
    len = 1
    for i in range(0, n - 1) :
        if arr[i + 1] > arr[i] :
            len += 1
        else:
            cnt += (((len - 1) * len) / 2) 
            len = 1
    if len > 1:
        cnt += (((len - 1) * len) / 2) 
    return cnt

def countDecreasing(arr, n):
    cnt = 0
    len = 1
    for i in range(0, n - 1) : 
        if arr[i + 1] < arr[i] :
            len += 1
        else:
            cnt += (((len - 1) * len) / 2) 
            len = 1
    if len > 1:
        cnt += (((len - 1) * len) / 2) 
    return cnt
"""
n,q=input().split()
n,q=int(n),int(q)
arr=list(map(int,input().split()))
val=[0]*n
x=0
if(arr[1]>arr[0]):
    x=1
else:
    x=0
    
for i in range(2,n):
    val[i]=val[i-1]
    if((arr[i]>arr[i-1]) and (x!=1)):
        val[i]+=1
        x=1
    elif((arr[i]<arr[i-1]) and (x!=0)):
        val[i]+=1
        x=0
        

    
for queries in range(q):
    l,r=input().split()
    l,r=int(l),int(r)    
    #if(len(arr[l-1:r])!=1):
    """x=int(countIncreasing(arr[l-1:r], len(arr[l-1:r])))
    y=int(countDecreasing(arr[l-1:r], len(arr[l-1:r])))
    if(x==y):
        print("YES")
    else:
        print("NO")
    #else:
        #print("NO")"""

    if((val[r-1]-val[l])%2!=0):
        print("YES")
    else:
        print("NO")
        
    
        
