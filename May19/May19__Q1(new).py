# cook your dish here
t=input()
t=int(t)
a=[]
a.append(0)
a.append(1)
for i in range(2,(10**6)+1):
    p=a[i-1]+i+i*a[i-1]
    p=p%(1000000007)
    a.append(p)
while(t>0):
    n=input()
    n=int(n)
    print(a[n])
    #print("y4")
    t=t-1
