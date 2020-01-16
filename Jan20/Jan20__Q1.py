t = int(input())
for q in range(t):
    #n,k=input().split()
    #n,k=int(n),int(k)
    #n,m,k=input().split()
    #n,m,k=int(n),int(m),int(k)
    #n=int(input())
    #n=int(input())
    #arr=list(map(int,input().split()))
    s,w1,w2,w3=input().split()
    s,w1,w2,w3=int(s),int(w1),int(w2),int(w3)
    c=0
    a=[w1,w2,w3]
    su=0
    brick=0
    if(w1<=s):
        if(w1+w2<=s):
            if(w1+w2+w3<=s):
                c=1
            else:
                c=2
        else:
            c=1
            if(w2<=s):
                if(w2+w3<=s):
                    c=2
                else:
                    c=3
            else:
                c=2
                if(w3<=s):
                    c=3
    print(c)
            
            
        
    
