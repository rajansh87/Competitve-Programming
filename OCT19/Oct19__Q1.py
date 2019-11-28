t=int(input())
for u in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=1
    #b=[0,0,0,0,0,0]
    #a=b+a
    #index=0
    for i in range(1,len(a)):
        if(i-5>=0):
            if(a[i]<min(a[i-5:i])):
               c+=1
               #print("a :  ",a[i])
        else:
            if(a[i]<min(a[0:i])):
               c+=1
               #print("a2 : ",a[i])
    print(c)
               
               



    
    
