##tt=int(input())
##for qwerty in range(tt):
##    n=int(input())
##    #n,k=input().split()
##    #n,k=int(n),int(k)
##    arr=list(map(int,input().split()))
##    
##
##  
n=int(input())
arr=list(map(int,input().split()))
for i in range(len(arr)):
    if(arr[i]=="Heads"):
        arr[i]=0
    else:
        arr[i]=1
count=0
ones=0
for i in range(len(arr)):
    if(arr[i]==0):
        count=0
    else:
        count+=1
        ones=max(ones,count)
#print(ones)
count=0
zeros=0
for i in range(len(arr)):
    if(arr[i]==1):
        count=0
    else:
        count+=1
        zeros=max(zeros,count)
#print(zeros)
ans=[zeros,ones]
print(ans)
            

