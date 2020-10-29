#tt=int(input())
#for qwerty in range(tt):
    #n=int(input())
    #a,b=map(int,input().split())
    #arr=list(map(int,input().split()))

n=int(input())
arr=list(map(int,input().split()))
a,b,ans=[0 for i in range(n)],[0 for i in range(n)],[0 for i in range(n)]

a[0]=arr[0]

for i in range(1,n):
    a[i]=arr[i]+a[i-1]//2

b[n-1]=arr[n-1]

for i in range(n-2,-1,-1):
    b[i]=arr[i]+b[i+1]//2


ans[0]=max(a[0],b[0])
ans[n-1]=max(a[n-1],b[n-1])

for i in range(1,n-1):
    ans[i]=arr[i]+a[i-1]//2+b[i+1]//2

print(max(ans))
            
