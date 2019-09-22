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
        ll num,n;
        cin>>num;
        n=num-1;
        ll a[n],tot=0,i,j,k=0;
        loopi(0,n){cin>>a[i];}
        tot=(n+1)*(n+1+1)/2;                 //n*(n+1)/2
        loopi(0,n)
        {
            tot-=a[i];
            //cout<<"tot : "<<tot<<endl;
        }
        cout<<tot<<endl;





   }
    return 0;
}
