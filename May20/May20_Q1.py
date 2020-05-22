def RightShiftOperation(arr,ind1,ind2,ind3):
    arr[ind1],arr[ind2],arr[ind3]=arr[ind3],arr[ind1],arr[ind2]
    

tt=int(input())
for qwerty in range(tt):
    #n=int(input())
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    brr=arr.copy()
    brr.sort()
    dic={}
    for i in range(n):
        dic[brr[i]]=i
    result=0
    f,s=-1,-1
    i=0
    n1,n2,n3=0,0,0
    crr=[]
    while(i<n):
        if arr[i]==brr[i] or s==i:
            i+=1
            continue
        n1=i
        n2=dic[arr[n1]]
        n3=dic[arr[n2]]
        if n3==n1 and f==-1:
            f=n1
            s=n2
            i+=1
            continue
        elif n1==n3:
            n1=f
            n2=s
            n3=i
            f,s=-1,-1
        RightShiftOperation(arr,n1,n2,n3)
        result+=1
        crr.append([n1+1,[n2+1,n3+1]])
        if arr[n1]==brr[n1]:
            i+=1
        if result>k:
            result=-1
            break
    if f!=-1:
        result=-1
    if result<=k and result!=-1:
        print(result)
        for i in crr:
            print(i[0],i[1][0],i[1][1])
    else:
        print(-1)
        
        
            
            
                
            
