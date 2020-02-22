import calendar
def day(dd,mm,yy):
    arr=[0,3,2,5,0,3,5,1,4,6,2,4]
    if(mm<3):
        yy-=1
    v=(yy+(yy//4) -(yy//100)+(yy//400)+arr[mm-1]+dd)%7
    return v      #return day of week
tt=int(input())
for qwerty in range(tt):
    #n=int(input())
    #data=[0]*400
    m1,y1=input().split()
    m1,y1=int(m1),int(y1)
    #arr=list(map(int,input().split()))
    m2,y2=input().split()
    m2,y2=int(m2),int(y2)
    if(m1>2):
        y1+=1
    if(m2<2):
        y2-=1
    val=0
    val=((y2-y1)//400)*101
    
    y1=y1+(((y2-y1)//400)*400)
    for i in range(y1,y2+1):      #main calc
        c=0
        da=day(1,2,i)
        if(calendar.isleap(i)):      #leap
            c=1
        if(da==6):
            val+=1
        elif(da==0 and c!=1):
            val+=1
    print(val)

    
    








    
    
    
