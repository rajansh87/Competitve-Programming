##tt=int(input())
##for qwerty in range(tt):
##    n=int(input())
##    #n,k=input().split()
##    #n,k=int(n),int(k)
##    arr=list(map(int,input().split()))
##    
##
##  
win_suit=input()
n=int(input())
for nn in range(n):
    suit1,num1,suit2,num2=input().split()
    num1,num2=int(num1),int(num2)
    if(suit1==win_suit and suit2!=win_suit):
        print("Player 1 wins")

    elif(suit1!=win_suit and suit2==win_suit):
        print("Player 2 wins")

    else:
        if(num1>num2):
            print("Player 1 wins")

        elif(num1<num2):
            print("Player 2 wins")

        else:
            print("Draw")
        

