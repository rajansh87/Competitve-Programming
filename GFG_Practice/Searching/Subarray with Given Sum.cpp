#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define loop1 for(i=0;i<n;i++)
#define loop2 for(j=0;j<n;j++)
#define loopi(a,b) for(i=a;i<b;i++)
#define loopj(a,b) for(j=a;j<b;j++)
#define rloopi(a,b) for(i=a;i>b;i--)
#define rloopj(a,b) for(j=a;j>b;j--)
#define test long long int t;cin>>t;while(t--)
int main()
{
   test
   {
        ll n,sum=0,i,j,c=0,curSum=0,mini=10000000000000000,i1=0,i2=0;
        cin>>n>>sum;
        ll a[n];
        loop1{cin>>a[i];}
        j=0;
        curSum=a[0];
        loopi(1,n+1)
        {
            while(curSum>sum && j<i-1)
                {
                    curSum-=a[j];
                    j++;
                }
            if(curSum==sum)
                {
                        i1=j;
                        i2=i-1;
                        mini=24;
                        break;
                }

            if(i<n)
                curSum+=a[i];
        }
        if(mini==10000000000000000)
            cout<<-1<<endl;
        else
            cout<<i1+1<<" "<<i2+1<<endl;


   }
    return 0;
}
