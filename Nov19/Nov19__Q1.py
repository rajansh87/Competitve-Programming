t=int(input())
for r in range(t):
    #n,query=input().split(" ")
    #n,query=int(n),int(query)
    #n=int(input())
    #n,m=input().split(" ")
    #n,m=int(n),int(m)
    n=int(input())
    arr=[]
    for w in range(n):
        s=input()
        arr.append(s)
    
    c=0
    m=0
    s=""
    for i in range(n-1):
        s=""
        for j in range(10):
            if(arr[i][j]==arr[i+1][j]):
                s+='0'
            else:
                s+='1'
        arr[i+1]=s
    s=""
    s+=arr[n-1]    
    #print("s:",s)
    c=0
    for i in range(10):
        if(s[i]=="1"):
            c+=1
    print(c)
                
        
    
            
        
