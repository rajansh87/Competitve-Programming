#include<stdio.h>
#include<math.h>
int main()
{
  long t,n;
  scanf("%d",&t);
  long j,i;
  for(j=0;j<t;j++)
 {
    scanf("%ld",&n);
    for(i=0;i<=n/26;++i)
     {
        if(0<n && n<=2)
            {printf("1 0 0\n");
              break;}
        else if(2<n && n<=10)
            {printf("0 1 0\n");
                break;}
        else if(10<n&& n<=26)
            {printf("0 0 1\n");
                 break;}
        long long k=pow(2,i);
        if(26*i<n && n<=26*i+2)
            {printf("%lld 0 0\n",k);
            break;}
        else if(26*i+2<n && n<=26*i+10)
     {printf("0 %lld 0\n",k);
             break;}
    else if(26*i+10<n && n<=26*(i+1))
      {printf("0 0 %lld\n",k);
             break;}
     }
 }
 return 0;
}
