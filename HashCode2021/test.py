"""
5 1 2 1
3 onion pepper olive
3 mushroom tomato basil
3 chicken mushroom pepper
3 tomato mushroom basil
2 chicken basil
pizza_ingre_count
"""
m,t2,t3,t4=map(int,input().split())
pizza=[]
pizza_ingre_count=[]
for ingredients in range(m):
    s=input()
    s=s.split()
    pizza_ingre_count.append(int(s[0]))
    temp=[]
    for i in s[1:]:
        if len(pizza)!=0:
            z=0
            for j in pizza:
                if i in j:
                    z=10
                    #print(i,' already in pizza')
                    break
            if z==0:
                #print('1unique ingredient ',i)
                temp.append(i)
        else:
            temp.append(i)
            #print('2unique ingredient ',i)
    if temp!=[]:
        pizza.append(temp)

ans=[]
p2,p3,p4=0,0,0
while m-4>=2:
    m-=4
    p4+=1
while m-3>=2:
    m-=3
    p3+=1
while m>0:
    p2+=1
    m-=2

print(p2+p3+p4)

while p2!=0:
    min1,min2,min3,min4,min5,min6=0,0,0,0,0,0
    ind1,ind2,ind3,ind4,ind5,ind6=0,0,0,0,0,0
    print(2,end=" ")
    
    min1,min2=sorted(pizza_ingre_count)[0:2]
    ind1=pizza_ingre_count.index(min1)
    ind2=pizza_ingre_count.index(min2)
    if ind1==ind2:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min1:
                if flag==0:
                    flag=1
                else:
                    flag=0
                    ind2=i
                    break
    print(min(ind1,ind2),max(ind1,ind2))
    if ind1!=ind2:
        if ind1>ind2:
            pizza_ingre_count.pop(ind1)
            pizza_ingre_count.pop(ind2)
    else:
        if ind1==ind2+1:
            pizza_ingre_count.pop(ind2)
            pizza_ingre_count.pop(ind2)
        if ind2==ind1+1:
            pizza_ingre_count.pop(ind1)
            pizza_ingre_count.pop(ind1)
        
    p2-=1
    
    
mi5=0
in5=0
while p3!=0:
    print(3,end=" ")
    mi5,in5=0,0
    min3,min4,mi5=sorted(pizza_ingre_count)[2:5]
    ind3=pizza_ingre_count.index(min3)
    ind4=pizza_ingre_count.index(min4)
    in5=pizza_ingre_count.index(mi5)
    if ind3==ind4:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min3:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                else:
                    flag=0
                    ind4=i
                    break
    if ind3==in5:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min3:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                else:
                    flag=0
                    in5=i
                    break
    if ind4==in5:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min4:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                else:
                    flag=0
                    in5=i
                    break
    #print('z1',ind3,ind4)
    while ind3==ind1:
        ind3+=1
    while ind3==ind2:
        ind3+=1
    while ind4==ind1:
        ind4+=1
    while ind4==ind2:
        ind4+=1
    while ind4==ind3:
        ind4+=1
    while in5==ind1:
        in5+=1
    while in5==ind2:
        in5+=1
    while in5==ind3:
        in5+=1
    while in5==ind4:
        in5+=1
    
    #print('z2',ind3,ind4)
    if ind3==min(ind3,ind4,in5):
        print(ind3,end=" ")
        if ind4==min(ind4,in5):
            print(ind4,in5)
        else:
            print(in5,ind4)
    elif ind4==min(ind3,ind4,in5):
        print(ind4,end=" ")
        if ind3==min(ind3,in5):
            print(ind3,in5)
        else:
            print(in5,ind3)
    else:
        print(in5,end=" ")
        if ind3==min(ind3,ind4):
            print(ind3,ind4)
        else:
            print(ind4,ind3)
    if ind3!=ind4 and ind3!=in5 and ind4!=in5:
        if ind3==max(ind3,ind4,in5):
            pizza_ingre_count.pop(ind3)
            if ind4==max(ind4,in5):
                pizza_ingre_count.pop(ind4)
                pizza_ingre_count.pop(in5)
            else:
                pizza_ingre_count.pop(in5)
                pizza_ingre_count.pop(ind4)
        elif ind4==max(ind3,ind4,in5):
            pizza_ingre_count.pop(ind4)
            if ind3==max(ind3,in5):
                pizza_ingre_count.pop(ind3)
                pizza_ingre_count.pop(in5)
            else:
                pizza_ingre_count.pop(in5)
                pizza_ingre_count.pop(ind3)
        else:
            pizza_ingre_count.pop(in5)
            if ind3==max(ind3,ind4):
                pizza_ingre_count.pop(ind3)
                pizza_ingre_count.pop(ind4)
            else:
                pizza_ingre_count.pop(ind4)
                pizza_ingre_count.pop(ind3)
    else:
        if ind3==ind4+1:
            pizza_ingre_count.pop(ind4)
            pizza_ingre_count.pop(ind4)
        if ind3==in5+1:
            pizza_ingre_count.pop(in5)
            pizza_ingre_count.pop(in5)
        if ind4==ind3+1:
            pizza_ingre_count.pop(ind3)
            pizza_ingre_count.pop(ind3)
        if ind4==in5+1:
            pizza_ingre_count.pop(in5)
            pizza_ingre_count.pop(in5)
        if in5==ind4+1:
            pizza_ingre_count.pop(ind4)
            pizza_ingre_count.pop(ind4)
        if in5==ind3+1:
            pizza_ingre_count.pop(ind3)
            pizza_ingre_count.pop(ind3)
                
    p3-=1
        
