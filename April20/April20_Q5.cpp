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
bool checkPrime(ll n)
{
    if(n<=1){return false;}
    if(n<=3){return true;}
    if(n%2==0 || n%3==0){return false;}
    for(ll i=5;i*i<=n;i=i+6){if(n%i==0 || n%(i+2)==0){return false;}}
    return true;
}
ll i,j;
void solve()
{
    ll n,m,k;
    cin>>n>>m>>k;
    ll faltu=0;
    ll newfaltu;
    loop1
    {
        loopj(0,m)
        {
            cin>>newfaltu;
        }
    }
    ll finalresult;
    loop1
    {
       finalresult=rand()%m+1;
       cout<<finalresult<<" ";
    }
    cout<<endl;

}


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    test
    {
        solve();
    }

    /*ll testcase=1;
    test
    {
        cout<<"Case #"<<testcase<<": ";
        solve();
        cout<<endl;

        testcase++;
    }*/
    return 0;
}
