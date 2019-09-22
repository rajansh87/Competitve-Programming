#include <bits/stdc++.h>
using namespace std;
#define ll long long int
void optimizeIO(){
	ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
}
int main()
{
    optimizeIO();
	ll n,m,x,z,q,i,t,e,o,j;
	cin>>t;
	while(t--)
	{
	    set<ll> s;
	    set<ll> st;
	    pair< set<ll>::iterator,bool> result;
	    set<ll>:: iterator itr;
	    o=e=0;
	    ll a[199999]={0};
	    cin>>q;
	    while(q--)
	    {
	        cin>>x;
	        if(s.size()==0)
	        {
	            s.insert(x);
	            a[x]=1;
	            z=__builtin_popcount(x);
	            if(z%2==0)
	            e++;
	            else o++;
	            
	            cout<<e<<" "<<o<<endl;
	            continue;
	        }
	        if(a[x]==1)
	        {
	            cout<<e<<" "<<o<<endl;
	        }
	        else
	        {
	            for(auto i:s)
	            {
	                m=i^x;
	     
	                //cout<<"zorv: "<<m<<" with: "<<i<<endl;
	                result=st.insert(m);
	                if(result.second==true)
	                {
	                    z=__builtin_popcount(m);
	                    //st.insert(m);
	                    a[m]=1;
	                    if(z%2==0)
	                    e++;
	                    else
	                    o++;
	                }
	            }
	                result=st.insert(x);
	                if(result.second==true)
	                {
	                    z=__builtin_popcount(x);
	                    //st.insert(x);
	                    a[x]=1;
	                    if(z%2==0)
	                    e++;
	                    else 
	                    o++;
	                }
	                cout<<e<<" "<<o<<endl;
	                s.insert(st.begin(),st.end());
	                //st.clear();
	        }
	    }
	    //s.clear();
	}
	return 0;
}
