#include<bits/stdc++.h>
using namespace std;
#define ll long long int
void solve()
{
    vector<pair<ll,ll>> arr;
    ll n,i,j,k,m,x,y;
    cin>>n;
   while(n--)
   {
       //make pairs
       cin>>m;       
       for(i=0;i<m;++i)
       {
           cin>>x>>y;
           arr.push_back(make_pair(x,y));//insertion
       }
   }
   ll z;
   sort(arr.begin(),arr.end());
   z=65;
    ll a=arr[0].first;
    ll b=arr[0].second;
    if(a>1)//condition
    {
        cout<<1<<endl;
        return;
    }
    for(i=1;i<arr.size();i++)//final
    {   
        if(b+1>=arr[i].first)
            b=max(b,arr[i].second);
        else
        {   
            cout<<b+1<<endl;
            return;
        }            
    }
    cout<<b+1<<endl;
}
int main()
{
solve();//function call
return 0;
}