s=input()
arr=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(s)):
    if(s[i]=="a"):
        arr[0]+=1
    elif(s[i]=="b"):
        arr[1]+=1
    elif(s[i]=="c"):
        arr[2]+=1
    elif(s[i]=="d"):
        arr[3]+=1
    elif(s[i]=="e"):
        arr[4]+=1
    elif(s[i]=="f"):
        arr[5]+=1
    elif(s[i]=="g"):
        arr[6]+=1
    elif(s[i]=="h"):
        arr[7]+=1
    elif(s[i]=="i"):
        arr[8]+=1
    elif(s[i]=="j"):
        arr[9]+=1
    elif(s[i]=="k"):
        arr[10]+=1
    elif(s[i]=="l"):
        arr[11]+=1
    elif(s[i]=="m"):
        arr[12]+=1
    elif(s[i]=="n"):
        arr[13]+=1
    elif(s[i]=="o"):
        arr[14]+=1
    elif(s[i]=="p"):
        arr[15]+=1
    elif(s[i]=="q"):
        arr[16]+=1
    elif(s[i]=="r"):
        arr[17]+=1
    elif(s[i]=="s"):
        arr[18]+=1
    elif(s[i]=="t"):
        arr[19]+=1
    elif(s[i]=="u"):
        arr[20]+=1
    elif(s[i]=="v"):
        arr[21]+=1
    elif(s[i]=="w"):
        arr[22]+=1
    elif(s[i]=="x"):
        arr[23]+=1
    elif(s[i]=="y"):
        arr[24]+=1
    elif(s[i]=="z"):
        arr[25]+=1
c=0
for i in range(len(arr)):
    if(arr[i]>1):
        c+=1
print(c)
