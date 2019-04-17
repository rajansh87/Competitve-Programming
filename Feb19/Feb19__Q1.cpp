#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t>0)
    {
       long long int n,a,b,k,tot=0,temp1,temp2,var1,var2;
       cin>>n>>a>>b>>k;

            if(n<a)
                temp1=0;
            else
                temp1=n/a;
            if(n<b)
                temp2=0;
            else
                temp2=n/b;

            var1=temp1+temp2;

            if(temp1==0 ||temp2==0)
                var2=0;
            else
                var2=n/(temp1*temp2);
            tot=var1-2*var2;

        if(tot>=k)
        {
            cout<<"Win\n";
        }
        else
        {
            cout<<"Lose\n";
        }
        t--;
    }
return 0;
}
