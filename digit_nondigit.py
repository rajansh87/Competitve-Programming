s="*/24#5%7&9*3@"
st=s
c=0
non=[]
dig=""
for i in range(len(s)):
    if(s[i].isdigit()):
        dig+=s[i]
    else:
        non.append(s[i])
if(len(non)%2!=0):
    odd=""
    even=""
    for i in range(len(dig)):
        if(int(dig[i])%2==0):
            even+=dig[i]
        else:
            odd+=dig[i]
    print(int(even),int(odd))
  
            
