#modules
import math as mt
import random as rm
def main():
    testcase=input()
    testcase=int(testcase) #trstcase input taken
    while(testcase>0):#loop for testcases
        var1,var2,var3=input().split(" ")
        var1=int(var1)
        var2=int(var2)
        var3=int(var3)
        z=0
        while(z<var1):
            arr=input().split(" ")
            z+=1
        #input done
################################################################
        z=0
        outputArray=[]
        while(z<var1):
            lets_take_value=rm.randrange(1,var2+1)  #randomly choose values
            outputArray.append(lets_take_value)    #store output in array/list
            z+=1
        z=0
################################################################            
    
        print(*outputArray,sep=" ")#final output
        

     

################################################################
        
        testcase-=1   #decrement to run testcases
            
main()   #mainfunction

################################################################                
        
    
