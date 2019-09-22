t=int(input())
for r in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  f=int(input())
  p=0
  d=10000000008
  pos=0
  for i in range(len(a)):
    if(a[i]<f):
      pos=i
      p+=1
      break
  q=0
  if(p==0):
    print("impossible")
  else:
    a.insert(pos,d)
    i=0
    while(len(a)!=2):
      if((a[(i+1)%len(a)]>100000) and ((i+1)%len(a)<=len(a))):
        a[i+1]=a[i+1]-a[i]
        i+=2
        i=i%len(a)
      else:
        if((i+1)%len(a)==0):
          a.remove(a[(i+1)%len(a)])
        else:
          a.remove(a[(i+1)%len(a)])
          i+=1
                
      i=i%len(a)
    print("possible")
    print(pos+1," ",d-a[0]+f)  
        
      
        
    
      
