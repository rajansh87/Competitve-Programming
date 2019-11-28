def even(a):
    for i in range(len(a)):
        if(a[i]%2!=0):
            return a[i]
def odd(a):
    for i in range(len(a)):
        if(a[i]%2==0):
            return a[i]
            

a=list(map(int,input().split()))
ans=0
if(a[0]%2==0):
    if(a[1]%2==0):
        ans=even(a)
    else:
        if(a[2]%2==0):
            ans=even(a)
        else:
            ans=odd(a)
elif(a[0]%2!=0):
    if(a[1]%2!=0):
        ans=odd(a)
    else:
        if(a[2]%2!=0):
            ans=odd(a)
        else:
            ans=even(a)
print(ans)
        
