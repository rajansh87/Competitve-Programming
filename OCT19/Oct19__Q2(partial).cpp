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
    ll n,m,i,j,q,e,x,y;
    cin>>n>>m>>q;
    ll a[n][m]={};
    for(e=0;e<q;e++)
    {
        cin>>x>>y;
        x--;
        y--;
        loopi(0,m)
        {
            a[x][i]++;
        }
        loop2
        {
            a[j][y]++;
        }
    }
    ll c=0;
    loop1
    {
        loopj(0,m)
        {
            if(a[i][j]%2!=0)
                c++;
        }
    }
    cout<<c<<endl;



   /* loop1
    {
        loopj(0,m)
        {
            cout<<a[i][j]<<"    ";
        }
        cout<<endl;
    }*/

    /////////////////////////////////////////////////////////
    /*
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
    ll a[n][m]={};
    ll r[n]={},c[m]={};
    for(e=0;e<q;e++)
    {
        cin>>x>>y;
        x--;
        y--;
        r[x]++;

        c[y]++;
    }
    loopi(0,n)
    {
        for(k=0;k<r[i];k++)
        {
            loopj(0,m)
            {
                a[i][j]++;
            }
        }
    }
    loopi(0,m)
    {
        for(k=0;k<c[i];k++)
        {
            loopj(0,n)
            {
                a[j][i]++;
            }
        }
    }



    loopi(0,n)
    {
        cout<<r[i]<<"   ";
    }
    cout<<endl;
    loopi(0,m)
    {
        cout<<c[i]<<"   ";
    }


   ll count=0;
    loop1
    {
        loopj(0,m)
        {
            if(a[i][j]%2!=0)
                count++;
        }
    }
    cout<<count<<endl;



    /*loopi(0,n)
    {
        loopj(0,m)
        {
            cout<<a[i][j]<<"    ";
        }
        cout<<endl;
    }





}
    return 0;
}


    */
    /////////////////////////////////////////////////////////





}
    return 0;
}
