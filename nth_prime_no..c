#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 100000000

void prime(int n)
{
    int i,j,count=0;

    if (n == 1) {
        printf("2\n");
        return;
    }
    for(i=3;i<=MAX;i+=2)
    {
        int isPrime=1;
        int jMax = sqrt(i);
        for(j=3;j<=jMax;j+=2)
        {
            if(i%j==0)
            {
                isPrime=0;
                break;
            }
        }
        if(isPrime)
        {
            if(++count==n)
            {
                printf("%d\n",i);
                return;
            }
        }
    }
}

int main()
{
   int n,i;
printf("\nEnter position : ");
   scanf("%d",&n);
   //int arr[n];
   printf("\nPrime No. at position %d is : ",n);
prime(n+1); //since it was giving answer for 1 previous no.
/*
   for(i=0;i<n;i++)
   {
       scanf("%d",&arr[i]);
   }
   for(i=0;i<n;i++)
   {
       prime(arr[i]);
   }
*/
   return 0;
}
