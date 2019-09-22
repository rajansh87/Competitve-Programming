

t=int(input())
for u in range(t):
    s=input()
    c=0
    i=0
    j=len(s)-1
    while(i<j):
        if(s[i]==")"):
            i+=1
        elif(s[j]=="("):
            j-=1
        else:
            c+=2
            i+=1
            j-=1
    print(c)
    
                    
            
                
                
            
