import numpy as np
tt=int(input())
for qwerty in range(tt):
    n=int(input())
    ans="Case #"
    ans+=str(qwerty+1)+": "
    space=" "
    arr=list(map(int,input().split()))
    count=0
    for i in range(1,n-1):
        if arr[i-1]<arr[i]>arr[i+1]:
            count+=1
    ans+=str(count)

    




    print(ans)   
