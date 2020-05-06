##tt=int(input())
##for qwerty in range(tt):
##    n=int(input())
##    a,b,c,d=map(int,input().split())
##    arr=list(map(int,input().split()))

n=int(input())
req=list(map(int,input().split()))
avail=list(map(int,input().split()))

c=0
i=0
c1=0
z=0
while(1):
    for i in range(n):
        if(avail[i]>=req[i]):
            c1+=1
        else:
            z=55
            break
    if z==55:
        break
    if c1==n:
        c+=1
        c1=0
        for i in range(n):
            avail[i]=avail[i]-req[i]

print(c)  
        
    
