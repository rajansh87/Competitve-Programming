import numpy
tt=int(input())
for qwerty in range(tt):
    #n=int(input())
    stri=input()
    ans="Case #"
    ans+=str(qwerty+1)+": "
    space=" "
    ##############################
#    input  completed
########################
    result =""         
    temp=0
    openb="("   #pattern
    closeb=")"   #pattern
    for i in range(len(stri)):   #creating start part
        if i==0:       #intital                 
            result+=(openb*int(stri[i])+stri[i])  
            temp+=int(stri[i])
        else:      #for rest
            if int(stri[i]) == int(stri[i-1]):     
                result+=stri[i]
            elif int(stri[i]) < int(stri[i-1]):          
                temp -= (int(stri[i-1])-int(stri[i]))
                result+=(closeb*(int(stri[i-1])-int(stri[i]))+stri[i])
            else:                                           
                temp += (int(stri[i])-int(stri[i-1]))
                result+=(openb*(int(stri[i])-int(stri[i-1]))+stri[i])
                
    result+=(closeb*temp)    #end part


    ans+=result
    print(ans)   #final=ouput from code
