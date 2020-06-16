tt=int(input())
for qwerty in range(tt):
    #n=int(input())
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))

    s=0
    x=0
    for i in range(n):
        s+=arr[i]
        if arr[i]>=k:
            x+=k
        else:
            x+=arr[i]
    print(s-x)
            
        

    

