t=int(input())
for u in range(t):
    n,k=input().split()
    n,k=int(n),int(k)
    arr=list(map(int,input().split()))
    """for i in range(k):
        a=arr[i%n]
        b=arr[n-(i%n)-1]
        arr[i%n]=a^b"""
    x=k%(3*n)
    if(n%2!=0 and k>n//2):
        arr[n//2]=0
    for i in range(x):
        arr[i%n]=arr[i%n]^arr[n-(i%n)-1]
    
    

    print(*arr,sep=" ")
               
               



    
    
