T=input()
j=0
while(j<T):
    n=input()
    i=0
    while(i<=n/26):
        if(0<n and n<=2):
            print 1,'',0,'',0,'\n'
            break
        elif(2<n and n<=10):
            print 0,'',1,'',0,'\n'
            break
        elif(10<n and n<=26):
            print 0,'',0,'',1,'\n'
            break
        k=2**i
        if(26*i<n and n<=26*i+2):
            print k,'',0,'',0,'\n'
            break
        elif(26*i+2<n  and n<=26*i+10):
            print 0,'',k,'',0,'\n'
            break
        elif(26*i+10<n and n<=26*(i+1)):
            print 0,'',0,'',k,'\n'
            break
        i=i+1
    j=j+1
