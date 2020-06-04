#tt=int(input())
#for qwerty in range(tt):
    #n=input()
    #n=int(n)
    #n,k=map(int,input().split()) 
    #arr=list(map(int,input().split()))

b=[5,3,8]
g=[2,4,6]


n=len(b)

b.sort()
g.sort()
a=[0]*(2*n)
a[::2]=b
a[1::2]=g

arr=[0]*(2*n)
arr[::2]=g
arr[1::2]=b
ans=""

if a==sorted(a) or arr==sorted(arr):
    ans="YES"
else:
    ans="NO"



print(ans)
    
    


