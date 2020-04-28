#module
from collections import Counter

#constant variables

#start
def MostOccuringNum(arr): #addition Functions
    z=Counter(arr).most_common()[0][0]
    return z


def main():   #main function
    tt=int(input())
    for qwerty in range(tt):
        #n=int(input())
        #arr=list(map(int,input().split()))
        #n,m,st=map(int,input().split())
        #inputs
        n,m,k=input().split(" ")
        n=int(n)
        m=int(m)
        k=int(k)
        data=[]
        #data=[[0 for i in range(n)]for j in range(k)]
        
        for i in range(n):
            temp=list(map(int,input().split()))
            data.append(temp)
        for i in range(n):
            data[i:i+k].sort()
            ma=1
            c=1
            temp=data[i][0]
            for j in range(1,k):
                if data[i][j]==data[i][j-1]:
                    c+=1
                else:
                    if c>ma:
                        ma=c
                        temp=data[i][j-1]
                    c=1
            if c>ma:
                ma=c
                temp=data[i][k-1]
            print(temp,end=" ")  #finaloutput
        print()
            
main()  #main function call
    
#end
