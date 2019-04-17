#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t;
    cin>>t;
    while(t--)
    {
        long long int n;
        cin>>n;
        string d[n];
        long long int a,b,c,x,e,i,j,co=0;
        string m;
        for(i=0;i<n;i++)
            cin>>d[i];
        for(i=0;i<n-1;i++)
        {
            for(j=i+1;j<n;j++)
            {
                m=d[i]+d[j];
                a=count(m.begin(),m.end(),'a');
                b=count(m.begin(),m.end(),'e');
                c=count(m.begin(),m.end(),'i');
                x=count(m.begin(),m.end(),'o');
                e=count(m.begin(),m.end(),'u');
                if(a>0 && b>0 && c>0 && x>0 && e>0)
                    co++;

                /*cout<<"\nstreing sarf : ";
                cout<<m<<" with pairs "<<i<<" "<<j<<endl;
                cout<<"a : "<<a<<endl;
                cout<<"e : "<<b<<endl;
                cout<<"i : "<<c<<endl;
                cout<<"o : "<<x<<endl;
                cout<<"u : "<<e<<endl;*/
            }
        }

        cout<<co<<endl;


    }

return 0;
}
