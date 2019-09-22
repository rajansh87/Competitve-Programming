t=int(input())
for r in range(t):
    n,z=input().split(" ")
    n,z=int(n),int(z)
    a=list(map(int,input().split()))
    h=0
    if(2*a[n-2]<=a[n-1]):
        h=a[n-2]*2
    else:
        h=a[n-1]
        
    for i in range(3,n+1):
        if(i*a[n-i]<=a[n-1]):
            if(h>i*a[n-i]):
                h=i*a[n-i]
        else:
            if(h>a[n-1]):
                h=a[n-1]
    print(h)
    
