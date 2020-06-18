tt=int(input())
for qwerty in range(tt):
    n=int(input())
    #n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    x1,x2,x3=0,0,0
    z=1
    for i in range(n):
        if arr[i]==5:
            x1+=1
        elif arr[i]==10:
            if x1>0:
                x1-=1
                x2+=1
            else:
                z=0
                break
        else:
            if arr[i]==15:
                if x2>0:
                    x2-=1
                    x3+=1
                elif x1>=2:
                    x1-=2
                    x3+=1
                else:
                    z=0
                    break

    if z==0:
        print("NO")
    else:
        print("YES")
            
    
            
        

    

