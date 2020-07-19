def modFact(n, p): 
	if n >= p: 
		return 0	

	result = 1
	for i in range(1, n + 1): 
		result = (result * i) % p 

	return result 

tt=int(input())
for qwerty in range(tt):
    #n=int(input())
    a,b=map(int,input().split())
    #arr=list(map(int,input().split()))            
    p=1
    p=modFact(a,b)
    print(p)
