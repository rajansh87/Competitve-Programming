#t=int(input())
#for j in range(t):
#n,p,k=input().split(" ")
#n,p,k=int(n),int(n),int(k)
#a=list(map(int,input().split()))

n=int(input())
s=input()
ones=s.count("1")
zero=s.count("0")
if(ones!=zero):
    print(1)
    print(s)
else:
    print(2)
    print(s[0:n-1], " ", s[n-1])    
