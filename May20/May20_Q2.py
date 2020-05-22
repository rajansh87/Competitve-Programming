tt=int(input())
for qwerty in range(tt):
    n=input()
    n=int(n)
    #n,k=map(int,input().split()) 
    arr=list(map(int,input().split()))

    result,temp=0,0
    maximum,minimum=0,999999999999999999999999+1
    
    it=0
  
    while(it<n):
        
        if(it==0 or arr[it]-temp<=2):
            result=result+1
            
        elif(arr[it]-temp>2):
            if(result<minimum):
                minimum=result        
                
            if(result>maximum):
                maximum=result
            result=1
            
        temp=arr[it]
        
        it+=1
        
    if(result<minimum):
        minimum=result        
                
    if(result>maximum):
        maximum=result

    print(minimum,maximum,sep=" ")  
