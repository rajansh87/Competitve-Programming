import numpy as np
tt=int(input())
for qwerty in range(tt):
    #n=int(input())
    ans="Case #"
    ans+=str(qwerty+1)+": "
    space=" "
    #n,d=map(int,input().split())
    #arr=list(map(int,input().split()))
    s=input()
    pos=[1,1]

    stack=[]
    j=0
    exp=""
    for i in s:
        if i!=")":
            stack.append(i)
        else:
            exp=""
            while(stack[-1]!="("):
                exp=stack.pop()+exp
            stack.pop()
            exp*=int(stack.pop())
            stack+=list(exp)
    st=""
    for i in stack:
        st+=i
    #print(st)
    for i in st:
        if i=="S":
            pos[1]+=1
        elif i=="N":
            pos[1]-=1
        elif i=="E":
            pos[0]+=1
        elif i=="W":
            pos[0]-=1
    if pos[0]<1:
        val=0-pos[0]
        pos[0]=10**9-val
    elif pos[0]>10**9:
        val=pos[0]-10**9
        pos[0]=val
    if pos[1]<1:
        val=0-pos[1]
        pos[1]=10**9-val
    elif pos[1]>10**9:
        val=pos[1]-10**9
        pos[1]=val
            

    ans+=str(pos[0])+" "+str(pos[1])




    
    
    



    print(ans)   
