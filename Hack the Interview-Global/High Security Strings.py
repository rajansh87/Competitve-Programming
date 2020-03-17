##tt=int(input())
##for qwerty in range(tt):
##    n=int(input())
##    #n,k=input().split()
##    #n,k=int(n),int(k)
##    arr=list(map(int,input().split()))
##    
##
##  
s=input()
weight=int(input())
arr=[0]*26
arr[0]=weight
for i in range(1,26):
    arr[i]=(weight+i)%26
strength=0
for i in range(len(s)):
    strength+=arr[(ord(s[i])-97)]
print(strength)
    

            

