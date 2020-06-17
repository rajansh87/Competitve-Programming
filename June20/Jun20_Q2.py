tt=int(input())
for qwerty in range(tt):
    #n=int(input())
    #n,k=map(int,input().split())
    #arr=list(map(int,input().split()))
    s=input()

    i=0
    ans=0
    while True:
        if (len(s)-1)<=i:
            break
        if s[i]!=s[i+1]:
            ans+=1
            i+=1
        if (len(s)-1)<=i:
            break
        i+=1
    print(ans)
        
    
            
        

    

