s="1203456"
st=s
st=list(st)
st=[int(i) for i in st]
st.sort()
ss=""
ss=s
ans=[]
##for i in range(len(st)):
##    ss+=str(st[i])
for i in range(0,len(ss)-1):
    if(int(ss[i])<int(ss[i+1])):
        prod=int(ss[i])*int(ss[i+1])
        if(str(prod) in ss):
            ans.append(str(prod))
print(ans)
            
