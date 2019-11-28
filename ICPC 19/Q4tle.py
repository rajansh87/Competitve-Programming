t=int(input())
for u in range(t):
    n,k=input().split(" ")
    n,k=int(n),int(k)
    #arr=list(map(int,input().split()))
    s=input()
    arr=[]
    for i in range(k):
        y=[]
        x=input()
        for i in range(len(x)):
            y.append(x[i])
            
        arr.append(y)
    ans=[]
    for i in range(len(s)):
        for j in range(len(arr)):
            if(s[i] in arr[j]):
                ans.append(j+1)
                break
                
    answer=""
    for i in range(len(ans)):
        answer+=str(ans[i])
        answer+=" "
    print(answer)
    
        
        
    
            
    

        
               
               



    
    

               
               



    
    
