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
    ll num;
    cin>>num;
    if(num==1)
    {
        cout<<"1"<<endl<<"1 1"<<endl;
        return;
    }

    cout<<num/2<<endl;
    loopi(0,num/2)
    {
        if(i==0 && num%2==1)
            cout<<"3 ";
        else
            cout<<"2 ";
        cout<<(2*i)+1<<" "<<(2*i+2)<<" ";
        if(num%2==1 && i==0)
        {
            cout<<num<<endl;
        }
    }
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
