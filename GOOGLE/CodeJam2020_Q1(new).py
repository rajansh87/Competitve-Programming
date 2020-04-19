import numpy
tt=int(input())
for qwerty in range(tt):
    n=int(input())
    ans="Case #"
    ans+=str(qwerty+1)+": "
    space=" "

    
    arr=numpy.array([list(map(int,input().split())) for i in range(n)])   
    row=0                 
    col=0                 
    s=0                 
    for i in range(n):
        if not(len(arr[i:i+1,:][0]) == len(numpy.unique(arr[i:i+1,:][0]))):
            row+=1
        if not(len(arr[:,i:i+1]) == len(numpy.unique(arr[:,i:i+1]))):
            col+=1
        s+=arr[i][i]



    ans+=str(s)+space+str(row)+space+str(col)
    print(ans)   #final=ouput from code
