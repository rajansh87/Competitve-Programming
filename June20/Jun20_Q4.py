tt=int(input())
for qwerty in range(tt):
    n=int(input())
    #n,k=map(int,input().split())
    #arr=list(map(int,input().split()))
    ans=0
    if n%2==0:
        while n%2==0:
            n//=2
    ans=(n-1)//2
    print(ans)
            
        

    

