#tt=int(input())
#for qwerty in range(tt):
    #n=int(input())
    #a,b=map(int,input().split())
    #arr=list(map(int,input().split()))

n=int(input())
arr=list(map(int,input().split()))

count=1
flag=False
for i in range(n-1):
    if arr[i]>=arr[i+1] and not flag:
        flag=True
        count+=1
        
    elif arr[i]<=arr[i+1] and flag:
        flag=False
        count+=1
        
print(count)
