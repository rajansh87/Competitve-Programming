#include <bits/stdc++.h>
using namespace std;
#define ll long long int

set<ll> s;
void prime(ll n)  
{  
    while (n % 2 == 0)  
    {  
        s.insert(2);  
        n = n/2;  
    }  
    for (ll i = 3; i <= sqrt(n); i = i + 2)  
    {  
        while (n % i == 0)  
        {  
            s.insert(i);  
            n = n/i;  
        }  
    }  
    if (n > 2)  
        s.insert(n);  
}
int main()
{
 
	ll m,x,z,q,i,t,e,o,j,a1=131072,a2=177147,y;
	string ss;
	cin>>t;
	cout<<endl;
	while(t--)
	{
	   cout<<1<<" "<<a1<<endl;
	   cin>>x;
	   cout<<endl;
	   
	   prime((a1*a1)-x);
	   /*for(auto j:s)
	   cout<<j<<" ";
	   cout<<endl;*/
	   
	   cout<<1<<" "<<a2<<endl;
	   cin>>y;
	   cout<<endl;
	   
	   q=a2*a2;
	   
	   for(auto i:s)
	   {
	       if(q%i==y){
	       e=i;
	       }
	   }
	   cout<<2<<" "<<e<<endl;
	   cin>>ss;
	   cout<<endl;
	   s.clear();
	   if(ss=="Yes")
	   continue;
	   else if(ss=="No") 
	   break;
	}
	return 0;
}
