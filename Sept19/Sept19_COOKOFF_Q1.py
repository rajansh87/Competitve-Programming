def matches(n):
     if(n==0):
          return 6
     elif(n==1):
          return 2
     elif(n==2):
          return 5
     elif(n==3):
          return 5
     elif(n==4):
          return 4
     elif(n==5):
          return 5
     elif(n==6):
          return 6
     elif(n==7):
          return 3
     elif(n==8):
          return 7
     elif(n==9):
          return 6
    
     
t=int(input())
for u in range(t):
     a,b=input().split(" ")
     a,b=int(a),int(b)
     s=a+b
     st=str(s)
     c=0
     for i in range(len(st)):
          c+=matches(int(st[i]))
     print(c)
          
     
     
