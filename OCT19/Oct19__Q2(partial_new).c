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
{   test{
    ll n,m,i,j,q,e,x,y,k;
    cin>>n>>m>>q;
    ll a1[n+1][m+1]={},a2[n+1][m+1]={};
    //ll r[n]={},c[m]={};
    loopi(0,q)
    {
        cin>>x>>y;
        a1[x][1]++;
        a2[1][y]++;
    }
    loopi(1,n+1)
    {
        loopj(1,m+1)
        {
            a1[i][j]=a1[i][j]+a1[i][j-1];
        }
    }
    loopi(1,m+1)
    {
        loopj(1,n+1)
        {
            a2[j][i]=a2[j][i]+a2[j-1][i];
        }
    }
    ll c=0;
    loopi(1,n+1)
    {
        loopj(1,m+1)
        {
            a1[i][j]+=a2[i][j];
            if(a1[i][j]%2!=0)
            {
                c++;
            }
        }
    }
    cout<<c<<endl;


}
    return 0;
}
