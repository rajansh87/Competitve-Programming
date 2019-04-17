#include<stdio.h>
int main()
{
int T,K,P1,P2,s=0;
scanf("%d",&T);
while(T>0)
{
    scanf("%d%d%d",&P1,&P2,&K);
    s=P1+P2;
    s=s/K;
    if(s%2==0)
        printf("CHEF\n");
    else
        printf("COOK\n");
    T--;
}
return 0;
}
