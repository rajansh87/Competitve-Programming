import numpy as np
tt=int(input())
for qwerty in range(tt):
    n=int(input())
    #s,n=map(int,input().split())
    arr=list(map(int,input().split()))            
    ans="Case #"
    ans+=str(qwerty+1)+": "
    arr=[-1]+arr
    arr.append(-1)
    c=0
    prevMax=-1
    ma=-1
    cur=0
    flag=1

    for i in range(n+2):
        cur=arr[i]
        if flag and cur<prevMax and ma<prevMax:
            c+=1
            ma=prevMax
        if cur>prevMax:
            flag=1
        else:
            flag=0
        prevMax=cur
            
        
    #print(c)

    print(ans+str(c))   
