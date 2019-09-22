import numpy


def func(arr,n):
    c=n//2
    sum1=numpy.zeros((n,n))
    score=numpy.zeros((n,n))
    temp=0
    sumscore=000000000000000000
    s=1000000000000000000
    v=0
    for i in range(n):
        temp=arr[i]
        sum1[i][i]=temp
    for i in range(0,n-1):
        sum1[i][i+1]=arr[i+1]+arr[i]
        score[i][i+1]=arr[i+1]+arr[i]
        
    for i in range(2,n):
        for j in range(0,n-i):
            sumscore=1000000000000000000
            s=1000000000000000000
            for k in range(0,i):
                v=int(score[j][j+k])+int(score[j+k+1][j+i])+int(sum1[j][j+k])+int(sum1[j+k+1][j+i])
                sumscore=min(sumscore,v)
                if(sumscore==v):
                    s=int(sum1[j][j+k])+int(sum1[j+k+1][j+i])
            score[j][j+i]=sumscore
            sum1[j][j+i]=s
    m=1000000000000000000;
    for i in range(0,c):
        m=min(int(score[i][i+c-1]),m)
    return m                                  


t=int(input())
for r in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(0,n):
        a.append(a[i])
    result=func(a,2*n)
    print(result)
    