mi7,mi8=0,0
in7,in8=0,0
while p4!=0:
    mi7,mi8=0,0
    in7,in8=0,0
    print(4,end=" ")
    min5,min6,mi7,mi8=sorted(pizza_ingre_count,reverse=True)[0:4]
    ind5=pizza_ingre_count.index(min5)
    ind6=pizza_ingre_count.index(min6)
    in7=pizza_ingre_count.index(mi7)
    in8=pizza_ingre_count.index(mi8)
    if ind5==ind6:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min5:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                elif flag==2:
                    flag=3
                else:
                    flag=0
                    ind6=i
                    break
    if ind5==in7:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min5:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                elif flag==2:
                    flag=3
                else:
                    flag=0
                    in7=i
                    break
    if ind5==in8:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min5:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                elif flag==2:
                    flag=3
                else:
                    flag=0
                    in8=i
                    break
    if ind6==in7:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min6:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                elif flag==2:
                    flag=3
                else:
                    flag=0
                    in7=i
                    break
    if ind6==in8:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==min6:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                elif flag==2:
                    flag=3
                else:
                    flag=0
                    in8=i
                    break
    if in7==in8:
        flag=0
        for i in range(len(pizza_ingre_count)):
            if pizza_ingre_count[i]==mi7:
                if flag==0:
                    flag=1
                elif flag==1:
                    flag=2
                elif flag==2:
                    flag=3
                else:
                    flag=0
                    in8=i
                    break
                
    while ind5==ind1:
        ind5+=1
    while ind5==ind2:
        ind5+=1
    while ind5==ind3:
        ind5+=1
    while ind5==ind4:
        ind5+=1
    while ind5==ind4:
        ind5+=1
    
    while ind6==ind1:
        ind6+=1
    while ind6==ind2:
        ind6+=1
    while ind6==ind3:
        ind6+=1
    while ind6==ind4:
        ind6+=1
    while ind6==ind5:
        ind6+=1

    while in7==ind1:
        in7+=1
    while in7==ind2:
        in7+=1
    while in7==ind3:
        in7+=1
    while in7==ind4:
        in7+=1
    while in7==ind5:
        in7+=1
    while in7==ind6:
        in7+=1

    while in8==ind1:
        in8+=1
    while in8==ind2:
        in8+=1
    while in8==ind3:
        in8+=1
    while in8==ind4:
        in8+=1
    while in8==ind5:
        in8+=1
    while in8==ind6:
        in8+=1
    while in8==in7:
        in8+=1

    if ind5==min(ind5,ind6,in7,in8):
        print(ind5,end=" ")
        if ind6==min(ind6,in7,in8):
            print(ind6,end=" ")
            if in7==min(in7,in8):
                print(in7,in8)
            else:
                print(in8,in7)
        elif in7==min(ind6,in7,in8):
            print(in7,end=" ")
            if ind6==min(ind6,in8):
                print(ind6,in8)
            else:
                print(in8,ind6)
        else:
            print(in8,end=" ")
            if ind6==min(ind6,in7):
                print(ind6,in7)
            else:
                print(in7,ind6)
    elif ind6==min(ind5,ind6,in7,in8):
        print(ind6,end=" ")
        if ind5==min(ind5,in7,in8):
            print(ind5,end=" ")
            if in7==min(in7,in8):
                print(in7,in8)
            else:
                print(in8,in7)
        elif in7==min(ind5,in7,in8):
            print(in7,end=" ")
            if ind5==min(ind5,in8):
                print(ind5,in8)
            else:
                print(in8,ind5)
        else:
            print(in8,end=" ")
            if ind5==min(ind5,in7):
                print(ind5,in7)
            else:
                print(in7,ind5)
    elif in7==min(ind5,ind6,in7,in8):
        print(in7,end=" ")
        if ind5==min(ind5,ind6,in8):
            print(ind5,end=" ")
            if ind6==min(ind6,in8):
                print(ind6,in8)
            else:
                print(in8,ind6)
        elif ind6==min(ind5,ind6,in8):
            print(ind6,end=" ")
            if ind5==min(ind5,in8):
                print(ind5,in8)
            else:
                print(in8,ind5)
        else:
            print(in8,end=" ")
            if ind5==min(ind5,ind6):
                print(ind5,ind6)
            else:
                print(ind6,ind5)
    else:
        print(in8,end=" ")
        if ind5==min(ind5,ind6,in7):
            print(ind5,end=" ")
            if ind6==min(ind6,in7):
                print(ind6,in7)
            else:
                print(in7,ind6)
        elif ind6==min(ind5,ind6,in7):
            print(ind6,end=" ")
            if ind5==min(ind5,in7):
                print(ind5,in7)
            else:
                print(in7,ind5)
        else:
            print(in7,end=" ")
            if ind5==min(ind5,ind6):
                print(ind5,ind6)
            else:
                print(ind6,ind5)
    if ind5!=ind6 and ind5!=in7 and ind5!=ind8 and ind6!=in7 and ind6!=in8 and in7!=in8:
        pizza_ingre_count.pop(ind5)
        pizza_ingre_count.pop(ind6)
        pizza_ingre_count.pop(in7)
        pizza_ingre_count.pop(in8)

        if ind5==max(ind6,in7,in8,ind5):
            pizza_ingre_count.pop(ind5)
            if ind6==max(ind6,in7,in8):
                pizza_ingre_count.pop(ind6)
                if in7==max(in7,in8):
                    pizza_ingre_count.pop(in7)
                    pizza_ingre_count.pop(in8)
                else:
                    pizza_ingre_count.pop(in8)
                    pizza_ingre_count.pop(in7)
            elif in7==max(ind6,in7,in8):
                pizza_ingre_count.pop(in7)
                if ind6==max(ind6,in8):
                    pizza_ingre_count.pop(ind6)
                    pizza_ingre_count.pop(in8)
                else:
                    pizza_ingre_count.pop(in8)
                    pizza_ingre_count.pop(ind6)
            elif in8==max(ind6,in7,in8):
                pizza_ingre_count.pop(in8)
                if ind6==max(ind6,in7):
                    pizza_ingre_count.pop(ind6)
                    pizza_ingre_count.pop(in7)
                else:
                    pizza_ingre_count.pop(in7)
                    pizza_ingre_count.pop(ind6)
        elif ind6==max(ind6,in7,in8,ind5):
            pizza_ingre_count.pop(ind6)
            if ind5==max(ind5,in7,in8):
                pizza_ingre_count.pop(ind5)
                if in7==max(in7,in8):
                    pizza_ingre_count.pop(in7)
                    pizza_ingre_count.pop(in8)
                else:
                    pizza_ingre_count.pop(in8)
                    pizza_ingre_count.pop(in7)
            elif in7==max(ind5,in7,in8):
                pizza_ingre_count.pop(in7)
                if ind5==max(ind5,in8):
                    pizza_ingre_count.pop(ind5)
                    pizza_ingre_count.pop(in8)
                else:
                    pizza_ingre_count.pop(in8)
                    pizza_ingre_count.pop(ind5)
            elif in8==max(ind5,in7,in8):
                pizza_ingre_count.pop(in8)
                if ind5==max(ind5,in7):
                    pizza_ingre_count.pop(ind5)
                    pizza_ingre_count.pop(in7)
                else:
                    pizza_ingre_count.pop(in7)
                    pizza_ingre_count.pop(ind5)
        elif in7==max(ind6,in7,in8,ind5):
            pizza_ingre_count.pop(in7)
            if ind5==max(ind5,ind6,in8):
                pizza_ingre_count.pop(ind5)
                if ind6==max(ind6,in8):
                    pizza_ingre_count.pop(ind6)
                    pizza_ingre_count.pop(in8)
                else:
                    pizza_ingre_count.pop(in8)
                    pizza_ingre_count.pop(ind6)
            elif ind6==max(ind5,ind6,in8):
                pizza_ingre_count.pop(ind6)
                if ind5==max(ind5,in8):
                    pizza_ingre_count.pop(ind5)
                    pizza_ingre_count.pop(in8)
                else:
                    pizza_ingre_count.pop(in8)
                    pizza_ingre_count.pop(ind5)
            elif in8==max(ind5,ind6,in8):
                pizza_ingre_count.pop(in8)
                if ind5==max(ind5,ind6):
                    pizza_ingre_count.pop(ind5)
                    pizza_ingre_count.pop(ind6)
                else:
                    pizza_ingre_count.pop(ind6)
                    pizza_ingre_count.pop(ind5)
        elif in8==max(ind6,in7,in8,ind5):
            pizza_ingre_count.pop(in8)
            if ind5==max(ind5,ind6,in7):
                pizza_ingre_count.pop(ind5)
                if ind6==max(ind6,in7):
                    pizza_ingre_count.pop(ind6)
                    pizza_ingre_count.pop(in7)
                else:
                    pizza_ingre_count.pop(in7)
                    pizza_ingre_count.pop(ind6)
            elif ind6==max(ind5,ind6,in7):
                pizza_ingre_count.pop(ind6)
                if ind5==max(ind5,in7):
                    pizza_ingre_count.pop(ind5)
                    pizza_ingre_count.pop(in7)
                else:
                    pizza_ingre_count.pop(in7)
                    pizza_ingre_count.pop(ind5)
            elif in7==max(ind5,ind6,in7):
                pizza_ingre_count.pop(in7)
                if ind5==max(ind5,ind6):
                    pizza_ingre_count.pop(ind5)
                    pizza_ingre_count.pop(ind6)
                else:
                    pizza_ingre_count.pop(ind6)
                    pizza_ingre_count.pop(ind5)  
        
    else:
        if ind5==ind6+1:
            pizza_ingre_count.pop(ind6)
            pizza_ingre_count.pop(ind6)
        if ind5==in7+1:
            pizza_ingre_count.pop(in7)
            pizza_ingre_count.pop(in7)
        if ind5==in8+1:
            pizza_ingre_count.pop(in8)
            pizza_ingre_count.pop(in8)
        if ind6==ind5+1:
            pizza_ingre_count.pop(ind5)
            pizza_ingre_count.pop(ind5)
        if ind6==in7+1:
            pizza_ingre_count.pop(in7)
            pizza_ingre_count.pop(in7)
        if ind6==in8+1:
            pizza_ingre_count.pop(in8)
            pizza_ingre_count.pop(in8)        
        if in7==ind6+1:
            pizza_ingre_count.pop(ind6)
            pizza_ingre_count.pop(ind6)
        if in7==ind5+1:
            pizza_ingre_count.pop(ind5)
            pizza_ingre_count.pop(ind5)
        if in7==in8+1:
            pizza_ingre_count.pop(in8)
            pizza_ingre_count.pop(in8)

                
    p3-=1
    
    
    
    

















