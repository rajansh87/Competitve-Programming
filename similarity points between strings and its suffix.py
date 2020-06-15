s="ababaa"



def all_suffixes(s):
    return [s[-i:] for i in range(1, len(s) + 1)]

suf=all_suffixes(s)
re=[]
for ss in suf:
    a=[ss,s]
    size = len(a)
    ans=""
    if (size == 0): 
        ans=""
        re.append(ans)
        continue

    if (size == 1): 
        ans=a[0]
        re.append(ans)
        continue
    a.sort() 
    end = min(len(a[0]), len(a[size - 1])) 

    i = 0
    while (i < end and a[0][i] == a[size - 1][i]): 
        i += 1

    pre = a[0][0: i] 
    ans = pre
    re.append(ans)
    continue

sim=0
for i in re:
    sim+=len(i)
print(sim)
    
