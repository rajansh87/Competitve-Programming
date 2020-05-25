import math as mt
tt=int(input())
for qwerty in range(tt):
    #n=input()
    #n=int(n)
    #n,k=map(int,input().split()) 
    #arr=list(map(int,input().split()))       
    x,y,left,right=input().split()
    x,y,left,right=int(x),int(y),int(left),int(right)

    calculatedValue=x|y

    ans=0

    if x>y and y==0:
        ans=0

    elif y>x and x==0:

        ans=0

    elif right>=calculatedValue:

        ans=calculatedValue

    else:

        if x>y:
            ma=x
        else:
            ma=y

        power=int(mt.log(ma))+1

        ans=(2**power)
        
        ans-=1

    print(ans)
        
