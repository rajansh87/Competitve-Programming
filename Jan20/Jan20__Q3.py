def checkandfindpalindromes(arr,i,j,n,m):
    c=0
    while(1):
        if((i-c>=0) and (i+c<n) and (j-c>=0) and (j+c<m)):
            if(((arr[i-c][j])==(arr[i+c][j])) and ((arr[i][j-c])==(arr[i][j+c]))):
                c+=1
            else:
                break
        else:
            break
    return c
    
                   


t = int(input())
for q in range(t):
    n,m=input().split()
    n,m=int(n),int(m)
    #n=int(input())
    #arr=list(map(int,input().split()))
    arr=[]
    temp=[]
    for i in range(n):
        temp=list(map(int,input().split()))
        #temp.insert(0,0)
        arr.append(temp)
        temp=[]
    x=0
    for i in range(n):
        for j in range(m):
            x+=checkandfindpalindromes(arr,i,j,n,m)

    print(x)















    
