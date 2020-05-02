import math as mt #modules
modulus=100000000+7  #constant values


def MakeConnectionsForTree(city1, city2,joinedTreeLinks):    ##building tree
    joinedTreeLinks[city1].append(city2) 
    joinedTreeLinks[city2].append(city1)
    
#dfs algo new
def myFunctionToParseTreeForWay(anyrandomListestcaseostoreValues,u,v,anyrandomStackToStoreValues,joinedTreeLinks,BooleanVariable1,priceOfGoingFromCity):
    anyrandomStackToStoreValues.append(u) 
    if(u==v):
        BooleanVariable1=1
        FindTotalCostOfGoingToCity(anyrandomStackToStoreValues,priceOfGoingFromCity)
        return 
    anyrandomListestcaseostoreValues[u]=True
    BooleanVariable2=0
    if(len(joinedTreeLinks[u])>0): 
        for j in joinedTreeLinks[u]: 
            if(anyrandomListestcaseostoreValues[j]==False): 
                myFunctionToParseTreeForWay(anyrandomListestcaseostoreValues,j,v,anyrandomStackToStoreValues,joinedTreeLinks,BooleanVariable1,priceOfGoingFromCity) 
                if BooleanVariable1:
                    BooleanVariable2=1  
                    break
    if(BooleanVariable2==0): 
        del anyrandomStackToStoreValues[-1]   
    return


def FindTotalCostOfGoingToCity(wayTowardsTheCity,priceOfGoingFromCity):    #cost estimation function
    DictOfGivenData={}
    
    for i in range(len(wayTowardsTheCity)):
        DictOfGivenData=CheckForPrimeFactorsInDic(DictOfGivenData,priceOfGoingFromCity[wayTowardsTheCity[i]-1])

    AnyRandomVariable=list(DictOfGivenData.values())
    OutputestcaseoBeFoundAndPrint=1
    
    for i in range(len(AnyRandomVariable)):
        OutputestcaseoBeFoundAndPrint*=(AnyRandomVariable[i]+1)
        OutputestcaseoBeFoundAndPrint%=modulus
        
    print(OutputestcaseoBeFoundAndPrint)






def myNewFunctionToParseTreeForWay(u,v,n,anyrandomStackToStoreValues,joinedTreeLinks,priceOfGoingFromCity):  # DFS algo
    anyrandomListestcaseostoreValues=[0]*(n+1)
    BooleanVariable1=0
    if u==v:
        AnyRandomVariable=[u]
        FindTotalCostOfGoingToCity(AnyRandomVariable,priceOfGoingFromCity)
    else:
        myFunctionToParseTreeForWay(anyrandomListestcaseostoreValues,u,v,anyrandomStackToStoreValues,joinedTreeLinks,BooleanVariable1,priceOfGoingFromCity)
    return

def CheckForPrimeFactorsInDic(DictOfGivenData,zzccevff):   #check for factore for tree

    while(zzccevff%2==0):
        
        if (2 not in DictOfGivenData):
            DictOfGivenData[2]=1
            
        else:
            DictOfGivenData[2]+=1
            
        zzccevff/=2
        
    for i in range(3,int(mt.sqrt(zzccevff))+1,2):
        
        while(zzccevff%i==0): 
            if(i not in DictOfGivenData):
                DictOfGivenData[i]=1
                
            else:
                DictOfGivenData[i]+=1 
            zzccevff/=i
            
    if(zzccevff>2): 
        if(zzccevff not in DictOfGivenData):
            DictOfGivenData[zzccevff]=1
        else:
            DictOfGivenData[zzccevff]+=1
            
    return DictOfGivenData



def main():   #main Function
     #inputs
    testcase=int(input())
    for Test in range(testcase):
        n=input()
        n=int(n)
        joinedTreeLinks=[[] for vert in range(n+1)]  
        
        for z in range(n-1):
            a,b=input().split()
            b=int(b)
            a=int(a)
            
            MakeConnectionsForTree(a,b,joinedTreeLinks)#make tree

        priceOfGoingFromCity=list(map(int,input().split()))
        
        askedQuestion=int(input())
        
        for q in range(askedQuestion):
            anyrandomStackToStoreValues=[]
            a,b=input().split()
            b=int(b)
            a=int(a)
            myNewFunctionToParseTreeForWay(a,b,n,anyrandomStackToStoreValues,joinedTreeLinks,priceOfGoingFromCity)  #main code to solve
            
main()  #main function call
