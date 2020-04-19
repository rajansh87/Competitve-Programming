import numpy as np
tt=int(input())
for qwerty in range(tt):
##use dictionary to store multiples

    #n=int(input())
    ans="Case #"
    ans+=str(qwerty+1)+": "
    space=" "
    n,d=map(int,input().split())
    arr=list(map(int,input().split()))
    i=len(arr)-1
    while(1):
        if i==-1:
            break
        x=d%arr[i]
        if x==0:
            i-=1
        else:
            d-=x
            
        
        
    ans+=str(d)



    print(ans)   
##
##import numpy as np
##tt=int(input())
##for qwerty in range(tt):
####use dictionary to store multiples
##
##    #n=int(input())
##    ans="Case #"
##    ans+=str(qwerty+1)+": "
##    space=" "
##    n,d=map(int,input().split())
##    arr=list(map(int,input().split()))
##    multiples=[]
##    for i in range(n):
##        val=arr[i]*(d//arr[i])
##        multiples.append(val)
##    z=0
##    while(1):
##        for i in range(n-1):
##            if multiples[i]>multiples[i+1]:
##                val=arr[i]*((multiples[i]-1)//arr[i])
##                multiples[i]=val
##            #print("A")
##        brr=multiples.copy()
##        brr.sort()
##        if brr==multiples:
##            break
##        #print("B")
##    for i in range(n-1,0,-1):
##        while multiples[i]>multiples[i-1]:
##            val=arr[i]*(multiples[i-1]//arr[i])
##            multiples[i]=val
##            #print("A")
##        multiples[i]+=arr[i]
##        #print("B")
##    ans+=str(min(multiples))
##    
##    
##
##
##
##    print(ans)   
