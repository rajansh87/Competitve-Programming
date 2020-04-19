
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
#define loopvar(var,a,b) for(var=a;var<b;var++)
#define rloopvar(var,a,b) for(var=a;var>b;var--)
int main()
{
    ll tt=1;
    test
    {
        ll n, k, p,i,j,e;
        cin>>n>>k>>p;
        //to solve
        vector<ll>arr2(p+5);
        loopi(1,n+1)
        {
            vector<ll>arr1(k+3);
            loopj(1,k+1)
            {
                cin>>arr1[j];
                arr1[j]+=arr1[j-1];
            }
            ll zero=0;
        for(j=p;j>=1;j--)
            {
                for(e=j-1;e>=max(zero,j-k);e--)
                    {
                        arr2[j]=max(arr2[e]+arr1[j-e],arr2[j]);
                    }
            }
        }
        cout<<"Case #"<<tt<<": "<<arr2[p]<<endl;
        tt++;
    }
    return 0;
}
