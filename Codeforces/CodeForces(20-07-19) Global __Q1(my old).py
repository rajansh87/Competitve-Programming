n=int(input())
a=list(map(int,input().split()))
k=0
b=[]
p=0
c=a.copy()
index=[]
index.append(1)
b.append(a[0])
major=sum(a)//2
if(a[0]>major):
    print(1)
    print(1)
    k=99
else:
    val=a[0]
    a.pop(0)
    a.sort()
    a.reverse()
    for i in range(0,n-1):
        if(a[i]<=val//2):
            b.append(a[i])
            #index.append(n-1-i)
        if(sum(b)>major):
            print(len(b))
            #print(index)
            
            k=99
            p=88
            break
    
    if(p==88):
        a=[]
        j=0
        for i in range(n):
            if(j<len(b)):
                a.append((c.index(b[j]))+1)
                c[c.index(b[j])]=100000000000000000
                j+=1
            else:
                break
        print(*a,sep=" ")
        
    
 
if(k==0):
    print(0)
