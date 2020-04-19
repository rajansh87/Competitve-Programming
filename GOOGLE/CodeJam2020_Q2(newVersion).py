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
ll i,j;
void solve()
{
    string s;
    cin>>s;
    ll dep=0;
    string ans;
    for(char c:s)
    {
        ll newdep=c-'0';
        while(newdep>dep)
        {
            dep++;
            ans+="(";
        }
        while(newdep<dep)
        {
            dep--;
            ans+=")";
        }
        ans+=c;
    }
    while(dep>0)
        {
            dep--;
            ans+=")";
        }
        cout<<ans;



}


int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    ll testcase=1;
    test
    {
        cout<<"Case #"<<testcase<<": ";
        solve();
        cout<<endl;

        testcase++;
    }
    return 0;
}
