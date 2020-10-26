#tt=int(input())
#for qwerty in range(tt):
    #n=int(input())
    #a,b=map(int,input().split())
    #arr=list(map(int,input().split()))

n=int(input())
s=input()
dic=dict()
for i in s:
    character_ascii=ord(i)
    if character_ascii not in dic:
        dic[character_ascii]=1
    else:
        dic[character_ascii]+=1

ma=max(dic.values())
print(ma)
