# cook your dish here
a=[]
a.append(0)
#print("1")
for i in range(1,100000+1):
    a.append(i)

k=0
var=0
#print("2")
for i in range(0,10000):
    var=a[k]+a[k+1]+a[k]*a[k+1]
    a[i+1]=var
    k=k+1
#print("3")
t=input()
t=int(t)

while(t>0):
    n=input()
    n=int(n)
    print((a[n])%(1000000007))
    #print("y4")
    t=t-1
