tt=int(input())
for qwerty in range(tt):
    n=int(input())
    #a,b,c,d=map(int,input().split())
    myteam=list(map(int,input().split()))
    opteam=list(map(int,input().split()))

    points=0

    myteam.sort()
    opteam.sort()
    z=0
    x=0
    while(1):
        z=0
        x=0
        #print("A")
        if len(myteam)!=0:
         #   print("B")
            if myteam[0]>opteam[0]:
          #      print("C")
                points+=1
                myteam.pop(0)
                opteam.pop(0)
                z+=1
            else:
           #     print("D")
                i=0
                while(myteam[i]<=opteam[0]):
                    i+=1
                points+=1
                for j in range(0,i+1):
                    myteam.pop(0)
                opteam.pop(0)
                z+=1
            if z!=1:
            #    print("E")
                x=66
                break
        else:
#            print("F")
            break
        if x==66:
 #           print("G")
            break
    print(points)
            
                
        
            
            

    

    
