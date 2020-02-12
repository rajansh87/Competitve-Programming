tt=int(input())
total=0
for qwerty in range(tt):
    #n=int(input())
    #arr = [ [ 0 for i in range(4) ] for j in range(4) ]
##    for request in range(n):
##        m,t=input().split()
##        m,t=(m),int(t)
##        arr[ord(m)-ord("A")][(t//3)-1]+=1
##    main=[]
    s=input()
    c=0
    s2=""
    ind1=-1
    ind2=-1
    i=0
    ind1=s.find("1")
    ind2=s[::-1].find("1")
    ind2=len(s)-ind2-1
    s2=s[ind1:ind2+1]
    if(s2.count("0")==len(s2)):
        print(0)
    else:
        print(s2.count("0"))
        
            






