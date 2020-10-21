tt=int(input())
for qwerty in range(tt):
    ans="Case #"
    ans+=str(qwerty+1)+":"
    #n=int(input())
    #n,b=input().split()
    #n,b=int(n),int(b)
    #arr=list(map(int,input().split()))
    s=input()
    pt=1
    dic=dict()
    for i in range(len(s)-4):
        if s[i:i+4]=="KICK":
            dic[pt]=0
            pt+=1
        if i<=len(s)-5:
            if s[i:i+5]=="START":
                for key in dic:
                    dic[key]+=1
    final=sum(dic.values())
    print(ans,final,sep=" ")

######
tt=int(input())
for qwerty in range(tt):
    ans="Case #"
    ans+=str(qwerty+1)+":"
    #n=int(input())
    #n,b=input().split()
    #n,b=int(n),int(b)
    #arr=list(map(int,input().split()))
    s=input()
    pt=1
    dic=dict()
    qt=1
    dic2=dict()
    c=0
    low=0
    high=len(s)-1-5
    kick,start=False,False
    st=""
    for i in range(len(s)-4):
    	if s[i:i+4]=="KICK":
    		st+='1'
    	if s[i:i+5]=="START":
    		st+='0'
    for i in range(len(st)):
    	if st[i]=="1":
    		c+=st[i+1::].count("0")
    
  
    #final=sum(dic.values())
    print(ans,c,sep=" ")

            
    
        

            
    
        

