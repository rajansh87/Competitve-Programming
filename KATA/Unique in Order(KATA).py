def unique_in_order(s):
    a=[]
    if(len(s)!=0):
        #s=input()
        i=1
        x=s[0]
        a=[]
        a.append(x)
        while(i<len(s)):
            if(x!=s[i]):
                x=s[i]
                a.append(x)
            i+=1
        #print(a)
        return a
    else:
        return a
        
