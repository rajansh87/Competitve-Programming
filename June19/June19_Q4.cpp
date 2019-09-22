#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n,k,ans=0,x,z,m,y,p=pow(10,9)+7;
        cin>>n>>k;
        n=n+k-1;
        x=2*k-n-1;
        z=n-k;
        m=0;
        if(x>0)
        {
            m=x/z+1;
            y=x-((m-1)*z);
            if(n%2==0)
                {
                    m=m/2;
                    ans=(m%p)*((x+y)%p);
                }
            else{
                    x=(x+y)/2;
                    ans=(m%p)*((x)%p);
                }
                ans=ans%p;
        }
        cout<<((ans+k-1)%p)<<endl;;
    }


    return 0;

}
