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
    ll testcase=1;
    test
    {
        ll n;
        cin>>n;
        ll i,j,arr[n][n];
        loop1
        {
            loop2
            {
                cin>>arr[i][j];
            }
        }
        ll count=0;
        ll s=0;
        i,j=0,0;
        loop1
        {
            j=i;
            s+=arr[i][j];
        }
        ll rowRepeat=0,colRepeat=0,mrow=0,mcol=0;
        loop2{
        ll freq1[1000]={0};
        loop1
        {
            freq1[arr[j][i]]++;
        }
        loopi(0,1000)
        {
            if(freq1[i]>1)
                mrow++;
        }
        if(mrow>0)
            count++;
        mrow=0;
        }
        mrow=count;
        count=0;




loop2{
        ll freq1[1000]={0};
        loop1
        {
            freq1[arr[i][j]]++;
        }
        loopi(0,1000)
        {
            if(freq1[i]>1){
                mcol++;
                }
        }
        if(mcol>0)
            count++;
        mcol=0;
        }
        mcol=count;
        count=0;



        cout<<"Case #"<<testcase<<": "<<s<<" "<<mrow<<" "<<mcol<<endl;
        testcase++;

    }
    return 0;
}
