t=int(input())
for qwerty in range(t):
    n,k=input().split()
    n,k=int(n),int(k)
    #n=int(input())
    arr=list(map(int,input().split()))
    s=sum(arr)
    ans=s%k
    print(ans)
    
            

