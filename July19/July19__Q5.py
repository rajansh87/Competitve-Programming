t=int(input())
for r in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  b=a[::-1]
  score=0
  score2=0
  s=0
  k=0
  temp=0
  s=10000000000000000000000
  while(len(a)!=1):
    s=10000000000000000000000000000000
    for i in range(len(a)):
      temp=a[i]+a[(i+1)%len(a)]
      if(temp<s):
        s=temp
        k=i
    a.insert(k,s)
    score+=s
    a.remove(a[k+1])
    a.remove(a[(k+1)%len(a)])
  #print(score)
  k=0
  temp=0
  s=10000000000000000000000
  while(len(b)!=1):
    s=10000000000000000000000000000000
    for i in range(len(b)):
      temp=b[i]+b[(i+1)%len(b)]
      if(temp<s):
        s=temp
        k=i
    b.insert(k,s)
    score2+=s
    b.remove(b[k+1])
    b.remove(b[(k+1)%len(b)])
  
  print(min(score,score2))
