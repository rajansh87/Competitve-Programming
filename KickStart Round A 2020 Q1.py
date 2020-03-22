tt=int(input())
for qwerty in range(tt):
    ans="Case #"
    #n=int(input())
    n,b=input().split()
    n,b=int(n),int(b)
    arr=list(map(int,input().split()))
    c=0
    arr.sort()
    s=0
    for i in range(n):
        s+=arr[i]
        if(s<=b):
            c+=1
    ans+=str(qwerty+1)+":"
    print(ans,c,sep=" ")

            
    
        

