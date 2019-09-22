import math
def JumpSearch(a,item,n):
    jump=math.sqrt(n)   #no. of blocks to jump = sqrt(n)
    i=0
    prev=0
    nxt=0
    while(a[i]<item and i<n):#jump till the bigger no.
        prev=i              #till the item dont come
        i+=int(jump)   #**jump**       
        nxt=i
        if(i>=n):
            return -1
    for i in range(prev,nxt+1):     #linear search between indexes
        if(a[i]==item):
            return i
            
    return -1
    
    

    

a=list(map(int,input().split()))
a.sort()         #array should be sorted
item=int(input("enter item to be searched : "))
pos=JumpSearch(a,item,len(a))
if(pos!=-1):
    print("element found at position : ",pos+1)
else:
    print("element not found")
#Time Complexity : sqrt(n)
#Space Complexity : O(1)
