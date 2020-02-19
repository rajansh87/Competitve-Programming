tt=int(input())
totalprofit=0
for qwerty in range(tt):
    n=int(input())
    #arr=list(map(int,input().split()))
    x3=[0]*4
    x6=[0]*4
    x9=[0]*4
    x12=[0]*4
    for request in range(n):
        m,t=input().split()
        m,t=(m),int(t)
        if(m=="A" and t==3):
            x3[0]+=1
        elif(m=="B" and t==3):
            x3[1]+=1
        elif(m=="C" and t==3):
            x3[2]+=1
        elif(m=="D" and t==3):
            x3[3]+=1
            
        if(m=="A" and t==6):
            x6[0]+=1
        elif(m=="B" and t==6):
            x6[1]+=1
        elif(m=="C" and t==6):
            x6[2]+=1
        elif(m=="D" and t==6):
            x6[3]+=1
            
        if(m=="A" and t==9):
            x9[0]+=1
        elif(m=="B" and t==9):
            x9[1]+=1
        elif(m=="C" and t==9):
            x9[2]+=1
        elif(m=="D" and t==9):
            x9[3]+=1
            
        if(m=="A" and t==12):
            x12[0]+=1
        elif(m=="B" and t==12):
            x12[1]+=1
        elif(m=="C" and t==12):
            x12[2]+=1
        elif(m=="D" and t==12):
            x12[3]+=1

##    print("12  3  6  9")
##    
##    for i in range(4):
##        print(x12[i],x3[i],x6[i],x9[i],sep="  ")
##

    show1=max(x12+x3+x6+x9)
    ind=-1
    if(show1 in x12):
        ind=x12.index(show1)
        x12=[-1]*4
    elif(show1 in x3):
        ind=x3.index(show1)
        x3=[-1]*4
    elif(show1 in x6):
        ind=x6.index(show1)
        x6=[-1]*4
    elif(show1 in x9):
        ind=x9.index(show1)
        x9=[-1]*4
        
    x12[ind]=-1
    x3[ind]=-1
    x6[ind]=-1
    x9[ind]=-1


    show2=max(x12+x3+x6+x9)
    ind=-1
    if(show2 in x12):
        ind=x12.index(show2)
        x12=[-1]*4
    elif(show2 in x3):
        ind=x3.index(show2)
        x3=[-1]*4
    elif(show2 in x6):
        ind=x6.index(show2)
        x6=[-1]*4
    elif(show2 in x9):
        ind=x9.index(show2)
        x9=[-1]*4

    x12[ind]=-1
    x3[ind]=-1
    x6[ind]=-1
    x9[ind]=-1

    show3=max(x12+x3+x6+x9)
    ind=-1
    if(show3 in x12):
        ind=x12.index(show3)
        x12=[-1]*4
    elif(show3 in x3):
        ind=x3.index(show3)
        x3=[-1]*4
    elif(show3 in x6):
        ind=x6.index(show3)
        x6=[-1]*4
    elif(show3 in x9):
        ind=x9.index(show3)
        x9=[-1]*4
        
    x12[ind]=-1
    x3[ind]=-1
    x6[ind]=-1
    x9[ind]=-1

    show4=max(x12+x3+x6+x9)
    ind=-1
    if(show4 in x12):
        ind=x12.index(show4)
        x12=[-1]*4
    elif(show4 in x3):
        ind=x3.index(show4)
        x3=[-1]*4
    elif(show4 in x6):
        ind=x6.index(show4)
        x6=[-1]*4
    elif(show4 in x9):
        ind=x9.index(show4)
        x9=[-1]*4

    x12[ind]=-1
    x3[ind]=-1
    x6[ind]=-1
    x9[ind]=-1
    

    money=0
    if(show1==0 and show2==0 and show3==0 and show4==0):
        money=-400
    
    if(show1==0 and show2==0 and show3==0 and show4!=0):
        money=-300+show4*25

    if(show1==0 and show2==0 and show3!=0 and show4==0):
        money=-300+show3*50

    if(show1==0 and show2==0 and show3!=0 and show4!=0):
        money=-200+show3*50+show4*25

    if(show1==0 and show2!=0 and show3==0 and show4==0):
        money=-300+show2*75

    if(show1==0 and show2!=0 and show3==0 and show4!=0):
        money=-200+show2*75+show4*25

    if(show1==0 and show2!=0 and show3!=0 and show4==0):
        money=-200+show2*75+show3*50

    if(show1==0 and show2!=0 and show3!=0 and show4!=0):
        money=-100+show2*75+show3*50+show4*25

    if(show1!=0 and show2==0 and show3==0 and show4==0):
        money=-300+show1*100

    if(show1!=0 and show2==0 and show3==0 and show4!=0):
        money=-200+show1*100+show4*25

    if(show1!=0 and show2==0 and show3!=0 and show4==0):
        money=-200+show1*100+show3*50

    if(show1!=0 and show2==0 and show3!=0 and show4!=0):
        money=-100+show1*100+show3*50+show4*25

    if(show1!=0 and show2!=0 and show3==0 and show4==0):
        money=-200+show1*100+show2*75

    if(show1!=0 and show2!=0 and show3==0 and show4!=0):
        money=-100+show1*100+show2*75+show4*25

    if(show1!=0 and show2!=0 and show3!=0 and show4==0):
        money=-100+show1*100+show2*75+show3*50

    if(show1!=0 and show2!=0 and show3!=0 and show4!=0):
        money=show1*100+show2*75+show3*50+show4*25
 
    
        
    
    print(money)
    totalprofit+=money
print(totalprofit)


















        
    
   
