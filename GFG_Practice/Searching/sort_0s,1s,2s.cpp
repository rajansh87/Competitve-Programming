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
        ll n,c1=0,c2=0,c3=0,i,j=0,temp=0,k=0;
        cin>>n;

        ll a[n],arr[n];
        loop1{cin>>a[i];}


        loop1
        {
            if(a[i]==0)
                c1++;
            else if(a[i]==1)
                c2++;
            else if(a[i]==2)
                c3++;
        }
        loopi(0,c1)
        {
            cout<<0<<" ";
        }
        loopi(0,c2)
        {
            cout<<1<<" ";
        }
        loopi(0,c3)
        {
            cout<<2<<" ";
        }
        cout<<endl;

   }
    return 0;
}
