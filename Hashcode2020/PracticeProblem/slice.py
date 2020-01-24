#t = int(input())
#for qwerty in range(t):
n,m=input().split()
n,m=int(n),int(m)
    #n=int(input())
arr=list(map(int,input().split()))
brr=arr.copy()
s=0
c=0
ans=[]
temp=[]
t=[]
ma=0
z=66
x=0
for i in range(m):
    s=sum(temp)
    for j in range(len(arr)):
        if(s+arr[j]<=n):
            c=s+arr[j]
            if(c>ma):
                ma=c
                x=arr[j]
                z=99
        else:
            z=66
    if(z==99):
        temp.append(x)
        arr.pop(arr.index(x))
                
        


            
#print(c)
#print(temp)
if(c!=sum(temp)):
    for i in range(len(arr)):
        if(c==(sum(temp)+arr[i])):
            temp.append(arr[i])
            break
    #print(temp)


ans=[]
x=0
i=0
for i in range(len(temp)):
    x=brr.index(temp[i])
    ans.append(x)
    brr[x]=-999999999

    
ans.sort()
print(len(ans))
print(*ans,sep=" ")



                            
