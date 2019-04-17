#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n,m,k,i,s=0;
        cin>>n>>m>>k;
        long long int a[k],b[k];
        for(i=0;i<k;i++)
            cin>>a[i]>>b[i];

        for(i=0;i<k-1;i++)
	    {
	        if(a[i+1]==a[i]+1 && b[i+1]==b[i])
	        	s++;
		}
		for(i=0;i<k-1;i++)
	    {
	         if(b[i+1]==b[i]+1 && a[i+1]==a[i])
	        	s++;
		}
	s=4*k-2*s;
	cout<<s<<endl;
    }

    return 0;
}
