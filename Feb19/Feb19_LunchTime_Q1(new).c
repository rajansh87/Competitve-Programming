#include<stdio.h>
int main()
{
long long int t;
scanf("%lld",&t);
while(t>0)
{
    long long int n,k,v;
    scanf("%lld%lld%lld",&n,&k,&v);
    long long int a[n],i;
    for(i=0;i<n;i++)
        {scanf("%lld",&a[i]);}
    long long int sum=0,x,var,avg=0;
    float number;
    for(i=0;i<n;i++)
    {
        sum=sum+a[i];
    }

    x=v*(n+k);
    var=x-sum;
    number=(var*1.0)/k;
    long long int p=number;
    if((number-p==0)&&(number>0))
        printf("%lld\n",p);
    else
        printf("-1\n");
t=t-1;
}
return 0;
}
