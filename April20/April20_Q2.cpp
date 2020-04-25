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
    ll n;
    cin>>n;
    ll arr[n];
    loop1{cin>>arr[i];}
    sort(arr,arr+n);
    reverse(arr,arr+n);
//ll  space=6;
//bool var=true;
ll rate=1 ;
    loopi(0,n-1)
    {
     	if(0<arr[i+1]-rate)
		{
			arr[i+1]=arr[i+1]-rate;
			rate++;
		}  
	else
	{
		arr[i+1]=0;
	}
}
ll result=0;
loop1
{
result+=arr[i];
}
cout<<result%(1000000000+7)<<endl;

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
