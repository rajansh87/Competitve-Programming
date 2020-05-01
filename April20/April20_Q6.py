import math
def main():
    testcase=input()
    testcase=int(testcase)
    for test in range(testcase):#loop for testcases
        number=int(input())
        inputArray=list(map(int,input().split()))  #list input
        dbArray=[[-1,0]]    #database
        #input done
################################################################
        z=0
        for z in range(number):
            tempVariable=abs(inputArray[z])#absolute value
            
            
            if(tempVariable%4==2):
                dbArray.append([z,1])
                
                
            elif(tempVariable%4==0):
                dbArray.append([z,0])
                
                

################################################################
        dbArray.append([number,0])
        
        result=(number*(number+1))//2
        

        z=1
        for z in range(1,len(dbArray)-1,1):
            if dbArray[z][1]==0:
                continue
            
            tempVariable=dbArray[z][0]-dbArray[z-1][0]            
            tempVariable=tempVariable*(dbArray[z+1][0]-dbArray[z][0])

            result=result-tempVariable
            
################################################################            
        print(result)   #final output
        
        #testcase-=1   #decrement to run testcases
            
main()   #mainfunction

################################################################                
        
    
