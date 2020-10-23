import numpy as np
tt=int(input())
for qwerty in range(tt):
    ans="Case #"
    ans+=str(qwerty+1)+":"
    n=int(input())
    #n,b=input().split()
    #n,b=int(n),int(b)
    #arr=list(map(int,input().split()))
    arr=[]
    temp=[]
    for i in range(n):
        temp=list(map(int,input().split()))
        arr.append(temp)
        temp=[]
    diagonals=[]
    m=2*n-3
    pt=0
    qt=0
    for i in range(n):
        a1=list(np.diag(arr,k=pt))
        a2=list(np.diag(arr,k=qt))
        if a1==a2:
        	diagonals.append(a1)
        else:
        	diagonals.append(a1)
        	diagonals.append(a2)
        pt+=1
        qt-=1
        #diagonals.append(np.diag(arr,k=i+1))
    #print(diagonals)
    ma=0
    for i in diagonals:
    	val=sum(i)
    	#print(i,val)
    	if val>ma:
    		ma=val
    #print(ma)
    	
    
    
    
    
  
    #final=sum(dic.values())
    print(ans,ma,sep=" ")

            
    
        

            
    
        

