
tt=int(input())
for qwerty in range(tt):
    #n=int(input())
    ans="Case #"
    ans+=str(qwerty+1)+":"
    

    #a,b=map(int,input().split())
    s=input()
    pattern="()"
    
    result=[]
    i=0
    if len(s)==1:
        if s=="0":
            result.append(s)
        else:
            result.append(pattern[0]*int(s)+s+pattern[1]*int(s))     
    else:
        while i<len(s):
            if s[i]!="0":
                if i<len(s)-1:
                    if s[i+1]!=s[i]:
                        result.append(pattern[0]*int(s[i])+s[i]+pattern[1]*int(s[i]))
                    else:
                        j=i+1
                        p=int(s[i])
                        temp=s[i]
                        while s[j]==s[i]:
                            j+=1
                            i+=1
                            temp+=s[i]
                            if j>=len(s):
                                break
                        #i+=1
                        result.append(pattern[0]*p+temp+pattern[1]*p)
                else:
                       
                    result.append(pattern[0]*int(s[i])+s[i]+pattern[1]*int(s[i]))
                    
            else:
                result.append(s[i])

                
            i+=1
                
    
        
    final=""
    for i in range(len(result)):
        final+=result[i]
    
    print(ans,final,sep=" ")   #final=ouput from code
