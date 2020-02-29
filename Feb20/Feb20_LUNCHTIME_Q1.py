def toss(arr):
    for i in range(len(arr)):
        arr[i]=abs(arr[i]-1)
        
tt=int(input())
for qwerty in range(tt):
    n,k=input().split()
    n,k=int(n),int(k)
    #n=int(input())
    #arr=list(map(int,input().split()))
    s=input()
    s=s.replace(" ","")
    arr=list(s)
    for i in range(n):
        if(arr[i]=="H"):
            arr[i]=1
        else:
            arr[i]=0
            
    for z in range(k):
        #print(arr)
        p=arr.pop(len(arr)-1)
        #print(" pop : ",p)
        if(p==1):
            toss(arr)
        
    c=arr.count(1)
    print(c)
    
