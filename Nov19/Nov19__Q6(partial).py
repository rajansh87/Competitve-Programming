import math 
  
def isPerfectSquare(x): 
    sr = math.sqrt(x)  
    return ((sr - math.floor(sr)) == 0) 
t=int(input())
for r in range(t):
    #x,y=input().split(" ")
    #x,y=int(x),int(y)
    #arr=list(map(int,input().split()))
    n=int(input())
    if(n==1):
        print(1)
    else:
        x=int("1"*(n))
        y=int("9"*(n))+1
        s=0
        z=0
        k=0
        for i in range(x,y):
            a=str(i)
            if("0" not in a):
                k=0
                for j in range(len(a)):
                    k=k+((int(a[j]))*(int(a[j])))
                if(isPerfectSquare(k)):
                    print(i)
                    z=55
                    break
        if(z==0):
            print(-1)
            
                
            
        
