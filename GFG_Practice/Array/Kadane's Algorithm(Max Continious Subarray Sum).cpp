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
        ll n,sum=0,i,j,c=0,curSum=0,maxi=INT_MIN,i1=0,i2=0,mini=0;
        cin>>n;
        ll a[n];
        loop1{cin>>a[i];}

        loop1
        {
            curSum+=a[i];
            if(maxi<curSum)
                maxi=curSum;
            if(curSum<0)
                curSum=0;
        }
        //if(maxi!=0)
            cout<<maxi<<endl;


   }
    return 0;
}
