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

void solve()
{
    ll n;
    cin>>n;
    ll arr[n][n];
    ll i,j;
    loop1
    {
        loop2
        {
            cin>>arr[i][j];
        }
    }
    ll k=0,r=0,c=0;
    loop1
    {
        k+=arr[i][i];
    }
    loop1
    {
        set<ll>s;
        bool dup=0;
        loop2
        {
            if(s.find(arr[i][j])!=s.end())
                dup=1;
            s.insert(arr[i][j]);

        }
        if(dup)
            r++;
    }
    loop1
    {
        set<ll>s;
        bool dup=0;
        loop2
        {
            if(s.find(arr[j][i])!=s.end())
                dup=1;
            s.insert(arr[j][i]);

        }
        if(dup)
            c++;
    }

    cout<<k<<" "<<r<<" "<<c;
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
