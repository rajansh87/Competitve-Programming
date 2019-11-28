n=int(input())
s=str(n)
st=""
for i in range(len(s)):
    x=int(s[i])**2
    st=st+str(x)

print(st)
