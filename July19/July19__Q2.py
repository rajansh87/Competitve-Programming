t=int(input())
for r in range(t):
  n=int(input())
  k=int(input())
  n1=k//n
  x=k-n*n1
  ans=0
  if(x==n or x==0):
    ans=0
  elif(x<n/2):
    ans=2*x
  elif(x==n/2):
    ans=n-1
  elif(x>n/2):
    ans=2*(n-x)
  print(ans)
      
    
  
