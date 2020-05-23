tt=int(input())
for qwerty in range(tt):
    #n=input()
    #n=int(n)
    #n,k=map(int,input().split()) 
    #arr=list(map(int,input().split()))
    n,q=map(int,input().split())
    givenstring=input()
    count=[0 for i in range(26+1)]
    for character in givenstring:
        count[ord(character)-ord("a")]+=1

    query=0
    while(query<q):   
        requiredValue=0
        myCount=int(input())        
        for it in range(0,26,1):
            if count[it]>myCount:
                requiredValue+=count[it]-myCount
                
        print(requiredValue)
        query+=1
        
