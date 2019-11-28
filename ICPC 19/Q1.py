t=int(input())
for u in range(t):
    #n,k=input().split(" ")
    #n,k=int(n),int(k)
    #arr=list(map(int,input().split()))
    num=input()
    a=[]
    n=len(num)
    for i in range(n):
        a.append(int(num[i]))
    s=0
    arr=[]
    for i in range(n):
        arr.append(0)
    for i in range(n):
        #b=a.copy()
        s=""
        x=a.pop(i)
        s=str(a)
        s=s.replace("[","")
        s=s.replace("]","")
        s=s.replace(",","")
        s=s.replace(" ","")
        arr[i]=int(s)        
        a.insert(i,x)
    print(min(arr))
            
    

        
               
               



    
    

               
               



    
    
