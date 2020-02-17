t=int(input())
for qwerty in range(t):
    #n,m,k=input().split()
    #n,m,k=int(n),int(m),int(k)
    n=int(input())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))        
    arr1.sort()
    arr2.sort()
    s=0
    for i in range(n):
        s+=min(arr1[i],arr2[i])
    print(s)
                        
                        

