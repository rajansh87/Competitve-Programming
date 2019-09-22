t=int(input())

for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mean1=0
    mean2=0
    s=0
    var=0
    arr=[]
    p=0
    if(len(a)==1):
        print(1)
    else:
        s=sum(a)
        mean1=s/n
        for i in range(n):
            var=s
            var=var-a[i]
            mean2=var/(n-1)
            if(mean1==mean2):
                arr.append(i+1)
                p=5

    
    if(p==0):
        print("Impossible")
    else:
        print(min(arr))
            
        
        
    
