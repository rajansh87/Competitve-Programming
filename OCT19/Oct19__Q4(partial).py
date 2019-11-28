from collections import OrderedDict

def func(n,dataArray):
    x=dataArray[n]
    print("ans : ",x)
    i=1
    while(i*i<=n):
        if(n%i==0):
            if(n//i==i):
                dataArray[i]+=1
            else:
                dataArray[i]+=1
                dataArray[n//i]+=1
        i+=1
    return x
    

t=int(input())
for u in range(t):
    n=int(input())
    #n,k=input().split()
    #n,k=int(n),int(k)
    arr=list(map(int,input().split()))
    dic=OrderedDict()
    for i in range(max(arr)):
        dic[i+1]=0
    m=0
    for i in range(n):
        c=func(arr[i],dic)
        if(c>m):
            m=c
    print(m)
        
               
               



    
    
